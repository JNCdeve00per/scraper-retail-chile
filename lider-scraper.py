# -*- coding: utf-8 -*-
import json
import requests

#
# developed by jnsdevel00per
#

head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'authority': 'buysmart-bff-production.lider.cl',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'accept': 'application/json, text/plain, */*',
    'x-flowid': 'b1e37d68-1a88-4168-9968-3b3b477ded65',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://www.lider.cl',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'referer': 'https://www.lider.cl/',
    'accept-language': 'es,en;q=0.9'
}


descuento=55
precioFalla=1000
categorias = ["Juguetería_y_entretención","Computación","Mundo_Bebé", "Tecno","Celulares","Electrohogar","Dormitorio","Muebles-","Decohogar","Deportes","Aire_libre","Automóvil-","Belleza_y_Cuidado_Personal","Climatización","Ferretería-","Librería_y_Cumpleaños","A3D"]

url = 'https://buysmart-bff-production.lider.cl/buysmart-bff/category'

for categoria in categorias:
    
    ploads = {'categories':categoria,'page':1,'facets':[],'sortBy':'','hitsPerPage':700}
    r1=requests.post(url,headers=head,json=ploads)
    data = r1.json()
    Qproductos=data["nbHits"]
    ploads2 = {'categories':categoria,'page':1,'facets':[],'sortBy':'','hitsPerPage':Qproductos}
    r1=requests.post(url,headers=head,json=ploads)
    data = r1.json()
    #print (data)
    for producto in data["products"]:
        if producto["discount"] > descuento :
            print("Producto con "+str(producto["discount"]) +"%  de descuento : "+producto["displayName"])
        if producto["price"] ["BasePriceSales"]< precioFalla :
            print("Posible oferta con "+str(producto["price"] ["BasePriceSales"]) +"  precio : "+producto["displayName"])
        
        dif=producto["price"] ["BasePriceReference"]-producto["price"] ["BasePriceSales"]
        difPercent=(dif*100)/producto["price"] ["BasePriceReference"]
        if difPercent > descuento :
            print("Producto con "+str(difPercent) +"%  de diferencia : "+producto["displayName"])
       
        
      
     

  
  
    
    
  








