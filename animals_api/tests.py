from django.test import Client, TestCase
from django.urls import reverse
from rest_framework_jwt.serializers import User
from animals_api.models import Cat, Dog


class UserAPITestCase(TestCase):
    """
    User API
    """

    def setUp(self):
        self.c = Client()

        self.normal_user = User.objects.create_user(
            username="joe", password="password", email="joe@soap.com")
        self.superuser = User.objects.create_superuser(
            username="clark", password="supersecret", email="joe@soap.com")

        self.first_cat = Cat.objects.create(name='first_cat', owner=self.normal_user)
        self.second_cat = Cat.objects.create(name='second_cat', owner=self.superuser)

        self.first_dog = Dog.objects.create(name='first_dog', owner=self.normal_user)
        self.second_dog = Dog.objects.create(name='second_dog', owner=self.superuser)

        self.c.login(username="joe", password="password")

    def tearDown(self):
        for cat in Cat.objects.all():
            cat.delete()
        for user in User.objects.all():
            user.delete()
        for dog in Dog.objects.all():
            dog.delete()

        self.c.logout()

    def test_show_cat_only_owner(self):
        """GET /cats returns a list of cats"""
        url = reverse("cats-list")
        response = self.c.get(url)
        assert response.status_code == 200, \
            "Expect 200 OK. got: {}".format(response.status_code)
        num_cats = len(response.json())

        assert num_cats == 1, \
            "Expect it to return exactly 1 cat. Got: {}".format(num_cats)

    def test_show_dog_only_owner(self):
        """GET /dogs returns a list of dogs"""
        url = reverse("dogs-list")
        response = self.c.get(url)
        assert response.status_code == 200, \
            "Expect 200 OK. got: {}".format(response.status_code)
        num_cats = len(response.json())

        assert num_cats == 1, \
            "Expect it to return exactly 1 dog. Got: {}".format(num_cats)

    def test_can_create_cat_if_logget(self):
        """POST /cats/ returns 201 CREATED"""

        data = {
            "name": "cat_third"
        }
        url = reverse("cats-list")

        response = self.c.post(url, data)
        assert response.status_code == 201, \
            'Expect 201 created. Got: {}'.format(response.status_code)
        assert Cat.objects.count() == 3, \
            'Expect a new user to have been created'

    def test_can_view_not_own_cat(self):
        """GET /cats/ returns 404"""

        url = reverse("cats-detail", args=[self.second_cat.pk])

        response = self.c.get(url)
        assert response.status_code == 404, \
            'Expect 403 created. Got: {}'.format(response.status_code)
