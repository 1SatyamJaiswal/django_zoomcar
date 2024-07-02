from rest_framework import viewsets, permissions, serializers
from .serializers import UserSerializer, RegisterSerializer
from .models import User
from rest_framework import generics, status
from rest_framework.response import Response

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = RegisterSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"Fail": "Failed to create new account"}, status=status.HTTP_400_BAD_REQUEST)
        super().create(request, *args, **kwargs)
        headers = self.get_success_headers(serializer.data)
        return Response({"Success": "Account Created Successfully", "status_code": 200, "data": serializer.data}, status=status.HTTP_200_OK, headers=headers)