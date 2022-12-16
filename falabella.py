import requests
import lxml.html as lh
from bs4 import BeautifulSoup
from selenium import webdriver
import sys, os
import warnings

import locale




warnings.filterwarnings("ignore")  
url=["https://www.falabella.com/falabella-cl/category/cat7090035/Linea-blanca?page=",
     "https://www.falabella.com/falabella-cl/category/cat7170003/Calefaccion?page="
     "https://www.falabella.com/falabella-cl/category/cat40052/Computadores?page=",
     "https://www.falabella.com/falabella-cl/category/cat2005/Audio?page=",
     "https://www.falabella.com/falabella-cl/category/cat1320008/Moda-Hombre?page=",
     #"https://www.falabella.com/falabella-cl/category/cat16610015/Living---Sala-de-Estar?page=",
     #"https://www.falabella.com/falabella-cl/category/cat2046/Oficina-y-escritorio?page=",
     #"https://www.falabella.com/falabella-cl/category/cat2021/Muebles-de-comedor?page=",
     "https://www.falabella.com/falabella-cl/collection/outlet-ver-todo-electro?page=",
     "https://www.falabella.com/falabella-cl/collection/ofertas-hombre-v2?page=",
     "https://www.falabella.com/falabella-cl/category/cat2038/Fotografia?page=",
     "https://www.falabella.com/falabella-cl/category/cat2036/Fitness?page=",
     "https://www.falabella.com/falabella-cl/category/cat6930003/Ropa-deportiva-hombre?page=",
     "https://www.falabella.com/falabella-cl/category/cat6930168/Ropa-deportiva-mujer?page=",
     "https://www.falabella.com/falabella-cl/category/cat6050003/Accesorios-Hombre?page=",
     "https://www.falabella.com/falabella-cl/category/cat7190093/Smart-Home?page=",
     "https://www.falabella.com/falabella-cl/collection/ofertas-accesorios-v2?page=",
     "https://www.falabella.com/falabella-cl/category/cat1012/TV-y-Video?page=",
     "https://www.falabella.com/falabella-cl/category/cat2018/Celulares-y-Telefonos?page="]

head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
    'authority': 'www.falabella.com',
    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json, text/plain, */*',
    'origin': 'www.falabella.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'referer': 'www.falabella.com',
    'accept-language': 'es,en;q=0.9'
}

descuento=60
print("Criterio sobre % "+str(descuento))
for ur in url:
    i = 1
    s = requests.Session()
    r1=s.get(ur+str(1))
    soup = BeautifulSoup(r1.text,"lxml")
    columns = soup.findAll('button', attrs = {'class' : 'pagination-button-mkp'})[-1]
    pagMaxint=int(columns.text)
    while i <= pagMaxint: 
        
        driver = webdriver.PhantomJS()
        driver.set_window_size(10, 10)
        driver.get(ur+str(i))
        containers = driver.find_elements_by_xpath('//div[@class="jsx-4001457643 search-results-4-grid grid-pod"]')
     
     

   
        for items in containers:
            try:
                 
                var =items.text
                precioGrupo  = var.partition('$')
                precio      = precioGrupo[2]
                arrayPrecio  = precio.partition('\n')
                precioString = arrayPrecio[0]
                precioString = precioString.lstrip(" ").replace(".","")
                precioOriginalv1=arrayPrecio[2].partition('\n')
                precioOriginalv1=precioOriginalv1[2].partition('\n')
                precioOriginalv1=precioOriginalv1[2].partition('\n')
                precioOriginalv2=precioOriginalv1[0].replace(".","").replace("$","").replace(" ","")
                precioOriginalv3=int((precioOriginalv2))
                
                
                precioInt=int((precioString))
                dif=precioOriginalv3-precioInt
                difPercent=(dif*100)/precioOriginalv3
                
                if precioInt <3000:
                    print("==============================")
                    print("posible oferta")
                    print(var)
                    
                if difPercent > descuento:
                            print("___________________________")
                            print(items.text)
                            numero=0
            except Exception as ex:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                #print(exc_type, fname, exc_tb.tb_lineno)
                pass
            
        containers2 = driver.find_elements_by_xpath('//div[@class="jsx-4001457643 search-results-4-grid grid-pod"]')

        for items2 in containers2:
            try:
               
            
                var =items2.text
                precioGrupo = var.partition('$')
                precio= precioGrupo[2]
                arrayPrecio=  precio.partition('\n')
                
                precioString=arrayPrecio[0]
                precioString = precioString.lstrip(" ").replace('$','').replace('.','')

                precioOriginalv1=arrayPrecio[2].partition('\n')
                precioOriginalv2=precioOriginalv1[0].replace(".","").replace("$","").replace(" ","")
                precioOriginalv3=int((precioOriginalv2))
                
                
                precioInt=int((precioString))
                dif=precioOriginalv3-precioInt
                difPercent=(dif*100)/precioOriginalv3     
                
                precioInt=int(precioString)
                if precioInt <3000:
                    print("==============================")
                    print("posible oferta")
                    print(var)
                if difPercent > descuento:
                            print("___________________________")
                            print(items2.text)
                            numero=0  
            except Exception as ex:
      
                pass
        i=i+1
        driver.close()
   

    
    


   