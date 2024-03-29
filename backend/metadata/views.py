from .models import Account
from django.http import HttpResponse
from django.forms.models import model_to_dict

import json

from django.http import HttpResponse

def metadata(request, address):
    response_data = {}
    try:
        account = Account.objects.get(address=address)
        metadata = model_to_dict(account)
        del metadata["id"]
        metadata['authorized'] = [t.address for t in account.authorized.all()]
        response_data = metadata
    except Account.DoesNotExist:
        response_data["result"] = "error"
        response_data["message"] = "Wallet address don't have any Mic token"
    return HttpResponse(json.dumps(response_data), content_type="application/json")