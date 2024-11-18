from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPermission
from actors.models import Actor
from actors.serializers import ActorModelSerializer


class ActorCreateListView(generics.ListCreateAPIView):
    """
    Permite criar e listar atorores por meio dos metodos GET, POST

    """

    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Busca o detalhe de um actor especifico.
    permite visualizar, atualizar e deletar um actor

    """

    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer
