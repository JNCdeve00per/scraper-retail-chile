import time
import sys, os
import warnings
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager





#
# developed by jnsdevel00per
#



url=["https://www.easy.cl/tienda/categoria/calefaccion-electrohogar?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/refrigeracion-electrohogar?cur_page=80&cur_view=grid&cur_pos=24",
     "https://www.easy.cl/tienda/categoria/cocina-electrohogar-?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/lavado-planchado-electrohogar?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/aspirado-y-limpieza-electrohogar?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/electrodomesticos-electrohogar?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/calefont-y-termos-electrohogar?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/ventilacion-electrohogar?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/muebles-de-living-y-sala-de-estar?cur_pos=24&cur_page=90&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/muebles-de-comedor-y-cocina?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/muebles-de-oficina?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/muebles-de-dormitorio-?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/muebles-para-ninos?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/muebles-funcionales-?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/muebles-de-bano-?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/ofertas-imperdibles-muebles?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/mueble-de-terraza?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/jardin?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/parrillas-y-accesorios?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/piscinas?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/camping?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/deportes-12?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/juegos-01?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/camas-0?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/colchones?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/box-spring?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/camas-americanas?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/camas?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/camas-funcionales?cur_pos=24&cur_page=80&cur_view=grid"
     "https://www.easy.cl/tienda/categoria/ropa-de-cama?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/dormitorio-infantil?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/muebles-de-dormitorio?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/Combos-dormitorio?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/marcas?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/ofertas-dormitorio-?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/cortinas?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/alfombras?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/menaje-cocina?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/menaje-comedor-3?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/decoracion-hogar--?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/decoracion-bano-?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/iluminacion?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/papeles-murales-y-guardas?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/muebles-comedor-bar?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/mueble-cocina?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/griferia-cocina?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/cocina-electrohogar-?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/cocina-comedor-electrodomesticos?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/cocina-comedor-calefont-termos?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/cocina-comedor-refrigeracion?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/organizacion-cocina-3?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/organizacion-loggia-?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/menaje-cocina?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/menaje-comedor-3?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/limpieza-aseo-?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/sanitarios?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/vanitorios-lavamanos?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/cabinas-duchas?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/tinas-hidromasajes-spa?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/organizacion-de-bano-0?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/toallas-cortinas-pisos-bano?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/calefones-y-termos--5?cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/griferia-de-bano?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/seguridad-movilidad-reducida?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/extractores-de-ba%C3%B1o?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/Destapadores?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/mascotas-gatos?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/mascotas-perro?cur_pos=24&cur_page=80&cur_view=grids",
     "https://www.easy.cl/tienda/categoria/cerraduras?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/aleros?cur_page=80&cur_view=grid&cur_pos=8",
     "https://www.easy.cl/tienda/categoria/marcos-molduras-y-otros?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/soluciones-techo?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/ventanas--?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/puertas-de-interior?cur_pos=52&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/puertas-de-exterior-0?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/mallas-listeles?cur_page=80&cur_view=grid&cur_pos=24",
     "https://www.easy.cl/tienda/categoria/mallas-listeles?cur_page=80&cur_view=grid&cur_pos=24",
     "https://www.easy.cl/tienda/categoria/fragues-adhesivos?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/pasto-sintetico-y-alfombras?cur_page=80&cur_view=grid&cur_pos=20",
     "https://www.easy.cl/tienda/categoria/piso-vinilicos?cur_page=80&cur_view=grid&cur_pos=24",
     "https://www.easy.cl/tienda/categoria/piso-flotantes?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/porcelanatos?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/ceramicas?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/herramientas-y-accesorios--?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/papel-mural-decorativo?cur_pos=&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/herramientas-suministros-pintura?cur_pos=72&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/barnices-tratamiento-superficies?cur_pos=52&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/adhesivos-selladores-siliconas?cur_pos=52&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/texturas-pastas?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/pinturas-spray?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/pinturas-especialidad?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/esmalte-sintetico-oleos?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/pintura-latex?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/accesorios-de-herramientas-electricas?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/herramientas-de-jardin?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/herramientas-manuales?cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/herramientas-manuales-alba%C3%B1ileria-y-construccion?cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/herramientas-estacionarias--5?cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/herramientas-electricas?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/electricidad?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/seguridad-para-el-hogar?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/seguridad-industrial?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/gasfiteria?cur_pos=80&cur_page=3&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/fijaciones?cur_pos=36&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/quincalleria?cur_pos=24&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/maderas-y-tableros-?cur_pos=52&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/fierros-mallas-y-alambres-1?cur_pos=40&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/perfiles-?cur_pos=108&cur_page=8&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/cemento-morteros-y-aditivos-?cur_pos=48&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/tabiqueria-1?cur_pos=40&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/techumbre?cur_pos=52&cur_page=80&cur_view=grid",
     "https://www.easy.cl/tienda/categoria/seguridad-bano-y-movilidad-reducida?cur_pos=24&cur_page=80&cur_view=grid"

     

       
     ]

for ur in url:
  

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_window_size(10, 10)
    driver.get(ur)
    containers = driver.find_elements_by_xpath('//div[@class="product"]')
    descuento=55
 
    for items in containers:
        try:
         
            var=items.text
    
            pattern = "..%"
      
            substring = re.search(pattern, var).group()
       
            substring=substring.replace('-', '')
            substring=substring.replace('%', '')
            produInt=int(substring)
        

  
            if produInt > descuento:
                print("####################################")
                print("aplica descuento  " +items.text)
                
                
        except Exception as ex:
            pass
    
    driver.close()
        
        
            
    