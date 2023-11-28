import json
from django.db.models import Prefetch
from django.test import TestCase
from django.urls import reverse
from .models import Pills, Contacts, Information, Phones


class UrlsTest(TestCase):

    def test_index_url(self):
        url = reverse("index")
        self.assertEqual(url, "/")

    def test_pills_url(self):
        url = reverse("pills")
        self.assertEqual(url, "/api/pills/")

    def test_pill_url(self):
        url = reverse("pill", kwargs={"pk": 1})
        self.assertEqual(url, "/api/pills/1")

    def test_pills_url_response(self):
        response = self.client.get("/api/pills/")
        self.assertEqual(response.status_code, 200)

    def test_informations_url(self):
        url = reverse("informations")
        self.assertEqual(url, "/api/informations/")

    def test_informations_url_response(self):
        response = self.client.get("/api/informations/")
        self.assertEqual(response.status_code, 200)

    def test_contacts_url(self):
        url = reverse("contacts")
        self.assertEqual(url, "/api/contacts/")

    def test_contacts_url_response(self):
        response = self.client.get("/api/contacts/")
        self.assertEqual(response.status_code, 200)


class TemplatesTest(TestCase):

    def test_home_template_correct_load(self):
        response = self.client.get(reverse("index"))
        self.assertTemplateUsed(response, "index.html")

    def test_page404_template_correct_load(self):
        response = self.client.get("/nao-existe")
        self.assertTemplateUsed(response, "404.html")


class ModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Pills.objects.create(text="Primeira Pill")

        Pills.objects.create(
            text="Segunda Pill",
            background=2,
            isLottie=False
        )

        c = Contacts.objects.create(
            name="Uj",
            address="Av. Aqui",
            description="Uma descrição",
            latitude=-37.556982,
            longitude=-38.556982,
        )
        Phones.objects.create(
            contacts=c,
            number="123456",
        )
        Phones.objects.create(
            contacts=c,
            number="654321",
        )
        Information.objects.create(
            img="img/teste.jpg",
            title="Titulo",
            text="Um texto",
            themeColor=None
        )

    def test_pill_default_correct_save(self):
        pill = Pills.objects.get(pk=1)
        self.assertEqual(pill.text, "Primeira Pill")
        self.assertEqual(pill.background, 1)
        self.assertEqual(pill.isLottie, True)
        self.assertIsNotNone(pill.createDate)

    def test_pill_correct_save(self):
        pill = Pills.objects.get(pk=2)
        self.assertEqual(pill.text, "Segunda Pill")
        self.assertEqual(pill.background, 2)
        self.assertEqual(pill.isLottie, False)
        self.assertIsNotNone(pill.createDate)

    def test_contact_correct_save(self):
        contact = Contacts.objects.prefetch_related(
            Prefetch("phones_set")).first()
        numbers = list(contact.phones_set.all())
        self.assertEqual(contact.name, "Uj")
        self.assertEqual(contact.address, "Av. Aqui")
        self.assertEqual(contact.description, "Uma descrição")
        self.assertEqual(len(numbers), 2)
        self.assertEqual(numbers[0].number, "123456")
        self.assertEqual(numbers[1].number, "654321")

    def test_information_correct_save(self):
        info = Information.objects.first()
        response = self.client.get(info.img.url)
        self.assertEqual(info.title, "Titulo")
        self.assertEqual(info.img.url, "/media/img/teste.jpg")
