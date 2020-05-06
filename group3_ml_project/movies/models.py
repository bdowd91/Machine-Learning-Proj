from django.db import models

# Create your models here.
class movies(models.Model):
    index = models.IntegerField()
    budget = models.BigIntegerField()
    genres = models.CharField(max_length=528)
    homepage = models.CharField(max_length=528)
    id = models.IntegerField(primary_key=True)
    keywords = models.CharField(max_length=528)
    original_language = models.CharField(max_length=528)
    original_title = models.CharField(max_length=528)
    overview = models.TextField()
    popularity = models.FloatField()
    production_companies = models.TextField()
    production_countries = models.TextField()
    release_data = models.DateField()
    revenue = models.BigIntegerField()
    runtime = models.IntegerField()
    spoken_languages = models.TextField()
    status = models.CharField(max_length=528)
    tagline = models.CharField(max_length=528)
    title = models.CharField(max_length=528)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    cast = models.TextField()
    crew = models.TextField()
    director = models.CharField(max_length=528)
    time_created = models.TimeField()
    time_stamp = models.DateTimeField()


