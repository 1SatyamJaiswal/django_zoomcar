from rest_framework import serializers
from .models import Car, History
from rest_framework import status
from rest_framework.response import Response

# History Serializer to Maintain the history of the cars rented
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        name = History
        fields = ['origin', 'destination', 'amount', 'hours_requirement']

# Car Serializer to maintain the information about the cars
class CarSerializer(serializers.ModelSerializer):
    rent_history = HistorySerializer(many=True)
    
    class Meta:
        name = Car
        fields = ['car_id', 'category', 'model', 'number_plate', 'current_city', 'rent_per_hr', 'rent_history']
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"Fail": "Failed to add the new car"}, status=status.HTTP_400_BAD_REQUEST)
        super().create(request, *args, **kwargs)
        headers = self.get_success_headers(serializer.data)
        return Response({"status": "Car Added Successfully", "status_code": 200, "data": serializer.data, "total_payable_amt": 1000}, status=status.HTTP_200_OK, headers=headers)
        