from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=200)

class HomebrewBatch(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='brew_images', blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient)
    start_date = models.DateField()
    rack_date = models.DateField()
    bottle_date = models.DateField()
    original_gravity = models.FloatField()
    final_gravity = models.FloatField()
    abv = models.FloatField()
    notes = models.TextField()

    class Meta:
       ordering = ('name',)

    def __str__(self) -> str:
        return self.name

class TastingNote(models.Model):
    batch = models.ForeignKey(HomebrewBatch, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField()
    rating = models.FloatField()