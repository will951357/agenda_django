from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):

    class Meta:
        # Classe destinada a editar os meta dados da pagina
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    name = models.CharField(max_length=70)

    def __str__(self) -> str:
        return self.name

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 blank=True, null=True
                                 )
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 blank=True, null=True
                                 )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    

