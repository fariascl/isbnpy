# isbnpy
Librería para obtener datos relacionados al número estándar internacional de libro (ISBN).
El ISBN es un código único que permite identificar los datos ásicos de un libro, tales como título, editorial, lengua original, tipo, etcétera (para más información puedes ir al [artículo en la wikipedia](https://es.wikipedia.org/wiki/ISBN)) 

Uso de librería:
Hay que aclarar que los datos son obtenidos por medio de un scraping a la página [isbnsearch.org.org](https://isbnsearch.org/), y parseados de tal manera que se entregue un JSON (o más bien un diccionario en Python) legible para ser usado en donde quieras.
Para usar correctamente esta librería, es necesario obtener la cookie que está relacionada con la verificación de recaptcha de Google
