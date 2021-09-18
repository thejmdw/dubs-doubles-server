# """View module for handling requests about products"""
# from django.core.exceptions import ValidationError
# from rest_framework import status
# from django.http import HttpResponseServerError
# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# from rest_framework import serializers
# from dubsapi.models import Product, Image
# from django.contrib.auth.models import User
# import uuid
# import base64
# from django.core.files.base import ContentFile


# class ImageView(ViewSet):
#     """Level up products"""

#     def create(self, request):
#         """Handle POST operations

#         Returns:
#             Response -- JSON serialized product instance
#         """

#         # Uses the token passed in the `Authorization` header
#         # productr = productr.objects.get(user=request.auth.user)

#         # Create a new Python instance of the product class
#         # and set its properties from what was sent in the
#         # body of the request from the client.
#         image = Image()

#         image.product = Product.objects.get(pk=request.data["productId"])
#         # image.user = request.auth.user

#         format, imgstr = request.data["image"].split(';base64,')
#         ext = format.split('/')[-1]
#         data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["productId"]}-{uuid.uuid4()}.{ext}')
#         image.image = data
#         # product.description = request.data["description"]
#         # product.designer = request.data["designer"]
#         # product.number_of_player = request.data["numberOfPlayers"]
#         # product.release_year = request.data["releaseYear"]
#         # product.product_duration = request.data["productDuration"]
#         # product.age_range = request.data["ageRange"]
#         # product.categories = request.data["categories"]

#         # Use the Django ORM to get the record from the database
#         # whose `id` is what the client passed as the
#         # `productTypeId` in the body of the request.
#         # product_type = productType.objects.get(pk=request.data["productTypeId"])
#         # product.product_type = product_type

#         # Try to save the new product to the database, then
#         # serialize the product instance as JSON, and send the
#         # JSON as a response to the client request
#         try:
#             image.save()
#             #  product.categories.set(request.data["categories"])
#             #  product.categories.add(request.data["categories"])
#             serializer = ImageSerializer(image, context={'request': request})
#             return Response(serializer.data)

#         # If anything went wrong, catch the exception and
#         # send a response with a 400 status code to tell the
#         # client that something was wrong with its request data
#         except ValidationError as ex:
#             return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



#     def retrieve(self, request, pk=None):
#         """Handle GET requests for single product

#         Returns:
#             Response -- JSON serialized product instance
#         """
#         try:
#             # `pk` is a parameter to this function, and
#             # Django parses it from the URL route parameter
#             #   http://localhost:8000/products/2
#             #
#             # The `2` at the end of the route becomes `pk`
#             image = Image.objects.get(pk=pk)
#             serializer = ImageSerializer(image, context={'request': request})
#             return Response(serializer.data)
#         except Exception as ex:
#             return HttpResponseServerError(ex)

#     def update(self, request, pk=None):
#         """Handle PUT requests for a product

#         Returns:
#             Response -- Empty body with 204 status code
#         """
#         # productr = productr.objects.get(user=request.auth.user)

#         # Do mostly the same thing as POST, but instead of
#         # creating a new instance of product, get the product record
#         # from the database whose primary key is `pk`
#         image = Image.objects.get(pk=pk)
        
#         image.product = Product.objects.get(pk=request.data["productId"])
#         # image.user = request.auth.user
#         image.image = request.data["image"]
#         # product = product.objects.get(pk=pk)
#         # product.title = request.data["title"]
#         # product.description = request.data["description"]
#         # product.designer = request.data["designer"]
#         # product.number_of_player = request.data["numberOfPlayers"]
#         # product.release_year = request.data["releaseYear"]
#         # product.product_duration = request.data["productDuration"]
#         # product.age_range = request.data["ageRange"]
#         # product.categories = request.data["categories"]

#         # product_type = productType.objects.get(pk=request.data["productTypeId"])
#         # product.product_type = product_type
#         image.save()

#         # 204 status code means everything worked but the
#         # server is not sending back any data in the response
#         return Response({}, status=status.HTTP_204_NO_CONTENT)

#     def destroy(self, request, pk=None):
#         """Handle DELETE requests for a single product

#         Returns:
#             Response -- 200, 404, or 500 status code
#         """
#         try:
#             image = Image.objects.get(pk=pk)
#             image.delete()

#             return Response({}, status=status.HTTP_204_NO_CONTENT)

#         except Image.DoesNotExist as ex:
#             return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

#         except Exception as ex:
#             return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#     def list(self, request):
#         """Handle GET requests to products resource

#         Returns:
#             Response -- JSON serialized list of products
#         """
#         # Get all product records from the database
#         images = Image.objects.all()

#         # Support filtering products by type
#         #    http://localhost:8000/products?type=1
#         #
#         # That URL will retrieve all tabletop products
#         product = self.request.query_params.get('Product', None)
#         if product is not None:
#             images = images.filter(product__id=product)

#         serializer = ImageSerializer(
#             images, many=True, context={'request': request})
#         return Response(serializer.data)

# # class UserSerializer(serializers.ModelSerializer):
# #     """JSON serializer for productr's related Django user"""
# #     class Meta:
# #         model = User
# #         fields = ('id', 'first_name', 'last_name', 'username' )

# class ProductSerializer(serializers.ModelSerializer):
#     """JSON serializer for products

#     Arguments:
#         serializer type
#     """
#     class Meta:
#         model = Product
#         fields = ( 'id', 'name', )
#         depth = 1

# class ImageSerializer(serializers.ModelSerializer):
#     """JSON serializer for products

#     Arguments:
#         serializer type
#     """
#     # user = UserSerializer(many=False)
#     product = ProductSerializer(many=False)

#     class Meta:
#         model = Image
#         fields = ( 'id', 'product', 'image' )
#         depth = 1