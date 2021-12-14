import json

# from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .models import Owners, Dogs
# Create your views here.

class OwnersView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        owners = Owners.objects.create(
            owner_name = data['owner_name'],
            email = data['email'],
            age = data['age']
        )

        return JsonResponse({'message' : 'created'}, status=201)



    def get(self, request):
        owners = Owners.objects.all()
        result = []

        for owner in owners:
            result.append({
                "owner_name" : owner.owner_name,
                "email" : owner.email,
                "age" : owner.age,
            })
        return JsonResponse({"result" : result}, status=200)



class DogsView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        dogs = Dogs.objects.create(
            dog_name = data['dog_name'],
            age = data['age'],
            owners = Owners.objects.get(owner_name = data['owner_name'])
        )

        return JsonResponse({'message' : 'created'}, status=201)



    def get(self, request):
        dogs = Dogs.objects.all()
        result = []

        for dog in dogs:
            result.append({
                "dog_name" : dog.dog_name,
                "age" : dog.age,
                "owners" : Owners.objects.get(id = dog.owners_id).owner_name
            })
        return JsonResponse({"result" : result}, status=200)