from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db import transaction
# Create your views here.
class AddAddress(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        
        user_address = models.Address.objects.create(
            userId = request.user,
            lat = data['lat'],
            lng = data['lng'],
            isDefault = data['isDefault'],
            address = data['address'],
            phone = data['phone'],
            addressType = data['addressType']
        )

        if user_address.isDefault == True:
            models.Address.objects.filter(userId=request.user).update(isDefault=False)
        
        user_address.save()

        return Response(status=status.HTTP_201_CREATED)
    
class GetUserAddresses(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        addresses = models.Address.objects.filter(userId=request.user)
        serializer = serializers.AddressSerializer(addresses, many = True)

        return Response(serializer.data)

class GetDefaultAddress(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        addresses = models.Address.objects.filter(userId= request.user, isDefault = True)

        if addresses.exists():
            address = addresses.first()
            serializer = serializers.AddressSerializer(address)
            return Response(serializer.data)
        else:
            return Response({'message': 'No default address found'})

class DeleteAdress(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        address_id = request.query_params.get('id')


        if not address_id:
            return Response({'message': 'No id provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = request.user

            address_item = models.Address.objects.get(id=address_id, userId=user)

            with transaction.atomic():
                if address_item.isDefault:
                    other_address = models.Address.objects.filter(userId=user).exclude(id=address_id)
                    
                    if other_address.exists():
                        new_default_address = other_address.first()
                        new_default_address.isDefault = True;
                        new_default_address.save();
                    else:

                        return Response({'message': 'You can not delete a default address without any othe address '}, status=status.HTTP_400_BAD_REQUEST)

                address_item.delete();

                return Response({'message': 'Deleted successfully'}, status=status.HTTP_200_OK)
                
        except models.Address.DoesNotExist:
            return Response({'message': 'Address does not exist'},  status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class SetDefaultAddress(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        address_id = request.query_params.get('id')

        if not address_id:
            return Response({'message': 'No id provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = request.user
            address = models.Address.objects.get(id=address_id)

            models.Address.objects.filter(userId=user).update(isDefault=False);
        
            address.isDefault = True;
            address.save();
        
            return Response(status=status.HTTP_200_OK)

        except models.Address.DoesNotExist:
            return Response({'message': 'Address does not exist'}, status=status.HTTP_404_NOT_FOUND )