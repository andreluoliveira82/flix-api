from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):
    """
    Global permission class that checks if the user has the required permission for each method in the API.
    """

    def has_permission(self, request, view) -> bool:
        """
        Checks if the user has the required permission for the current request.
        """
        model_permission_codename = self.__get_model_permission_codename(
            method=request.method,
            view=view,
        )

        # if model_permission_codename is None, then Lock (False):
        if not model_permission_codename:
            return False

        return request.user.has_perm(model_permission_codename)

    def __get_model_permission_codename(self, method, view) -> str:
        """
        Returns the permission codename for the given method and view.
        """
        try:
            app_label = view.queryset.model._meta.app_label
            action = self.__get_action_sufix(method)
            model_name = view.queryset.model._meta.model_name
            return f"{app_label}.{action}_{model_name}"
        except Exception:
            return None

    def __get_action_sufix(self, method) -> str:
        """
        Returns the action suffix for the given method.
        """
        method_actions = {
            "GET": "view",
            "POST": "add",
            "PUT": "change",
            "PATCH": "change",
            "DELETE": "delete",
            "OPTIONS": "view",
            "HEAD": "view",
        }
        return method_actions.get(method, "")
