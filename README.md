# Ejercicios de - Nivel Intermedio

## 1. Clase para representar un rectángulo

**Descripción:** Crea una clase `Rectangulo` con atributos `base` y `altura`, y un método `area` que calcule el área.

**Input:**
```python
r = Rectangulo(5, 3)
print(r.area())
```
**Output esperado:**

```
   15
```
## 2. Clase con método de clase y método estático
Descripción: Crea una clase Circulo con un método estático que convierta grados a radianes y un método de clase que cree un círculo con área dada.

**Input:**
```python
print(Circulo.grados_a_radianes(180))
```
**Output esperado:**
```
3.141592653589793
```
## 3. Generador de números pares
Descripción: Escribe una función generadora que devuelva los primeros n números pares.

**Input:**

```python
for n in pares(4):
    print(n)
```
**Output esperado:**

```
0
2
4
6
```
## 4. Generador de palabras de una frase
Descripción: Crea una función generadora que devuelva una palabra a la vez de una frase dada.

**Input:**

```python
for palabra in palabras('Hola mundo cruel'):
    print(palabra)
```
**Output esperado:**
```
Hola
mundo
cruel
```
## 5. Decorador para medir tiempo de ejecución
Descripción: Crea un decorador que mida y muestre el tiempo de ejecución de una función.

**Input:**

```python
@medir_tiempo
def tarea():
    import time
    time.sleep(1)

tarea()
```
**Output esperado:**

```
Tiempo de ejecución: ~1.0 segundos
```
## 6. Decorador para verificar tipos
Descripción: Crea un decorador que verifique que todos los argumentos sean enteros.

**Input:**

```python
@verificar_enteros
def suma(a, b):
    return a + b

print(suma(2, 3))
```
**Output esperado:**

```
5
```
## 7. Dockerfile para una app simple
Descripción: Crea un Dockerfile que corra una aplicación simple de que imprime "Hola desde Docker".

**Input:**

```bash
docker build -t mi_app .
docker run mi_app
```
**Output esperado:**

```
Hola desde Docker
```
## 8. Ejecutar script de dentro de Docker
Descripción: Crea un contenedor Docker que ejecute un script que lea un archivo y lo imprima.

**Input:**

```bash
docker build -t lector .
docker run lector
```
**Output esperado:**

```
Contenido del archivo...
```
## 9. Contar vocales en un string
Descripción: Escribe una función que cuente cuántas vocales tiene un string.

**Input:**

```python
print(contar_vocales('Hola mundo'))
```
**Output esperado:**

```
4
```
## 10. Invertir palabras en un string
Descripción: Crea una función que reciba una frase y devuelva las palabras en orden invertido.

**Input:**

```python
print(invertir_palabras('Hola mundo cruel'))
```
**Output esperado:**

```
cruel mundo Hola
```
## 11. Fusionar dos diccionarios
Descripción: Crea una función que combine dos diccionarios.

**Input:**


print(fusionar_diccionarios({'a': 1}, {'b': 2}))
**Output esperado:**


```
{'a': 1, 'b': 2}
```
## 12. Contar palabras únicas con un diccionario
Descripción: Escribe una función que cuente las palabras únicas de una frase.

**Input:**

```python
print(contar_palabras('hola mundo hola'))
```
**Output esperado:**

```bash
{'hola': 2, 'mundo': 1}
```
## 13. Intercambiar valores en una tupla
Descripción: Escribe una función que reciba una tupla (a, b) y devuelva (b, a).

**Input:**

```python
print(intercambiar((1, 2)))
```
**Output esperado:**

```
(2, 1)
```
## 14. Extraer elementos de una tupla
Descripción: Devuelve los elementos impares de una tupla.

**Input:**

```python
print(filtrar_impares((1, 2, 3, 4)))
```
**Output esperado:**

```
(1,3)
```
## 15. Operaciones básicas con sets
Descripción: Devuelve la unión de dos sets y la diferencia simétrica.

**Input:**

```python
a = {1, 2, 3}
b = {3, 4}
print(a | b)
print(a ^ b)
```
**Output esperado:**

```
{1, 2, 3, 4}
{1, 2, 4}
```
## 16. Eliminar duplicados de una lista usando sets
Descripción: Escribe una función que elimine los duplicados de una lista.

**Input:**

```python
print(eliminar_duplicados([1, 2, 2, 3]))
```
**Output esperado:**

```
[1, 2, 3]
```
## 17. Crear una clase Persona con str
Descripción: Implementa una clase con un método __str__ personalizado.

**Input:**

```python
p = Persona("Ana", 30)
print(p)
```
**Output esperado:**

