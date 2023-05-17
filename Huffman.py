#Código Huffman
import huffman_clase

archivo = input("Ingresa el nombre del archivo\n") #Ingresar el nombre del archivo

########################################################################################################################
#Hexadecimal a Binario
#El archivo originalmente se abre en hexadecimal, para obtenerlo en binario use la funcion "join" que sirve para unir
# caracteres. Consiste en colocar la separacion, y entre corchetes colocar "n" para que inicie en 0 y termine,
# en este caso, en 8 bits. Cuando "n" sea igual a los 8 bits, se abre el archivo y (rb) se lee en binario.

archivo_binario = "".join([f"{n:08b}" for n in open (archivo,'rb').read()])

########################################################################################################################
# Tuplas

tuplas = [] #en donde estan las tuplas
secuencia = range(0,len(archivo_binario),16) #secuencia de números, len() devuvelve la longitud de un objeto, salto de 16
#Realizar las tuplas de 16 bits
for b in secuencia:  #b - binario
    tuplas.append(archivo_binario[b:b+16].zfill(16)) #append agregar un solo elemento al final de la fila, agregar cero

########################################################################################################################
# Codificar y guardar
bits, raiz = huffman_clase.codificar(tuplas)
#print(bits)

# bits a bytes archivo .hff
bytes = huffman_clase.ConvBytes(bits)
#guardar el archivo en un archivo.hff
archivo_huff = open("huffman.hff",'wb')
archivo_huff.write( bytes )
archivo_huff.close()


########################################################################################################################
#Decodificar y obtener el archivo
#bytes a bits
bitNuevos = "".join([f"{n:08b}" for n in open("huffman.hff", "rb").read()])

decodificar = huffman_clase.decodificar(bitNuevos, raiz)

# bits a Hexadecimal
baB = huffman_clase.ConvBytes(decodificar)

#Descomprimido
archivo_des = open("huffman_des.jpg",'wb') #Cambiar la extension del archivo al archivo que ingreso
archivo_des.write( baB  )
archivo_des.close()

