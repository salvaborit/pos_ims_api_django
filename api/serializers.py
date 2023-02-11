from rest_framework import serializers

from .models import Terminal
from .models import Acquirer
from .models import Model
from .models import Location
from .models import Status
from .models import Connectivity


class TerminalSerializer(serializers.ModelSerializer):
    acquirer = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Acquirer.objects.all())
    status = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Status.objects.all())
    model = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Model.objects.all())
    location = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Location.objects.all())

    class Meta:
        model = Terminal
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    connectivity = serializers.PrimaryKeyRelatedField(
        many=False, queryset=Connectivity.objects.all())

    class Meta:
        model = Model
        fields = '__all__'


class AcquirerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acquirer
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class ConnectivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Connectivity
        fields = '__all__'
