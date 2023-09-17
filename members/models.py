from django.db import models

# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  photo = models.ImageField(upload_to='member_photos/', null=True, blank=True)  # Add this line
  text = models.CharField(max_length=200)
  date_added = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f"{self.firstname} {self.lastname}" 

class Entry(models.Model):
  """Something specific learned about a topic."""
  topic = models.ForeignKey(Member, on_delete=models.CASCADE)
  text = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)
 
  class Meta:
    verbose_name_plural = 'entries'
  
  def __str__(self):
        """Return a string representation of the model.""" 
        return f" {self.text[:50]}..." 



class Pupil(models.Model):
    name = models.CharField(max_length=100)
    score_1 = models.IntegerField()
    score_2 = models.IntegerField()
    score_3 = models.IntegerField()
    score_4 = models.IntegerField()