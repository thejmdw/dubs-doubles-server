"""
   Author: Daniel Krusch
   Purpose: To convert product type data to json
   Methods: GET, POST
"""

"""View module for handling requests about product categories"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from dubsapi.models import Topping, ToppingType
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ToppingSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for product type"""
    class Meta:
        model = Topping
        url = serializers.HyperlinkedIdentityField(
            view_name='Topping',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name', 'price', 'topping_type_id')


class Toppings(ViewSet):
    """Categories for products"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized product type instance
        """
        new_topping = Topping()
        new_topping.name = request.data["name"]
        new_topping.price = request.data["price"]
        new_topping.topping_type = ToppingType.objects.get(pk=request.data["topping_type_id"])
        new_topping.save()

        serializer = ToppingSerializer(new_topping, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        """
        @api {PUT} /products/:id PUT changes to product
        @apiName UpdateProduct
        @apiGroup Product

        @apiHeader {String} Authorization Auth token
        @apiHeaderExample {String} Authorization
            Token 9ba45f09651c5b0c404f37a2d2572c026c146611

        @apiParam {id} id Product Id to update
        @apiSuccessExample {json} Success
            HTTP/1.1 204 No Content
        """
        


        topping = Topping.objects.get(pk=pk)
        topping.name = request.data["name"]
        topping.price = request.data["price"]
        topping.topping_type = ToppingType.objects.get(pk=request.data["topping_type_id"])
        topping.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single type"""
        try:
            type = Topping.objects.get(pk=pk)
            serializer = ToppingSerializer(type, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to Topping resource"""
        topping = Topping.objects.all()

        # Support filtering Toppings by area id
        # name = self.request.query_params.get('name', None)
        # if name is not None:
        #     ProductCategories = ProductCategories.filter(name=name)

        serializer = ToppingSerializer(
            topping, many=True, context={'request': request})
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        """
        @api {DELETE} /products/:id DELETE product
        @apiName DeleteProduct
        @apiGroup Product

        @apiHeader {String} Authorization Auth token
        @apiHeaderExample {String} Authorization
            Token 9ba45f09651c5b0c404f37a2d2572c026c146611

        @apiParam {id} id Product Id to delete
        @apiSuccessExample {json} Success
            HTTP/1.1 204 No Content
        """
        try:
            topping = Topping.objects.get(pk=pk)
            topping.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Topping.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
