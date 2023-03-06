from django.db import models

# Create your models here.
class Predictor(models.Model):
    id = models.AutoField(primary_key=True)
    tweet = models.CharField(max_length=200)
    is_hate_speech = models.IntegerField()
    target_hs_individu = models.IntegerField()
    target_hs_group = models.IntegerField()
    type_hs_religion = models.IntegerField()
    type_hs_ras = models.IntegerField()
    type_hs_physical = models.IntegerField()
    type_hs_gender = models.IntegerField()
    type_hs_other = models.IntegerField()
    level_hs_weak = models.IntegerField()
    level_hs_moderate = models.IntegerField()
    level_hs_strong = models.IntegerField()