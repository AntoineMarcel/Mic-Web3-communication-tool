from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from metadata.models import Account, Sender

class Banner_API(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, sendBy=None, receiver=None):
        try:
            account = Account.objects.get(address=receiver)
            sender = Sender.objects.get(sender=sendBy)
        except:
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        if not sender in account.authorized.all():
            return Response({"status": "error"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"status": "success", "data": [sender.name, account.email]}, status=status.HTTP_200_OK)