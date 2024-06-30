from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import ItemSerializer, OrderSerializer
from .models import Item, Order
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated  # Invoke Token Authentication - expect a token in the header
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin

# Create your views here.


class ItemViewSet(
        ListModelMixin,  # Show all
        RetrieveModelMixin,  # Get request for a single item
        viewsets.GenericViewSet  # Provide the build in methods to retrieve, list, create, update for models
        ):
    """
    A simple ViewSet for listing or retrieving items.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class OrderViewSet(
        ListModelMixin,
        RetrieveModelMixin,
        UpdateModelMixin,
        viewsets.GenericViewSet
        ):
    """
    A simple ViewSet for listing, retrieving and creating orders.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer

    def get_queryset(self):
        """
        This view should return a list of all the orders
        for the currently authenticated user.
        """
        user = self.request.user
        return Order.objects.filter(user=user)

    def create(self, request):
        try:
            data = JSONParser().parse(request)
            serializer = OrderSerializer(data=data)
            if serializer.is_valid(raise_exception=True):  # Will check the stock
                item = Item.objects.get(pk=data["item"])
                order = item.place_order(request.user, data["quantity"])  # Create the order in the DB
                return Response(OrderSerializer(order).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error", "message": "Json decoding error"}, status=400)
