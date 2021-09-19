
"""View module for handling requests about line items"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from dubsapi.models import LineItem, Order, Product, Customer




class LineItemSerializer(serializers.ModelSerializer):
    """JSON serializer for line items """
    class Meta:
        model = LineItem
        # url = serializers.HyperlinkedIdentityField(
        #     view_name='lineitem',
        #     lookup_field='id'
        # )
        fields = ('id', 'order', 'product', 'toppings')
        depth = 1

class LineItems(ViewSet):
    """Line items for dubs orders"""

    # TIP: By setting this class attribute, then a `basename` parameter
    #      does not need to be set on the route in urls.py:11 and allow
    #      the serializer (see above) use the `view_name='lineitem'`
    #      argument for the HyperlinkedIdentityField. If this is NOT set
    #      then the following exception gets thrown.
    #
    # ImproperlyConfigured at /lineitems/4
    #   Could not resolve URL for hyperlinked relationship using view name
    #   "LineItem-detail". You may have failed to include the related
    #   model in your API, or incorrectly configured the `lookup_field`
    #   attribute on this field.
    # queryset = LineItem.objects.all()
    def list(self, request):
        """Handle GET requests to Topping resource"""
        line_item = LineItem.objects.all()

        # Support filtering Toppings by area id
        # name = self.request.query_params.get('name', None)
        # if name is not None:
        #     ProductCategories = ProductCategories.filter(name=name)

        serializer = LineItemSerializer(
            line_item, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        @api {GET} /cart/:id DELETE line item from cart
        @apiName RemoveLineItem
        @apiGroup ShoppingCart

        @apiHeader {String} Authorization Auth token
        @apiHeaderExample {String} Authorization
            Token 9ba45f09651c5b0c404f37a2d2572c026c146611

        @apiParam {id} id Product Id to remove from cart
        @apiSuccessExample {json} Success
            HTTP/1.1 204 No Content
        """
        try:
            # line_item = LineItem.objects.get(pk=pk)
            customer = Customer.objects.get(user=request.auth.user)
            line_item = LineItem.objects.get(pk=pk, order__customer=customer)

            serializer = LineItemSerializer(line_item, context={'request': request})

            return Response(serializer.data)

        except LineItem.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        """
        @api {DELETE} /cart/:id DELETE line item from cart
        @apiName RemoveLineItem
        @apiGroup ShoppingCart

        @apiHeader {String} Authorization Auth token
        @apiHeaderExample {String} Authorization
            Token 9ba45f09651c5b0c404f37a2d2572c026c146611

        @apiParam {id} id Product Id to remove from cart
        @apiSuccessExample {json} Success
            HTTP/1.1 204 No Content
        """
        try:
            customer = Customer.objects.get(user=request.auth.user)
            order_product = LineItem.objects.get(pk=pk, order__customer=customer)
            order_product.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except LineItem.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

