from django.db import models

class Paper(models.Model):
  paper_id = models.CharField(max_length=30)
  title = models.CharField(max_length=100)
  abstract = models.CharField(max_length=600)
  year = models.CharField(max_length=4)
  authors = models.CharField(max_length=150)
  rank = models.FloatField()

  def __str__(self):
    return (self.paper_id+' '+self.title)

class Word(models.Model):
  word = models.CharField(max_length=16)
  origin = models.ForeignKey(Paper, on_delete=models.CASCADE)

  def __str__(self):
    return (self.word +' -> '+ str(self.origin))
