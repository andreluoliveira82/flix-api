from rest_framework import generics
from actors.models import Actor
from actors.serializers import ActormodelSerializer


class ActorCreateListView(generics.ListCreateAPIView):
    """
    Permite criar e listar atorores por meio dos metodos GET, POST

    """

    queryset = Actor.objects.all()
    serializer_class = ActormodelSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """Busca o detalhe de um actor especifico.
    permite visualizar, atualizar e deletar um actor

    """

    queryset = Actor.objects.all()
    serializer_class = ActormodelSerializer
