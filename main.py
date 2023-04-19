#archivo = open('texto.txt', 'a')
#archivo.write('Prueba de guardado en el archivo')
#archivo.close()

#archivo = open('texto.txt', 'r')
#print(archivo.read())

def encriptar(texto):
    print("El texto a encriptar es: "+texto)
    textoFinal = ''
    for letra in texto:
        asci = ord(letra)
        asci += 1
        textoFinal += chr(asci)
    return textoFinal
def desencriptar(texto):
    print("El texto a desencriptar es: "+texto)
    textoFinal = ''
    for letra in texto:
        asci = ord(letra)
        asci -= 1
        textoFinal += chr(asci)
    return textoFinal


#encriptar('Prueba')
#desencriptar('Pxrxuxexbxax')

def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoEncriptado)
    archivo.close()
    print("El archivo se encripto correctamente")

def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)

    archivo = open(rutaArchivo, 'w')
    archivo.write(textoDesencriptado)
    archivo.close()
    print("El archivo se desencripto correctamente")

respuestaEncriptar = input('Presione "E" para encriptar, o "D" para desencriptar')
rutaArchivo = input('Ingrese la ruta del archivo')

if respuestaEncriptar == 'E':
    encriptarArchivo(rutaArchivo)
else:
    desencriptarArchivo(rutaArchivo)


#encriptarArchivo()
#desencriptarArchivo()

#encriptarArchivo()

#archivo = open('texto.txt', 'a')
#archivo.write('Prueba de guardado en el archivo')
#archivo.close()

#archivo = open('texto.txt', 'r')
#print(archivo.read())