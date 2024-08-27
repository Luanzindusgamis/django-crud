from django.db import models

# Create your models here.
class Produto(models.Model):
    descricao= models.CharField(max_length=50,null=False)
    preco= models.CharField(max_length=10,null=False)
    quantidade= models.CharField(max_length=100,null=False)

    def __str__ (self):
        return self.descricao
    
    