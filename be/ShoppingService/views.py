from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json
from .models import CartInstances

def index(request):
    return HttpResponse('Hi! This is index page.')

def health(request):
    return HttpResponse('OK')

@csrf_exempt
def add_to_cart(request):
    try:
        data = json.loads(request.body.decode('utf-8'))
        user_id = data.get('user_id')
        item_id = data.get('item_id')
        if user_id and item_id:
            cart_instance = CartInstances(user_id=user_id, item_id=item_id)
            cart_instance.save()
            return JsonResponse({'Response': "add_to_cart() succeed"})
        else:
            return JsonResponse({'Error': 'Invalid message data'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'Error': 'Invalid JSON data'}, status=400)

@csrf_exempt
def get_cart(request):
    model_json = serializers.serialize("json", CartInstances.objects.all())
    data = {"Response": model_json}
    return JsonResponse(data)

