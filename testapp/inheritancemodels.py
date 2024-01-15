from django.db import models
import uuid

class Basemodel(models.Model):
    uuid=models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    date=models.DateField(auto_now_add=True)
    date2=models.DateField(auto_now=True)
    
    class Meta:
        abstract=True
        
        
class Common_Productmodel(models.Model):
    product_name=models.CharField(max_length=100,null=True,blank=True)
    product_type_image=models.ImageField(upload_to='myproduct_type',null=True,blank=True)
    product_price=models.CharField(max_length=100,null=True,blank=True)
    product_discription=models.TextField(null=True,blank=True)
    
    class Meta:
        abstract=True
        
        
