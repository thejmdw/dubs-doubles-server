"""
   Author: Daniel Krusch
   Purpose: To convert product category data to json
   Methods: GET, POST
"""

"""View module for handling requests about product categories"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from dubsapi.models import ProductType
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for product category"""
    class Meta:
        model = ProductType
        url = serializers.HyperlinkedIdentityField(
            view_name='ProductType',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name')


class ProductTypes(ViewSet):
    """Categories for products"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized product category instance
        """
        new_product_category = ProductType()
        new_product_category.name = request.data["name"]
        new_product_category.save()

        serializer = ProductTypeSerializer(new_product_category, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single category"""
        try:
            category = ProductType.objects.get(pk=pk)
            serializer = ProductTypeSerializer(category, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to ProductType resource"""
        product_category = ProductType.objects.all()

        # Support filtering ProductTypes by area id
        # name = self.request.query_params.get('name', None)
        # if name is not None:
        #     ProductCategories = ProductCategories.filter(name=name)

        serializer = ProductTypeSerializer(
            product_category, many=True, context={'request': request})
        return Response(serializer.data)

