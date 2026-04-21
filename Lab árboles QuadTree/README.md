Problema
Eres parte de un equipo que desarrolla un sistema de logistica de entregas en una ciudad.
Tienes coordenadas (x,y) de 10.000 puntos de entrega (estos datos los puedes tomar de datos reales
o generarlos, para este ejercicio los datos son estaticos, es decir, no cambian).

Necesitas implementar un sistema que responda eficientemente preguntas como:
* ¿que puntos de entrega estan a un radio de 500 metros de un punto dado? (tener en cuenta unidades)
* ¿cual es el puntos de entrega mas cercano a una ubicacion dada?

Objetivo: Implementar un Arbol-Quadtree desde cero, y comparar con fuerza bruta.

Micro-tareas para resolver el ejercicio:
* Construir el arbol Quadtree (no se pueden usar arboles ya generados o librerias como scipy)
* Implementar busqueda dentro de un radio (Range Search)
* Vecinos (puntos encontrados dentro del radio) y encontrar los mas cercanos
* Verificacion visual de radio y puntos encontrados dentro del radio.
* Verificacion visual de los vecinos mas cercanos.
Notas:
* IMPORTANTE: trate de hacer el codigo para K-dimensiones, sino, puede ser solo para 2D
* No se permiten soluciones completas de internet o vibe coding, sí se pueden apoyar de IA o internet
* Se puede hacer preguntas

Responder las siguientes preguntas en el analisis comparativo:
* para que tamaño de datos el arbol-Quadtree comienza a ser mas rapido que "fuerza bruta"
(no arboles, si listas, ...)?



Contenido del documento :

sección 1 : Implementación del árbol

Presenta una breve explicacón y construcción 

sección 2 : Test

Explicación fuerza bruta y aplicación
Gráfica de buscar radio
Gráfica de vecino cercano
tiempos de comparación 1
tiempos de comparación 1

Sección 3 : Análisis , problemas y dificultades 

Se realizaron pruebas con diferentes tamaños de datos:


1.000
5.000
10.000
20.000
