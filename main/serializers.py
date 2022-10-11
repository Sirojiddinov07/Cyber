from  rest_framework.serializers import ModelSerializer
from .models import *


class HeaderSerializer(ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'



class InfoSerializer(ModelSerializer):
    class Meta:
        model = Info
        fields = '__all__'



class GamesSerializer(ModelSerializer):
    class Meta:
        model = Games
        fields = '__all__'




class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'



class TurnirSerializer(ModelSerializer):
    class Meta:
        model = Turnir
        fields = '__all__'



class GalarySerializer(ModelSerializer):
    class Meta:
        model = Galery
        fields = '__all__'
