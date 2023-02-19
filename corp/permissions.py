from rest_framework import permissions


class CompanyEmployeesPermissions(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_staff
