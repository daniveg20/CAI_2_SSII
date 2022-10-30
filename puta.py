from Crypto.Cipher import AES
from PIL import Image
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad



'''
La implementación puede ser una aplicación de escritorio, web o movil, debe contar con una interfaz gráfica que permita escoger 
o	Cifrado
o	Descifrado
o	ECB
o	CBC
o	CFB
o	OFB
'''


def bytesToImagen (bytesData, ruta, modo, tupla):
    #CREAMOS UNA NUEVA IMANGE CON MODO RGB, EL TAMAÑO Y LOS BYTES
    img = Image.frombytes("RGB", tupla, bytesData)
    #MOSTRAMOS LA IMAGEN
    #img.show()
    #SI ENCUENTRA LA SUBCADENA "eCBC u otra" entonces agrega al archivo "d" mas el modo
    if ((ruta.find("eCBC") or ruta.find("eECB") or ruta.find("eCFB") or ruta.find("eOFB")) > -1 ):
        print ("encontro")
        nombreArchivo = ruta.replace(".bmp", "_d"+modo+".bmp")
        img.save(nombreArchivo)
    #EN CASO DE QUE NO ENCUENTRE, ENTONCES LO AGREGARA
    elif (ruta=="Imagen1.bmp"):
        img.save("Imagen1_e" + modo + ".bmp")
    elif (ruta == "Imagen2.bmp"):
        img.save("Imagen2_e"+modo+".bmp")
def imagenToBytes(ruta):
    #PASAMOS A BYTES NUESTRA IMAGEN
    img = Image.open(ruta, mode="r")
    array_img = img.tobytes()
    return array_img

def imagenTamaño (ruta):
    img = Image.open(ruta, mode="r")
    return img.size

def cifradoAES_ECB (llave, ruta):
    #PASAMOS LA LLAVE A BYTES
    llave_b = bytes(llave, "utf-8")
    #CREAMOS UNA NUEVA INSTANCIA DE AES EN MODO ECB
    cifradoECB = AES.new(llave_b, AES.MODE_ECB)
    #LLAMAMOS AL ARRAY DE BYTES
    bytesIMG = imagenToBytes(ruta)
   #DCIFRAMOS NUESTRO ARRAY CON EL LLLAVE
    bytesCifrado  = cifradoECB.encrypt(pad(bytesIMG, AES.block_size))

    #MANDAMOS A CREAR UNA NUEVA IMAGEN CON LOS BYTES Y TAMAÑOS YA LOGRADOS
    bytesToImagen(bytesCifrado, ruta, "ECB", imagenTamaño(ruta))

def cifradoAES_CBC  (llave, ruta, iv):
    llave_b = bytes(llave, "utf-8")
    #A DIFERENCIA DEL ANTERIOR, AQUI PASAMOS A BYTES NUESTRO ARRAY DE INICIALIZACION.
    iv_b = bytes(iv, "utf-8")
    cifradoCBC = AES.new(llave_b, AES.MODE_CBC, iv_b)
    bytesBase = imagenToBytes(ruta)
    byteCifrados = cifradoCBC.encrypt(pad(bytesBase, AES.block_size))
    bytesToImagen(byteCifrados, ruta, "CBC", imagenTamaño(ruta))

def cifradoAES_CFB(llave, ruta, iv):
    llave_b = bytes(llave, "utf-8")
    iv_b = bytes(iv, "utf-8")
    cifradoCBC = AES.new(llave_b, AES.MODE_CFB, iv_b)
    bytesBase = imagenToBytes(ruta)
    byteCifrados = cifradoCBC.encrypt(pad(bytesBase, AES.block_size))
    bytesToImagen(byteCifrados, ruta, "CFB", imagenTamaño(ruta))

def cifradoAES_OFB(llave, ruta, iv):
    llave_b = bytes(llave, "utf-8")
    iv_b = bytes(iv, "utf-8")
    cifradoCBC = AES.new(llave_b, AES.MODE_CFB, iv_b)
    bytesBase = imagenToBytes(ruta)
    byteCifrados = cifradoCBC.encrypt(pad(bytesBase, AES.block_size))
    bytesToImagen(byteCifrados, ruta, "OFB", imagenTamaño(ruta))

def descifradoAES_ECB(llave, ruta):
    llave_b = bytes(llave, "utf-8")
    cifradoECB = AES.new(llave_b, AES.MODE_ECB)
    bytesIMG = imagenToBytes(ruta)
    print (len(bytesIMG))
    bytesDescifrados = cifradoECB.decrypt(pad(bytesIMG,  AES.block_size))
    #bytesDescifrados = cifradoECB.decrypt(pad(bytesIMG, ))
    bytesToImagen(bytesDescifrados, ruta, "ECB", imagenTamaño(ruta))

def descifradoAES_CBC(llave, ruta, iv):
    llave_b = bytes(llave, "utf-8")
    iv_b = bytes(iv, "utf-8")
    cifradoCBC = AES.new(llave_b, AES.MODE_CBC, iv_b)
    bytesBase = imagenToBytes(ruta)
    byteCifrados = cifradoCBC.decrypt(pad(bytesBase, AES.block_size))
    bytesToImagen(byteCifrados, ruta, "CBC", imagenTamaño(ruta))

def descifradoAES_CFB(llave, ruta, iv):
    llave_b = bytes(llave, "utf-8")
    iv_b = bytes(iv, "utf-8")
    cifradoCBC = AES.new(llave_b, AES.MODE_CFB, iv_b)
    bytesBase = imagenToBytes(ruta)
    byteCifrados = cifradoCBC.decrypt(pad(bytesBase, AES.block_size))
    bytesToImagen(byteCifrados, ruta, "CFB", imagenTamaño(ruta))

def descifradoAES_OFB(llave, ruta, iv):
    llave_b = bytes(llave, "utf-8")
    iv_b = bytes(iv, "utf-8")
    cifradoCBC = AES.new(llave_b, AES.MODE_OFB, iv_b)
    bytesBase = imagenToBytes(ruta)
    byteCifrados = cifradoCBC.decrypt(pad(bytesBase, AES.block_size))
    bytesToImagen(byteCifrados, ruta, "OFB", imagenTamaño(ruta))

'''
La implementación puede ser una aplicación de escritorio, web o movil, debe contar con una interfaz gráfica que permita escoger 
o	Cifrado
o	Descifrado
o	ECB
o	CBC
o	CFB
o	OFB
'''

llave =   "1234567890123456"
vector =  "ABCDEFGASDASDASD"
cifradoAES_ECB(llave, "Imagen1.bmp")
cifradoAES_CBC(llave, "Imagen1.bmp", vector)
cifradoAES_CFB(llave, "Imagen1.bmp", vector)
cifradoAES_OFB(llave, "Imagen1.bmp", vector)

cifradoAES_ECB(llave, "Imagen2.bmp")
cifradoAES_CBC(llave, "Imagen2.bmp", vector)
cifradoAES_CFB(llave, "Imagen2.bmp", vector)
cifradoAES_OFB(llave, "Imagen2.bmp", vector)