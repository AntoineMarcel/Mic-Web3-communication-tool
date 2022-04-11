from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from metadata.models import Account, Sender

class Redirect_API(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, sendBy=None, receiver:str=None):
        receiver = receiver.lower()
        try:
            account = Account.objects.get(address=receiver)
            sender = Sender.objects.get(sender=sendBy)
        except:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        if not sender in account.authorized.all():
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": "success", "data": account.email}, status=status.HTTP_200_OK)

class Sender_API(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, sendBy=None):
        try:
            sender = Sender.objects.get(sender=sendBy)
        except:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        from_header = (f"{sender.name} <{sender.sender.split('@')[0]}@joinmic.xyz>")
        return Response({"status": "success", "data": from_header}, status=status.HTTP_200_OK)