from django.db import models

# Create your models here.
class ContactSubmission(models.Model):
    Name = models.CharField(_(""), max_length=100)
    Email = models.EmailField()
    Created_at = models.DateTimeField(auto_now_add=True)
    Message = models.TextField()
    
    def __str__ (self):
        return self.Name