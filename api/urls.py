from django.urls import path

from .views import APIStatus
from .views import TerminalList, TerminalDetail
from .views import AcquirerList, AcquirerDetail
from .views import ModelList, ModelDetail
from .views import LocationList, LocationDetail
from .views import StatusList, StatusDetail
from .views import ConnectivityList, ConnectivityDetail


urlpatterns = [
    path('status/', APIStatus.as_view()),

    path('terminals/', TerminalList.as_view()),
    path('terminals/<int:pk>/', TerminalDetail.as_view()),

    path('acquirers/', AcquirerList.as_view()),
    path('acquirers/<int:pk>/', AcquirerDetail.as_view()),

    path('models/', ModelList.as_view()),
    path('models/<int:pk>/', ModelDetail.as_view()),

    path('locations/', LocationList.as_view()),
    path('locations/<int:pk>/', LocationDetail.as_view()),

    path('statuses/', StatusList.as_view()),
    path('statuses/<int:pk>/', StatusDetail.as_view()),

    path('connectivities/', ConnectivityList.as_view()),
    path('connectivities/<int:pk>/', ConnectivityDetail.as_view()),
]
