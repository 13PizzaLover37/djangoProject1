from django.db import models
from datetime import date
# Create your models here.


class Gender(models.Model):
    # gender
    gender = models.CharField("Gender", max_length=20)

    def __str__(self):
        return self.gender

    class Meta:
        verbose_name = "gender"
        verbose_name_plural = "gender"


class Passport(models.Model):
    # Passport's info
    number = models.CharField("Number", max_length=8)
    date_from = models.DateField("Date_from", default=date.today)
    date_to = models.DateField("Date_to", default=date.today)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = "passport"
        verbose_name_plural = "passport"


class Nationality(models.Model):
    # Nationalities
    nationality = models.CharField("Nationality", default="Null", max_length=25)

    def __str__(self):
        return self.nationality

    class Meta:
        verbose_name = "nationality"
        verbose_name_plural = "nationality"


class Languages(models.Model):
    language = models.CharField("Language", max_length=25)

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = "language"
        verbose_name_plural = "languages"

class Person(models.Model):
    # person
    name = models.CharField("Name", max_length=30)
    surname = models.CharField("Surname", max_length=30)
    birthday = models.DateField("Birthday", default=date.today)
    photo = models.ImageField("Photo", upload_to="photos/")
    gender = models.ForeignKey(Gender, verbose_name="gender", on_delete=models.CASCADE, null=True)
    passport = models.OneToOneField(Passport, on_delete=models.CASCADE, null=True, unique=True)
    nationality = models.ForeignKey(Nationality, verbose_name="nationality", on_delete=models.CASCADE, null = True)
    languages = models.ManyToManyField(Languages, verbose_name="language", related_name="languages")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "person"


