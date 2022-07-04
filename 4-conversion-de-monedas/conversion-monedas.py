#En una casa de cambio necesitan construir un programa tal que al dar como dato una cantidad expresada en dolares, covierta esa cantidad en pesos

import requests 
from bs4 import BeautifulSoup 
   
dinero = input("Ingresa la moneda o la cantidad de dinero con la moneda de origen a la que quieres convertir a pesos mexicanos: ") 
search = "{} a pesos mexicanos".format(dinero) 

url = f"https://www.google.com/search?&q={search}" 
   
req = requests.get(url) 
  
sor = BeautifulSoup(req.text, "html.parser")  

temp = sor.find("div", class_='BNeawe').text 
  
print(temp) 