```
Ana (30 años)
```
## 18. Generador de números primos
Descripción: Genera los primeros n números primos.

**Input:**

```python
for p in primos(5): 
  print(p)
```
**Output esperado:**

```
2
3
5
7
11
```
## 19. Decorador para registrar llamadas
Descripción: Imprime un mensaje cada vez que se llama una función decorada.

**Input:**

```python
@loggear
def saludar():
    print("Hola")

saludar()
```
**Output esperado:**
```
Llamando a saludar
Hola
```
## 20. Uso de variables de entorno con Docker
Descripción: Crea una app en Docker que imprima una variable de entorno pasada al contenedor.

**Input:**

```bash
docker run -e NOMBRE=Mundo mi_app
```
**Output esperado:**

```
Hola Mundo
```
## 21. Revertir un string sin usar [::-1]
Descripción: Escribe una función que revierta un string sin usar slicing.

**Input:**

```python
print(revertir('python'))
```
**Output esperado:**


```
nohtyp
```
## 22. Obtener claves comunes entre dos diccionarios
Descripción: Devuelve las claves comunes entre dos diccionarios.

**Input:**

```python
print(claves_comunes({'a':1, 'b':2}, {'b':3, 'c':4}))
```
**Output esperado:**


```
{'b'}
```
## 23. Verificar si una tupla está contenida en otra
Descripción: Devuelve True si una sub-tupla está dentro de otra tupla.

**Input:**

```python
print(esta_contenida((1,2,3,4), (2,3)))
```
**Output esperado:**

```
True
```
## 24. Set: verificar subconjunto
Descripción: Indica si un set es subconjunto de otro.

**Input:**

```python
print({1,2} <= {1,2,3})
```
**Output esperado:**

```
True
```
## 25. Clase que cuente instancias creadas
Descripción: Clase que mantiene un conteo de instancias con una variable de clase.

**Input:**

```python
a = Instancia()
b = Instancia()
print(Instancia.contador)
```
**Output esperado:**

```
2
```
## 26. Generador de Fibonacci
Descripción: Genera los primeros n números de Fibonacci.

**Input:**

```python
for n in fibonacci(6): print(n)
```
**Output esperado:**

```
0
1
1
2
3
5
```
## 27. Decorador para repetir ejecución
Descripción: Crea un decorador que ejecute una función n veces.

**Input:**

```python
@repetir(3)
def hola(): print("Hola")

hola()
```
**Output esperado:**
```
Hola
Hola
Hola
```
## 28. Leer y escribir archivos con Docker
Descripción: Docker que lea un archivo de entrada y escriba en un archivo de salida.

**Input:**

```bash
docker run -v $(pwd):/data mi_app
```
**Output esperado:**

```
Archivo procesado
```
## 29. Reemplazar palabras en un string
Descripción: Función que reemplace ciertas palabras por otras.

**Input:**

```python
print(reemplazar('Hola mundo', {'Hola': 'Adiós'}))
```
**Output esperado:**


Adiós mundo
## 30. Diccionario con listas como valores
Descripción: Agrega valores a un diccionario de listas.

**Input:**

```python
d = {}
agregar_valor(d, 'clave', 1)
agregar_valor(d, 'clave', 2)
print(d)
```
**Output esperado:**

```bash

{'clave': [1, 2]}
```
## 31. Crear un set a partir de una lista
Descripción: Convierte una lista en un set.
**Input:**

```python
print(lista_a_set([1, 2, 2, 3]))
```
**Output esperado:**

```
{1, 2, 3}
```
## 32. Crear un diccionario a partir de dos listas
Descripción: Crea un diccionario a partir de dos listas.
**Input:**

```python
print(listas_a_diccionario(['a', 'b'], [1, 2]))
```
**Output esperado:**

```
{'a': 1, 'b': 2}
```
## 33. Crear un set a partir de un string
Descripción: Convierte un string en un set de caracteres únicos.
**Input:**

```python
print(string_a_set('python'))
```
**Output esperado:**

```
{'p', 'y', 't', 'h', 'o', 'n'}
```

## 34. Crear un diccionario a partir de un string
Descripción: Crea un diccionario que cuente la frecuencia de cada carácter en un string.
**Input:**

```python
print(string_a_diccionario('python'))
```
**Output esperado:**

```
{'p': 0, 'y': 1, 't': 2, 'h': 3, 'o': 4, 'n': 5}
```

## 35. Crear un set a partir de un diccionario
Descripción: Convierte un diccionario en un set de claves.
**Input:**

```python
print(diccionario_a_set({'a': 1, 'b': 2}))
```
**Output esperado:**

```
{'a', 'b'}
```

