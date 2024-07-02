from .serializers import CarSerializer, HistorySerializer
from rest_framework import viewsets, status, permissions
from rest_framework import decorators
from .models import Car, History
from rest_framework.response import Response

class CarViewSet(viewsets.ViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    def get_queryset(self):
        origin = self.request.query_params.get('origin')
        destination = self.request.query_params.get('dest')
        category = self.request.query_params.get('cat')
        required_hours = self.request.query_params.get('rh')
    
        queryset = Car.objects.filter(current_city=origin, category=category, is_available=True)
        
        return queryset
        
class HistoryViewSet(viewsets.ViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"Fail": "No car is available at the moment"}, status=status.HTTP_400_BAD_REQUEST)
        super().create(request, *args, **kwargs)
        headers = self.get_success_headers(serializer.data)
        return Response({"status": "Car Rented Successfully", "status_code": 200, "data": serializer.data, "total_payable_amt": 1000}, status=status.HTTP_200_OK, headers=headers)