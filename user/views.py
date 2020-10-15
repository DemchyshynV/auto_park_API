from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import UserSerializer
from .models import UserModel


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAdminUser, IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    def list(self, request, *args, **kwargs):
        qs = self.get_queryset().exclude(id=self.request.user.id)
        return Response(UserSerializer(qs, many=True).data)


