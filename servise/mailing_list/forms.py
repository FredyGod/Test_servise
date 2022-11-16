from django.forms import ModelForm, TextInput
from .models import Mailing_list, Client, Message

class Mailing_listForm(ModelForm):
    class Meta:
        model = Mailing_list
        fields = ['id_res', 'title', 'date_start', 'date_end']

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['tel_number', 'cod', 'teg', 'timezone']
        widgets = {'tel_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона'}),
                   'teg': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите тег'}),
                   }

class MessageForm(ModelForm):
    class Meta:
        model = Message, Mailing_list, Client
        fields = ['id_ms', 'date_create', 'status', 'id_res', 'id_cl']

class DirectoryClient(ModelForm):
    class Meta:
        model = Client
        fields = ['id_cl', 'tel_number', 'cod', 'teg', 'timezone']

class AddMailing_listForm(ModelForm):
    class Meta:
        model = Mailing_list
        fields = ['id_res', 'title', 'date_start', 'date_end']
        widgets = {'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите текст сообщения'}),
                   'date_end': TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите дату завершения рассылки'}),
                   }