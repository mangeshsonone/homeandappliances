# from django.db import models
# from .inheritancemodels import Basemodel,Common_Productmodel
# from django.utils.text import slugify
# from .models import ProductType


# class Product(Basemodel,Common_Productmodel):
#     slug=models.SlugField(unique=True,null=True,blank=True)
#     ProductType=models.ForeignKey(ProductType,on_delete=models.CASCADE,related_name='P_producttype')
    
#     def __str__(self):
#         return self.product_name
    
#     def save(self,*args, **kwargs):
#         self.slug=slugify(self.product_name)
#         super().save(*args,**kwargs)