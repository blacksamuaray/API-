from django.db import models

class Books(models.Model):
    title=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    isbn=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.title

#model yaratilgandan keyin 1 marta makemigrations va migrate berish lozim
#Undan so'ng admin.py elon qilish kerak books degan class ni