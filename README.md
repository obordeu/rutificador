# rutificador
Busca nombres en la pagina https://chile.rutificador.com/ y devuelve el RUT y nombre según Padrón

Si el nombre tiene más de un hit en rutificador, los ordena por distancia al nombre y elige el más cercano.

Facilmente escalable a muchos requests por segundo, en caso de alcanzar el MAX, intenta de nuevo despues de 5 segundos.


# Uso
Guardar Rutificador.py en la carpeta de tu proyecto
```python
from Rutificador import getRUT

data={
	'nombre': 'GARY MEDEL SOTO'
	}

rut=getRUT(data)

print rut
```
Entrega:

```python

{'nombre': 'GARY MEDEL SOTO', 'rutificador': 16795344, 'nombreRutificador': u'MEDEL SOTO GARY ALEXIS'}


```