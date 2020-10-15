from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from user.serializers import UserSerializer
from user.models import UserModel


class RegisterView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
