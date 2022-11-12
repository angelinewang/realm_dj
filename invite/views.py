from django.shortcuts import render

# Create your views here.

class InvitesList(generics.ListAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer
