from rest_framework import permissions

# codigo para aprendizado de como funciona o sistema de permissões do Django Rest Framework para cada model e cada metodo de request
# não vou utilizar este codigo, pois vamos usar a classe GlobalDefaultPermission (core.permissions.py) para definir as permissões para todos e qualquer model


class GenrePermissionClass(permissions.BasePermission):
    """
    Custom permission to check if user has permission to view or edit genre.
    """

    def has_permission(self, request, view) -> bool:
        """
        for each method in view, check if user has permission to view, create, edit or delete genre.
        """

        # safe methods
        if request.method in [
            "GET",
            "HEAD",
            "POST",
        ]:
            return (request.user.has_perm("genres.view_genre"),)

        # POST method (can add new genre)
        if request.method == "POST":
            return request.user.has_perm("genres.add_genre")

        # PUT/PATCH methods (can edit existing genre)
        if request.method in ["PUT", "PATCH"]:
            return request.user.has_perm("genres.change_genre")

        # DELETE method (can delete existing genre)
        if request.method == "DELETE":
            return request.user.has_perm("genres.delete_genre")

        # default return False
        return False
