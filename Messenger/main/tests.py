from django.test import TestCase
from . models import UserInfo
from django.contrib.auth.models import User

class UserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        UserInfo.objects.create(username="Bod", first_name="Bohdan", last_name = "Holovin", job="student", age = 9, friends=" ")

    def test_first_name_label(self):
        user = UserInfo.objects.get(id=1)
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_first_name_max_length(self):
        user = UserInfo.objects.get(id=1)
        max_length = user._meta.get_field('first_name').max_length
        self.assertEquals(max_length, 100)

    def test_last_name_label(self):
        user = UserInfo.objects.get(id=1)
        field_label = user._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_last_name_max_length(self):
        user = UserInfo.objects.get(id=1)
        max_length = user._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 200)

    def test_job(self):
        user = UserInfo.objects.get(id=1)
        field_label = user._meta.get_field('job').verbose_name
        self.assertEquals(field_label, 'job')

    def test_job_max_length(self):
        user = UserInfo.objects.get(id=1)
        max_length = user._meta.get_field('job').max_length
        self.assertEquals(max_length, 200)

