from django.http import HttpResponseRedirect
from requests import post
from .forms import Mailing_listForm, ClientForm, MessageForm, DirectoryClient, AddMailing_listForm
from .models import Mailing_list, Client, Message
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from twilio.rest import Client
import pickle


class ClientDetailView(DetailView):
    model = Client

    def createClient(request):
        if request.method == "POST":
            client = ClientForm(request.POST)
            if client.is_valid():
                client.save()
                return HttpResponseRedirect('#')
            else:
                error = 'Форма была не верной'

        form = ClientForm
        context = {
            'form': form,
            'error': error,
        }
        return render(request, '#', context)

    def editClient(request, pk):
        contact = get_object_or_404(Client, pk=pk)
        client = ClientForm(request.POST or None, instance=post)
        if client.is_valid():
            client.save()
            return redirect('#')

        context = {
            'client': client,
            'contact': contact,
        }
        return render(request, context)

    def deleteClient(request, pk):
        contact = get_object_or_404(Client, pk=pk)
        if request.method == 'POST':
            contact.delete()
            return redirect('#')

        context = {
            'object': contact,
        }
        return render(request, context)

class Mailing_listView(ListView):

    def get_detail(request):
        import pickle
        qs = Mailing_list.objects.values_list('id_res', 'title', 'date_start', 'date_end')
        return render(request, qs)

    def object_detail(request, status):
        content = MessageForm.objects.filter(category__name__contains=status)

        context = {
            'content': content,
            'status': status,
        }
        return render(request, context)

class CreateDeleteMailing_listView(DetailView):
    model = Mailing_list

    def createMailing_list(request):
        if request.method == "POST":
            content = Mailing_listForm(request.POST)
            if content.is_valid():
                content.save()
                return HttpResponseRedirect('#')
            else:
                error = 'Форма была не верной'

        form = Mailing_listForm
        context = {
            'form': form,
            'error': error,
        }
        return render(request, '#', context)

    def deleteMailing_list(request, pk):
        Ml = get_object_or_404(Client, pk=pk)
        if request.method == 'POST':
            Ml.delete()
            return redirect('#')

        context = {
            'object': Ml,
        }
        return render(request, context)


class SendingMeiling_list(DetailView):
    model = Mailing_listForm, Client

    def send_sms(request):
        if request.method == 'POST':
            text = Mailing_listForm.objects.values_list('title')
            client = Client.objects.values_list('code' + 'tel_number')
            teg = Client.objects.values_list('teg')
            start = Mailing_listForm.objects.values_list('date_start')
            end = Mailing_listForm.objects.values_list('date_end')
            try:
                if start is not end:
                    auth_token = '...'

                    sender = Client(auth_token)

                    message = sender.messages.create(
                        body=text,
                        from_=sender,
                        to=client or teg,
                    )
                    return 'Successfully sent!'
            except Exception as ex:
                return 'Error sending', ex