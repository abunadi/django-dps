import requests

from django.test import TestCase, RequestFactory
from django.utils.six import text_type
from django_dps.transactions import make_payment

from .models import Payment


class DpsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_interactive(self):
        amount = 112.45
        payment = Payment.objects.create(amount=amount)

        request = self.factory.get('/', HTTP_HOST='localhost:8000')
        response = make_payment(payment, request=request)
        self.assertEqual(response.status_code, 302)
        response = requests.get(response['Location'])

        # check the dps page looks approximately correct
        self.assertIn('Payment Checkout', response.text)
        self.assertIn(text_type(amount), response.text)

    def test_recurring(self):
        pass
