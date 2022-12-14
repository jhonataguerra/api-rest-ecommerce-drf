from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from apps.users.models import User
from apps.users.api.serializers import UserSerializer


@api_view(["GET", "POST"])
def user_api_view(request):
    def get(request):
        if request.method == "GET":
            users = User.objects.all()
            users_serializers = UserSerializer(users, many=True)
            return Response(users_serializers.data, status=status.HTTP_200_OK)

        elif request.method == "POST":
            users_serializer = UserSerializer(data=request.data)
            if users_serializer.is_valid():
                users_serializer.save()
                return Response(users_serializer.data, status=status.HTTP_201_CREATED)
            return Response(users_serializer.errors)


@api_view(["GET", "PUT", "DELETE"])
def user_detail_api_view(request, pk=None):
    #   QuerySet
    user = User.objects.filter(id=pk).first()

    # Validação e métodos
    if user:

        if request.method == "GET":
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

        elif request.method == "PUT":
            request.data

            user_serializer = UserSerializer(user, data=request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == "DELETE":
            user.delete()
            return Response(
                {"message": "Deletado com sucesso."}, status=status.HTTP_200_OK
            )
    return Response(
        {"message": "Não foi possível localizar um usuário com estes dados."},
        status=status.HTTP_400_BAD_REQUEST,
    )
