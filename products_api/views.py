from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, permissions
import json
from timeit import default_timer as timer


from .serializers import ProductSerializer

from products.models import Product

# Create your views here.

# class ListProductsAPIView(ListAPIView):
#     serializer_class = ProductSerializer
#     def get_queryset(self):
#         selected_products = self.request.session.get('selected_products', [])
#         return Product.objects.filter(slug__in=selected_products)
#
# list_products = ListProductsAPIView.as_view()

@api_view(['GET'])
def list_products(request):
    selected_products = request.session.get('selected_products', {})
    print(selected_products)
    # db_results = Product.objects.filter(slug__in=selected_products.keys())

    product_list = []
    for product_slug, quantity in selected_products.items():
        start = timer()
        result = Product.objects.get(slug=product_slug)
        end = timer()
        print(end - start)
        serializer = ProductSerializer(result)

        data = serializer.data
        data['quantity'] = quantity
        product_list.append(data)

    return Response(product_list)


@api_view(['POST'])
def add_product(request, slug):
    """
    the structure for the session's 'selected_products'-key value is:
    {slug for product1: how many of the product,
     slug for product2: how many of the product}

    :param request:
    :param slug: the slug of the selected product to be added to the list
    :return: json Response with
    {
        "status": "<state>",
        "selected_product": <the selected product>
    }
    """

    print(slug)
    # 1. check for the slug in the database
    try:
        selected_product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:  # if the slug (product) isn't in the database
        return Response({
            'status': 'Bad Request',
            'selected_product': None,
        }, status=400)

    # 2. adding the product to the session's "selected_products"
    selected_products = request.session.get('selected_products', {})
    if slug in selected_products:
        selected_products[slug] += 1  # if the product already existed, 1 will be added
    else:
        selected_products[slug] = 1  # if not, new product will be added

    request.session['selected_products'] = selected_products


    data = ProductSerializer(selected_product).data
    data['quantity'] = selected_products[slug]
    return Response({
        'status': 'success',
        'selected_product': data,
    })


@api_view(['DELETE'])
def remove_product(request, slug):
    """
    the structure for the session's 'selected_products'-key value is:
    {slug for product1: how many of the product,
     slug for product2: how many of the product}

    Response: json Response with
    {
        "status": "<state>",
        "selected_product": <the selected product>
    }
    """

    # check if the slug exists in the session's "selected_products"
    try:
        selected_product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:  # if the slug (product) isn't in the database
        return Response({
            'status': 'Bad Request',
            'selected_product': None,
        }, status=400)

    selected_products = request.session.get('selected_products', {})
    if slug in selected_products:
        if selected_products[slug] > 1:
            selected_products[slug] -= 1
        else:
            del selected_products[slug]
    else:
        return Response({
            'status': 'Bad Request',
            'selected_product': None,
        }, status=400)

    request.session['selected_products'] = selected_products

    quantity = selected_products.get(slug, 0)
    if quantity > 0:
        data = ProductSerializer(selected_product).data
        data['quantity'] = quantity
    else:
        data = None
    # if the product deleted, data will equal to None
    return Response({
        'status': 'success',
        'selected_product': data,
    })
