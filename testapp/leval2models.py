# from django.db import models
# from .inheritancemodels import Basemodel,Common_Productmodel
# from django.utils.text import slugify
# from .models import ProductType


# class Leval2_Stage1_Product(Basemodel):
#     slug=models.SlugField(unique=True,null=True,blank=True)
#     ProductType=models.ForeignKey(ProductType,on_delete=models.CASCADE,related_name='P_producttype')
#     product_name=models.CharField(max_length=100)
#     product_image=models.ImageField(upload_to='myproduct_type')
    
#     def __str__(self):
#         return self.product_name
    
#     def save(self,*args, **kwargs):
#         self.slug=slugify(self.product_name)
#         super().save(*args,**kwargs)
        
        
# class Leval2_Stage2_Product(Basemodel,Common_Productmodel):
#     slug=models.SlugField(unique=True,null=True,blank=True)
#     Leval2_Stage1_Product=models.ForeignKey(Leval2_Stage1_Product,on_delete=models.CASCADE,
#                                             related_name='P_Leval2_Stage1_Product')
    
#     def __str__(self):
#         return self.product_type_name
    
#     def save(self,*args, **kwargs):
#         self.slug=slugify(self.product_name)
#         super().save(*args,**kwargs)