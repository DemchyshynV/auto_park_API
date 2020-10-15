from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializer import CarSerializer


class CarCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        serializer = CarSerializer(data={'user_id': self.request.user.id, **self.request.data})
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'ok'})
