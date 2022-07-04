Para realizar este ejercicio de checar el precio de cambio de diversas monedas utilice varios recursos los cuales uno de ellos fue extraido de la pagina

** https://es.acervolima.com/como-extraer-datos-web-de-google-usando-python/

Especificamente la siguiente parte

====================================================================

import requests
from bs4 import BeautifulSoup

city = input("Enter the City Name: ")
search = "Weather in {}".format(city)

url = f"https://www.google.com/search?&q={search}"

req = requests.get(url)

sor = BeautifulSoup(req.text, "html.parser")

temp = sor.find("div", class_='BNeawe').text

print(temp)

====================================================================

y buscando un poco mas haya para poder utilizar este codigo encontre en la pagina 

** https://www.activestate.com/resources/quick-reads/how-to-pip-install-requests-python-package/

donde menciona que se tiene que instalar requests, para esto se utilizam las siguentes lineas de codigo

/**  pip install requests  **/

o esta otra linea 

/**  python -m pip install requests  **/

y regresando a la primer pagina nos menciona que se tiene que instalar un modulo BeautifulSoup, el cual las lineas de codigo son las siguientes

/**  pip instalar beautifulsoup4  **/

y ya actualizando un poco las lineas de codigo asi obtenemos el resultado
