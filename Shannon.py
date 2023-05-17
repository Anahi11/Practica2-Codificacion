#Código Shannon-Fano

from collections import Counter
import statistics

archivo = input("Ingresa el nombre del archivo\n") #Ingresar el nombre del archivo

########################################################################################################################
#Hexadecimal a Binario
#El archivo originalmente se abre en hexadecimal, para obtenerlo en binario use la funcion "join" que sirve para unir
# caracteres. Consiste en colocar la separacion, y entre corchetes colocar "n" para que inicie en 0 y termine,
# en este caso, en 8 bits. Cuando "n" sea igual a los 8 bits, se abre el archivo y (rb) se lee en binario.

archivo_binarioS = "".join([f"{n:08b}" for n in open (archivo,'rb').read()])


########################################################################################################################
# Tuplas

tuplas = [] #en donde estan las tuplas
secuencia = range(0,len(archivo_binarioS),16) #secuencia de números, len() devuvelve la longitud de un objeto, salto de 16
#Realizar las tuplas de 16 bits
for b in secuencia:  #b - binario
    tuplas.append(archivo_binarioS[b:b+16].zfill(16)) #append agregar un solo elemento al final de la fila, agregar cero

#print(tuplas)

########################################################################################################################
# Obtener la probabilidad : obtener total de tuplas, frecuencia y dividir.
#Obtener el total de tuplas
Totalt= len(tuplas)
#print(Totalt)

#Obtener frecuencias, cuantas veces se repite cada una de las tuplas.
frecuencias = dict(Counter(tuplas))
#print(frecuencias)  #dict para diccionarios

#Probabilidad de cada tuplas y ordenadas en orden decreciente
Probabilidades ={simbolo : frecuencia/Totalt for simbolo, frecuencia in frecuencias.items()}
#Reverse = False para que los ordene de menor a mayor y poder realizar la suma equiprobable
Probabilidades = dict(sorted(Probabilidades.items(), key=lambda i:i[1], reverse=True))
print(Probabilidades)

########################################################################################################################
# Conjuntos que sean equiprobables
sumaProb = 0
for i in Probabilidades.values():
    sumaProb += i
print(sumaProb)

equiprobable = sumaProb/2
print(equiprobable)

lista1 = []
lista0 = []
for i in Probabilidades.values():
    suma0 = sum(lista1)+i
    if suma0 <= equiprobable:
        lista1.append(i)
    else:
        lista0.append(i)

print('Lista 1',lista1)
print('Lista 0',lista0)
