from django.db import models
from .inheritancemodels import Basemodel,Common_Productmodel
from django.utils.text import slugify


class Categaory(Basemodel):
    slug=models.SlugField(unique=True,null=True,blank=True)
    categaory_name=models.CharField(max_length=100)
    categaory_image=models.ImageField(upload_to='mycategaory',null=True,blank=True)
    
    def __str__(self):
        return self.categaory_name
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.categaory_name)
        super().save(*args,**kwargs)
        
        
class ProductType(Basemodel):
    slug=models.SlugField(unique=True,null=True,blank=True)
    Categaory=models.ForeignKey(Categaory,on_delete=models.CASCADE,related_name='P_categaory')
    product_type_name=models.CharField(max_length=100)
    product_type_image=models.ImageField(upload_to='myproduct_type',null=True,blank=True)
    
    def __str__(self):
        return '{} from {}'.format(self.product_type_name,self.Categaory)
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.product_type_name)
        super().save(*args,**kwargs)
        
        
class Product(Basemodel,Common_Productmodel):
    slug=models.SlugField(unique=True,null=True,blank=True)
    ProductType=models.ForeignKey(ProductType,on_delete=models.CASCADE,related_name='P_producttype')
    
    def __str__(self):
        return self.product_name
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.product_name)
        super().save(*args,**kwargs)
        
        
        
class Leval2_Stage2_Product(Basemodel,Common_Productmodel):
    slug=models.SlugField(unique=True,null=True,blank=True)
    Leval2_Stage1_Product=models.ForeignKey(Product,on_delete=models.CASCADE,
                                            related_name='P_Leval2_Stage1_Product')
    
    def __str__(self):
        return self.product_name
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.product_name)
        super().save(*args,**kwargs)