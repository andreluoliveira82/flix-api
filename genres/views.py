from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from core.permissions import GlobalDefaultPermission
from genres.models import Genre
from genres.serializers import GenreModelSerializer



class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer


# @csrf_exempt
# def genre_create_list_view(request):
#     """
#     se o usuario fizer um GET, enviamos para ele todos os generos de filmes cadastrados em nosso database.
#     caso ele faça um post, cadastramos o genero (novo) que ele enviar
#     """
#     if request.method == "GET":
#         genres = Genre.objects.all()
#         data = [{"id": genre.id, "name": genre.name} for genre in genres]
#         return JsonResponse(data, safe=False)

#     elif request.method == "POST":
#         data = json.loads(request.body.decode("utf-8"))
#         new_genre = Genre(name=data["name"])
#         new_genre.save()
#         return JsonResponse({"id": new_genre.id, "name": new_genre.name}, status=201)


class GenereRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer


# @csrf_exempt
# def genre_datail_view(request, pk):
#     """
#     se o usuario fizer um GET, enviamos para ele o genero de filme que
#     """
#     genre = get_object_or_404(Genre, pk=pk)

#     if request.method == "GET":
#         data = {"id": genre.id, "name": genre.name}
#         return JsonResponse(data, safe=False)

#     # caso o metodo enviado for put, atualizamos o genero
#     elif request.method == "PUT":
#         data = json.loads(request.body.decode("utf-8"))
#         genre.name = data["name"]
#         genre.save()
#         return JsonResponse(data, status=202)

#     # caso o metodo enviado for delete, deletamos o genero
#     elif request.method == "DELETE":
#         genre.delete()
#         return JsonResponse({'message':"Gênero deletado com sucesso"}, status=204)
#     return JsonResponse({}, status=405)  # 405 = Method Not Allowed
