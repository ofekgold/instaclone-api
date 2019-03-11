from rest_framework import generics, mixins

from accounts.models import Account
from .serializer import AccountSerializer

class AccountListView(generics.ListAPIView, mixins.CreateModelMixin):
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)    