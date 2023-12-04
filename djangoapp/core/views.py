from rest_framework.decorators import api_view
from rest_framework.views import Response
from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from rest_framework.status import HTTP_404_NOT_FOUND
from .forms import ContactForm
from .mail import Email
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']
            mail = Email(nome=nome, mail=email, mensagem=mensagem)
            if mail.enviar():
                messages.success(
                    request, "Mensagem enviada com sucesso", extra_tags='alert alert-success')
            else:
                messages.error(request, "Erro ao enviar a mensagem",
                               extra_tags='alert alert-danger')
            url_destino = '/#contact'
            return redirect(url_destino)

    else:
        return render(request, "index.html")


@api_view(http_method_names=['GET'])
def PillsView(request):
    pills = Pills.objects.all()
    serializer = PillsSerializer(instance=pills, many=True)
    json = {
        "count": len(pills),
        "pills": serializer.data
    }

    return Response(json)


@api_view(http_method_names=['GET'])
def PillView(request, pk):
    pill = Pills.objects.filter(id=pk).first()

    if pill:
        serializer = PillsSerializer(instance=pill)
        return Response(serializer.data)

    else:
        return Response({
            'pill not foud'
        }, status=HTTP_404_NOT_FOUND)


@api_view(http_method_names=['GET'])
def ContactsView(request):
    contacts = Contacts.objects.all()
    serializer = ContactsSerializer(contacts, many=True)
    return Response(serializer.data)


@api_view(http_method_names=['GET'])
def InformationsView(request):
    informations = Information.objects.all()
    serializer = InformationsSerializer(informations, many=True)
    return Response(serializer.data)


def error_404(request, exception):
    return render(request, '404.html', status=404)
