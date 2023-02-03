from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """"Allows access only to author. """

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
