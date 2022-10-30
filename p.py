import os
import timeit 
from operator import mod
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
ficheros = os.listdir("./archivos") 
for fichero in ficheros:
    print(fichero)
    lista = []
    lista1 = []
    dicc = dict()
    with open("./archivos/" + str(fichero), 'rb') as file: 
        original = file.read()
    for i in range(3):
        key = os.urandom(32)
        iv = os.urandom(16)
        tamañoOriginal = os.path.getsize("./archivos/" + str(fichero))
        x = mod(len(original), 16)
        cifrar = Cipher(algorithms.AES(key), modes.CBC(iv))
        inicio = timeit.default_timer()
        encryptor = cifrar.encryptor()
        ct = encryptor.update(original + bytes(" "*(16-x),encoding='utf-8')) + encryptor.finalize()
        final = timeit.default_timer()
        with open("./archivos/" + str(fichero), 'wb') as encrypted_file: 
            encrypted_file.write(ct)
        tamañoCifrado = os.path.getsize("./archivos/" + str(fichero))
        with open("./archivos/" + str(fichero), 'rb') as enc_file: 
            encrypted = enc_file.read()
        inicio1 = timeit.default_timer()
        decryptor = cifrar.decryptor()
        p = (decryptor.update(ct) + decryptor.finalize())[:-(16-x)]
        final1 = timeit.default_timer()
        with open("./archivos/" + str(fichero), 'wb') as dec_file: 
            dec_file.write(p) 
                        
        tiempoFinal = final - inicio
        tiempoFinal1 = final1 - inicio1
        lista.append(tiempoFinal)
        lista1.append(tiempoFinal1) 
        rest = tamañoCifrado - tamañoOriginal
    print(rest)    
    print(lista)
    print(lista1)