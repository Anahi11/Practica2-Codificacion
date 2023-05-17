from collections import Counter
from heapq import heapify, heappop, heappush

#Crear la clase arbol, en donde estaran los simbolos y se realizara la codificacion y la decodificacion
class Arbol:
    #Cear los objetos en donde se almacenara el caracter y su frecuencia; se iniciliza izquierda y derecha para
    # asignarle posteriormete 0 o 1
    def __init__(self, caracter, frecuencia, izquierda=None, derecha=None):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = izquierda
        self.derecha = derecha

    def __lt__(self, other):
        return self.frecuencia < other.frecuencia

#Se construye el arbol, recibe "archivo". Cuenta los caracteres y despues los ordena del menor al mayor, en donde el menor
#es la raiz.
def construirarbol(archivo):
    counter = Counter(archivo)
    fila = [Arbol(caracter, counter[caracter]) for caracter in counter]
    heapify(fila)
    while len(fila) > 1:
        izquierda= heappop(fila)
        derecha =heappop(fila)
        Padre = Arbol(None, izquierda.frecuencia+derecha.frecuencia, izquierda, derecha)
        heappush(fila, Padre)
    return heappop(fila)

#Para construir el mapa de codificacion, se usa dfs que sirve para buscar profundamente por cada rama .
#Crea el diccionario mapa_codificacion en donde se almacena cada uno de los codigos nuevos para los caracteres, se le agrega 0 o 1
def construirmap(raiz):
    def dfs(raiz, codigo, mapa_codificacion):
        if raiz.caracter:
            mapa_codificacion[raiz.caracter] = ''.join(codigo)
        else:
            codigo.append('0')
            dfs(raiz.izquierda, codigo, mapa_codificacion)
            codigo.pop()
            codigo.append('1')
            dfs(raiz.derecha, codigo, mapa_codificacion)
            codigo.pop()
    mapa_codificacion = {}
    dfs(raiz, [], mapa_codificacion)
    return mapa_codificacion


#Para la codificacion usa las tuplas, y las funciones anteriores para poder comprimir el archivo.
def codificar(tuplas):
    raiz = construirarbol(tuplas)
    mapa_codificacion = construirmap(raiz)
    return ''.join([mapa_codificacion[caracter] for caracter in tuplas]),raiz

#Para la decodificacion lo que hace es recorrer el arbol de la codificacion y enocntrar el carcater al que pertenecen los bits.
def decodificar(codificar, raiz):
    if raiz.caracter:
        return raiz.ch * len(codificar)
    decodificar = []
    nodo = raiz
    for bit in codificar:
        if bit == "0":
            nodo = nodo.izquierda
        else:
            nodo = nodo.derecha
        if nodo.caracter:
            decodificar.append(nodo.caracter)
            nodo = raiz
    return ''.join(decodificar)

#Convierte de bits a bytes para poder obtener el .hff
def ConvBytes(bits):
    byte = bytearray()
    for i in range(0,len(bits),8):
        byte.append(int(bits[i:i+8],2))
    return bytes(byte)

