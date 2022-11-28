from rest_framework.views import APIView, Response
from apps.users.models import User
from apps.users.api.serializers import UserSerializer


class UserAPIView(APIView):
    def get(self, request):
        users = User.objects.all()
        users_serializers = UserSerializer(users, many=True)
        return Response(users_serializers.data)
