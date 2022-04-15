from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from hexbytes import HexBytes
from rest_framework.test import APIRequestFactory
from web3 import Web3
from api.views import Manage_API
from metadata.models import Account
from django.contrib.auth.models import User
from eth_account.messages import encode_defunct
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

class RedirectestCase(TestCase):
    def setUp(self):
        user = User.objects.create_superuser(username='admin')
        token = Token.objects.create(user=user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        account1 = Account.objects.create(address="0x450417Aa753738e93AD13A1415Bfc251D4e26A45@joinmic.xyz", email="test1@live.fr", reachable=True)
        account2 = Account.objects.create(address="0x64aa2b38369ced9acacf5cb234d8a29469735baf@joinmic.xyz", email="test2@live.fr")
        
       
        request = client.get(f'/redirect/test1@live.fr/0x64aa2b38369ced9acacf5cb234d8a29469735baf@joinmic.xyz')
        account2.authorized.add(account1)
        self.assertEqual(request.data["status"], 'error')
        request = client.get(f'/redirect/test1@live.fr/0x64aa2b38369ced9acacf5cb234d8a29469735baf@joinmic.xyz')
        self.assertEqual(request.data["status"], 'success')
        self.assertEqual(request.data["data"], 'test2@live.fr')