from django.db import models


class Actor(models.Model):
    GENDERS = [
        ('W', 'Woman'),
        ('M', 'Man')
    ]

    name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDERS, max_length=1)

    def __str__(self):
        if self.name:
            return self.name
        return '-- It doesnt have name --'


class Country(models.Model):
    name = models.CharField(max_length=128)
    iso_code = models.IntegerField()

    def __str__(self):
        if self.name:
            return self.name
        return '-- It doesnt have name --'


class Movie(models.Model):
    title = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    year = models.CharField(max_length=4)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="movies", null=True, blank=True)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name="movies", null=True, blank=True)

    def __str__(self):
        if self.title:
            return self.title
        return '-- It doesnt have title --'


class Oscar(models.Model):
    category = models.CharField(max_length=128)
    year = models.CharField(max_length=4)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name="oscars", null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="oscars", null=True, blank=True)

    def __str__(self):
        if self.category:
            return self.category
        return '-- It doesnt have category --'


