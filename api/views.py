from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from django_filters import rest_framework as filters


from .models import Terminal
from .models import Acquirer
from .models import Model
from .models import Location
from .models import Status
from .models import Connectivity

from .serializers import TerminalSerializer
from .serializers import AcquirerSerializer
from .serializers import ModelSerializer
from .serializers import LocationSerializer
from .serializers import StatusSerializer
from .serializers import ConnectivitySerializer

from .filters import TerminalFilter


class APIStatus(APIView):
    """ route 'status/' """

    def get(self, request):
        return Response({'status': 'true'})


class TerminalList(generics.ListCreateAPIView):
    """ route 'terminals/' """
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = TerminalFilter


class TerminalDetail(generics.RetrieveUpdateDestroyAPIView):
    """ route 'terminals/<int:pk>/' """
    queryset = Terminal.objects.all()
    serializer_class = TerminalSerializer


class AcquirerList(generics.ListCreateAPIView):
    """ route 'acquirers/' """
    queryset = Acquirer.objects.all()
    serializer_class = AcquirerSerializer


class AcquirerDetail(generics.RetrieveUpdateDestroyAPIView):
    """ route 'acquirers/<int:pk>/' """
    queryset = Acquirer.objects.all()
    serializer_class = AcquirerSerializer


class ModelList(generics.ListCreateAPIView):
    """ route 'models/' """
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class ModelDetail(generics.RetrieveUpdateDestroyAPIView):
    """ route 'models/<int:pk>/' """
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class LocationList(generics.ListCreateAPIView):
    """ route 'locations/' """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    """ route 'locations/<int:pk>/' """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class StatusList(generics.ListCreateAPIView):
    """ route 'statuses/' """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class StatusDetail(generics.RetrieveUpdateDestroyAPIView):
    """ route 'statuses/<int:pk>/ """
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ConnectivityList(generics.ListCreateAPIView):
    """ route 'connectivities/' """
    queryset = Connectivity.objects.all()
    serializer_class = ConnectivitySerializer


class ConnectivityDetail(generics.RetrieveUpdateDestroyAPIView):
    """ route 'connectivities/<int:pk>/' """
    queryset = Connectivity.objects.all()
    serializer_class = ConnectivitySerializer
