from rest_framework import serializers
from .models import Mailing_list, Client, Message

class Mailing_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing_list
        fields = ('title', 'date_start', 'date_end')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('tel_number', 'cod', 'teg', 'timezone')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message, Mailing_list, Client
        fields = ('id_ms', 'date_create', 'status', 'id_res', 'id_cl')
