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
from dubsapi.models import ToppingType
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ToppingTypeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for product type"""
    class Meta:
        model = ToppingType
        url = serializers.HyperlinkedIdentityField(
            view_name='ToppingType',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name')


class ToppingTypes(ViewSet):
    """Categories for products"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized product type instance
        """
        new_topping_type = ToppingType()
        new_topping_type.name = request.data["name"]
        new_topping_type.save()

        serializer = ToppingTypeSerializer(new_topping_type, context={'request': request})

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
        


        topping_type = ToppingType.objects.get(pk=pk)
        topping_type.name = request.data["name"]
        topping_type.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single type"""
        try:
            type = ToppingType.objects.get(pk=pk)
            serializer = ToppingTypeSerializer(type, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to ToppingType resource"""
        topping_type = ToppingType.objects.all()

        # Support filtering ToppingTypes by area id
        # name = self.request.query_params.get('name', None)
        # if name is not None:
        #     ProductCategories = ProductCategories.filter(name=name)

        serializer = ToppingTypeSerializer(
            topping_type, many=True, context={'request': request})
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
            topping_type = ToppingType.objects.get(pk=pk)
            topping_type.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except ToppingType.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
