from calendario import models
from rest_framework import viewsets, serializers
from planocontas.models import  Planocontasreferencial, PlanocontasPlanocontasreferencial, Planocontasitem
from planocontas import serializers

# Create your views here.
class PlanocontasreferencialViewSet(viewsets.ModelViewSet):
    queryset = Planocontasreferencial.objects.all()
    serializer_class = serializers.PlanocontasreferencialSerializer

class PlanocontasPlanocontasreferencialViewSet(viewsets.ModelViewSet):
    queryset = PlanocontasPlanocontasreferencial.objects.all()
    serializer_class = serializers.PlanocontasPlanocontasreferencialSerializer

class PlanocontasitemViewSet(viewsets.ModelViewSet):
    queryset = Planocontasitem.objects.all()
    serializer_class = serializers.PlanocontasitemSerializer