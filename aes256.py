import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import timeit 
from operator import mod
from pathlib import Path
#1570980
tamaños_clave = [16,24,32]
clases = []
for tamaño in tamaños_clave:
    key = os.urandom(tamaño)
    iv = os.urandom(16)
    clases.append((Cipher(algorithms.AES(key), modes.CBC(iv)), "AES"+str(tamaño*8)))
    clases.append((Cipher(algorithms.Camellia(key), modes.CBC(iv)), "Camellia"+str(tamaño*8)))

ficheros = os.listdir("./archivosImages") 
for fichero in ficheros:
    print(fichero)
    dicc = dict()
    with open("./archivosImages/" + str(fichero), 'rb') as file: 
        original = file.read()
    for cifrar,tipo in clases:
        lista = []
        lista1 = []
        for i in range(3):
            key = os.urandom(32)
            iv = os.urandom(16)
            tamañoOriginal = os.path.getsize("./archivosImages/" + str(fichero))
            x = mod(len(original), 16)
            inicio = timeit.default_timer()
            encryptor = cifrar.encryptor()
            ct = encryptor.update(original + bytes(" "*(16-x),encoding='utf-8')) + encryptor.finalize()
            final = timeit.default_timer()
            with open("./archivosImages/" + str(fichero), 'wb') as encrypted_file: 
                encrypted_file.write(ct)
            tamañoCifrado = os.path.getsize("./archivosImages/" + str(fichero))
            with open("./archivosImages/" + str(fichero), 'rb') as enc_file: 
                encrypted = enc_file.read()
"""            inicio1 = timeit.default_timer()
            decryptor = cifrar.decryptor()
            p = (decryptor.update(ct) + decryptor.finalize())[:-(16-x)]
            final1 = timeit.default_timer()
            with open("./archivosImages/" + str(fichero), 'wb') as dec_file: 
                dec_file.write(p)"""       
            
            #tiempoFinal = final - inicio
            #tiempoFinal1 = final1 - inicio1
            #lista.append(tiempoFinal)
            #lista1.append(tiempoFinal1)
        
        #rest = tamañoCifrado - tamañoOriginal
        #media = 0
"""        for i in lista:
            media += i
        x = media/len(lista)
        media1 = 0
        for i in lista1:
            media1 += i
        p = media1/len(lista)
        if tipo in dicc.keys():
            dicc[tipo] = dicc[tipo] + [(x,p,rest)]
        else:
            dicc[tipo] = [(x,p, rest)]
    print(dicc)"""