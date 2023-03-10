# isbnpy
Librería para obtener datos relacionados al número estándar internacional de libro (ISBN).
El ISBN es un código único que permite identificar los datos ásicos de un libro, tales como título, editorial, lengua original, tipo, etcétera (para más información puedes ir al [artículo en la wikipedia](https://es.wikipedia.org/wiki/ISBN)) 

## Importante
Hay que aclarar que los datos son obtenidos por medio de un scraping a la página [isbnsearch.org](https://isbnsearch.org/), y parseados de tal manera que se entregue un JSON (o más bien un diccionario en Python) legible para ser usado en donde quieras.

## Uso
Para usar correctamente esta librería, es necesario obtener la cookie (de [isbnsearch.org](https://isbnsearch.org)), ya que está relacionada con la verificación de recaptcha de Google, y esto suele dificultar la obtención de datos ya que al realizar multiples consultas, obliga a resolver el captcha.

``` python
from isbnpy import ISBNpy
cookie = 'PHPSESSID=cv5826t3tiu7q1tnsa2fenXXX' # cookie de ejemplo
isbn = '978841245546'
libro = ISBNpy(cookie)
data = libro.get(isbn)
print(data)
'''
puede entregar 3 resultados:
(1) 200: {'title': 'Mil novecientos ochenta y cuatro', 'isbn_13': '9788412455465', 'isbn_10': '8412455460', 'author': 'Orwell, George', 'edition': '1', 'binding': 'Paperback', 'publisher': 'Hermida Editores S.L.', 'published': '2022', 'status_code': 200}
(2) 200: {'msg': 'cookie expired', 'status_code': 403}
(3) 404: {'msg': 'isbn not found', 'status_code': 404}

'''
```
### Tipo de resultados
- Si el resultado que entrega es el (1), quiere decir que la consulta fue realizada con éxito.
- Si el resultado que entrega es el (2), quiere decir que la cookie expiró y para volver habilitarla es necesario recurrir al sitio web [isbnsearch.org](https://isbnsearch.org), realizar una consulta en el campo de búsqueda, verificar que no eres robot y listo.
- Si el resultado que entrega es el (3), quiere decir que el ISBN no existe en la base de datos

