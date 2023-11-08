from django.db import models
from pictures.models import PictureField


class Pills(models.Model):
    text = models.TextField(verbose_name='Texto')
    background = models.IntegerField(default=1)
    isLottie = models.BooleanField('Lottie?', default=True)
    createDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:25] + '...'

    class Meta:
        verbose_name = 'Pílula'
        verbose_name_plural = 'Pílulas'


class Contacts(models.Model):
    name = models.CharField('Nome', max_length=150)
    address = models.CharField('Endereço', max_length=255)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.name


class Phones(models.Model):
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    number = models.CharField('Telefone', max_length=15)

    class Meta:
        verbose_name = "Número"
        verbose_name_plural = "Números"


class Information(models.Model):
    title = models.CharField('Título', max_length=255)
    text = models.TextField('Texto')
    img = PictureField('imagem', null=True, upload_to='img/', blank=True)
    themeColor = models.CharField('cor', null=True, blank=True)
    createDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Informação"
        verbose_name_plural = "Informações"

    def __str__(self):
        return self.title
