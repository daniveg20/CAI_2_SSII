import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import timeit 
from operator import mod
from pathlib import Path
#1570980
tamaños_clave = [16,24,32]
clases = [(Cipher(algorithms.ChaCha20(os.urandom(32), os.urandom(16)), mode=None), "ChaCha20 "+str(32*8))]
for tamaño in tamaños_clave:
    key = os.urandom(tamaño)
    iv = os.urandom(16)
    clases.append((Cipher(algorithms.AES(key), modes.CBC(iv)), "AES "+str(tamaño*8)))
    clases.append((Cipher(algorithms.Camellia(key), modes.CBC(iv)), "Camellia "+str(tamaño*8)))

ficheros = os.listdir("./archivos") 
for fichero in ficheros:
    print(fichero)
    dicc = dict()
    with open("./archivos/" + str(fichero), 'rb') as file: 
        original = file.read()
    for cifrar,tipo in clases:
        lista = []
        lista1 = []
        for i in range(3):
            padd = padding.PKCS7(128).padder()
            unpadd = padding.PKCS7(128).unpadder()
            key = os.urandom(32)
            iv = os.urandom(16)
            tamañoOriginal = os.path.getsize("./archivos/" + str(fichero))
            print("Tamaño original: ",tamañoOriginal)
            #x = mod(len(original), 16)


            inicio = timeit.default_timer()
            encryptor = cifrar.encryptor()
            #ct = encryptor.update(original + bytes(" "*(16-x),encoding='utf-8')) + encryptor.finalize()
            original = padd.update(original)
            ct = encryptor.update((original + padd.finalize())) + encryptor.finalize()
            final = timeit.default_timer()
            with open("./archivos/" + str(fichero), 'wb') as encrypted_file: 
                encrypted_file.write(ct)
            tamañoCifrado = os.path.getsize("./archivos/" + str(fichero))
            print("Tamaño cifrado: ",tamañoCifrado)


            with open("./archivos/" + str(fichero), 'rb') as enc_file: 
                encrypted = enc_file.read()
            inicio1 = timeit.default_timer()
            decryptor = cifrar.decryptor()
            final1 = timeit.default_timer()
            #res = (decryptor.update(ct) + decryptor.finalize())[:-(16-x)]
            res = decryptor.update(ct) + decryptor.finalize()
            res = unpadd.update(res)
            with open("./archivos/" + str(fichero), 'wb') as dec_file: 
                dec_file.write((res + unpadd.finalize()))       
            

            tiempoFinal = final - inicio
            tiempoFinal1 = final1 - inicio1
            lista.append(tiempoFinal)
            lista1.append(tiempoFinal1)
        
        print("=============================")
        print("=============================")
        rest = tamañoCifrado - tamañoOriginal
        media = 0
        for i in lista:
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
    print(dicc)
