from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from metadata.models import Account
import requests
import random
import string

from web3 import Web3
from hexbytes import HexBytes
from eth_account.messages import encode_defunct

class Redirect_API(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request, sendBy:str=None, receiver:str=None):
        receiver = receiver.lower()
        sendBy = sendBy.lower()
        try:
            receiver_account = Account.objects.get(address=receiver)
            sender_account = Account.objects.get(email=sendBy)
        except:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        if receiver_account.reachable == True:
            return Response({"status": "success", "data": receiver_account.email}, status=status.HTTP_200_OK)
        if not sender_account in receiver_account.authorized.all():
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": "success", "data": receiver_account.email}, status=status.HTTP_200_OK)

class Sender_API(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request, sendBy=None):
        try:
            sender_account:Account = Account.objects.get(email=sendBy)
        except:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        if sender_account.name:
            from_header = (f"{sender_account.name} <{sender_account.address}>")
        else:
            from_header = (f"<{sender_account.address}>")
        return Response({"status": "success", "data": from_header}, status=status.HTTP_200_OK)

class Status_API(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, sender=None, receiver=None):
        sender = sender.lower()
        receiver = receiver.lower()
        receiver = f"{receiver}@joinmic.xyz"
        try:
            receiver_account = Account.objects.get(address=receiver)
            sender_account = Account.objects.get(email=sender)
            if sender_account in receiver_account.authorized.all():
                return Response({"status": "authorized"}, status=status.HTTP_200_OK)
            return Response({"status": "not authorized"}, status=status.HTTP_200_OK)
        except:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
class Manage_API(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, sender=None, receiver=None, sig=None, email=None):
        try:
            sender = sender.lower()
            sender_account = Account.objects.get(email=sender)
        except:
            return Response({"status": "Bad sender"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            w3 = Web3(Web3.HTTPProvider(""))
            message= encode_defunct(text=f"Authorize {sender} to send mails")
            address = w3.eth.account.recover_message(message,signature=HexBytes(sig))
            mic_mail = f"{receiver.lower()}@joinmic.xyz"
            if (address == receiver):
                if (email is None):
                    receiver_account = Account.objects.get(address=mic_mail)
                else:
                    if Account.objects.filter(address=mic_mail).count()>0:
                        return Response({"status": "error", "message":"This account already exist"}, status=status.HTTP_400_BAD_REQUEST)
                    characters = string.ascii_letters + string.digits + string.punctuation
                    password = ''.join(random.choice(characters) for i in range(15))
                    headers = {
                        'accept': 'application/json',
                        'X-API-Key': 'DF0CF4-95032C-254123-9206D9-424D28',
                        'Content-Type': 'application/json',
                    }
                    json_data = {
                        'active': '1',
                        'domain': 'joinmic.xyz',
                        'local_part': receiver,
                        'password': password,
                        'password2': password,
                        'quota': '3072',
                        'force_pw_update': '1',
                        'tls_enforce_in': '1',
                        'tls_enforce_out': '1',
                    }
                    response = requests.post('http://mail.joinmic.xyz/api/v1/add/mailbox', headers=headers, json=json_data)
                    if (response.json()[0]["type"] == "danger"):
                        return Response({"status": "error", "message": response.json()[0]["msg"]}, status=status.HTTP_400_BAD_REQUEST)
                    receiver_account = Account.objects.create(address=mic_mail, email=email)
                receiver_account.authorized.add(sender_account)
                return Response({"status": "success"}, status=status.HTTP_200_OK)
            return Response({"status": "error", "message":"wrong sig"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"status": "error"}, status=status.HTTP_409_CONFLICT)