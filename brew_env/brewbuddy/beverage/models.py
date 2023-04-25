from django.db import models


class HomebrewBatch(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField(blank=True)
    rack_date = models.DateField(blank=True)
    bottle_date = models.DateField(blank=True)
    original_gravity = models.FloatField(blank=True)
    final_gravity = models.FloatField(blank=True)
    abv = models.FloatField(blank=True)
    notes = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        # Calculate the ABV if both original and final gravity are provided
        if self.original_gravity and self.final_gravity:
            self.abv = round((self.original_gravity - self.final_gravity) * 131.25, 2)
        else:
            self.abv = None
        super(HomebrewBatch, self).save(*args, **kwargs)
        
    class Meta:
       ordering = ('name',)

    def __str__(self) -> str:
        return self.name

class TastingNote(models.Model):
    batch = models.ForeignKey(HomebrewBatch, on_delete=models.CASCADE)
    date = models.DateField()
    notes = models.TextField()
    rating = models.FloatField()