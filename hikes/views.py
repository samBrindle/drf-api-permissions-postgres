from rest_framework import generics
from.models import Hike
from .permissions import IsOwnerOrReadOnly
from .serializers import HikeSerializer


# Create your views here.
class HikeList(generics.ListCreateAPIView):
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer


class HikeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Hike.objects.all()
    serializer_class = HikeSerializer
