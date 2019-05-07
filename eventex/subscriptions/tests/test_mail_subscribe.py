from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        """ Valid POST should redirect to /inscricao/ """
        data = dict(name='Flávio Tassan', cpf='12345678901',
                    email='tassanf@gmail.com', phone='33-99929-2404')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'tassanf@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Flávio Tassan',
            '12345678901',
            'tassanf@gmail.com',
            '33-99929-2404'
        ]

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)


