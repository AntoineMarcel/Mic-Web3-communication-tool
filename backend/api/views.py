from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from metadata.models import Account

class Redirect_API(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, sendBy:str=None, receiver:str=None):
        receiver = receiver.lower()
        sendBy = sendBy.lower()
        try:
            receiver_account = Account.objects.get(address=receiver)
            sender_account = Account.objects.get(email=sendBy)
        except:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        if not sender_account in receiver_account.authorized.all():
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": "success", "data": receiver_account.email}, status=status.HTTP_200_OK)

class Sender_API(APIView):
    authentication_classes = []
    permission_classes = []
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