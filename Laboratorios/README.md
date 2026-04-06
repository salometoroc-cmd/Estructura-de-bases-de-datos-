Laboratorios 
Problema 1

Dado un hash encontrar la secuencia de numeros que lo generan .

reglas :

hash-> sha256

la secuencia de numeros son 10 enteros concatenados cada uno en un rango [0,9]

la solcuion empleada consiste en aplicar fuerza bruta .

se recorren un rango de numeros desde 0 hasta cuando se obtengan 10 digistos, generando cada posible combinacion de 10 digitos.

se convierte a string, se completan ceros para asegurara de que tenga 10 digitos , se calcula el hash SHA256 y se compara con el ingerado por el usuario 



Problema 2

Dado el Hash root del arbol de mertel determinar el orden de las transacciones que se generan.

reglas las transacciones son conocidas y el numero de transacciones
