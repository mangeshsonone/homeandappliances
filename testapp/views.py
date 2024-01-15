from django.shortcuts import render
from .models import *

def index(request):
   
    Cat=Categaory.objects.all()
    # pro=ProductType.objects.select_related().filter(Categaory=Cat[0])
    for i in Cat:
        print(i.slug)
    
    
    return render(request,'index.html',{'obj':Cat})
# 
 # d={}
    # for i in range(4):
    #     d[i]=i
    # d.update(d)
    # d=[1,2,3,4]
    # e=[1,5,3,8]
    # context={'obj':d,'obj2':e} 
    
def protype(request):
    slug=request.GET.get('slug')
    print(request)
    print(slug)
    abj=ProductType.objects.select_related().filter(Categaory__slug=slug) 
    print(abj)
    return render(request,'protype.html',{'obj':abj})

def product(request):
    slug=request.GET.get('slug')
    bbj=Product.objects.select_related().filter(ProductType__slug=slug)
    cbj=Leval2_Stage2_Product.objects.select_related()
    # bj=Product.objects.prefetch_related('P_Leval2_Stage1_Product')
    
    dbj=Leval2_Stage2_Product.objects.all()
    k=[]
    # for i in dbj:
    #     k.append(i.Leval2_Stage1_Product)
    l=[i.Leval2_Stage1_Product for i in cbj]
    # print(l)
    # print(k)
    
    return render(request,'secondfinal.html',{'obj':bbj,'rbj':l})

def productsec(request):
    slug=request.GET.get('slug')
    cbj=Leval2_Stage2_Product.objects.select_related().filter(Leval2_Stage1_Product__slug=slug)
    return render(request,'productsec.html',{'obj':cbj})