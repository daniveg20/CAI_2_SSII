from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import timeit 
from operator import mod

def apertura():
    ficheros = os.listdir("./archivos") 
    for fichero in ficheros:
        fp = open("./archivos/" + fichero, "rb")
        buffer = fp.read()
    return buffer
lista = []
lista1 = []    
for i in range(3):   
    key = os.urandom(32)
    nonce = os.urandom(16)
    algorithm = algorithms.ChaCha20(key, nonce)
    cipher = Cipher(algorithm, mode=None)
    x = mod(len(apertura()), 16)
    inicio = timeit.default_timer()
    encryptor = cipher.encryptor()
    ct = encryptor.update(apertura() + bytes(" "*(16-x),encoding='utf-8'))
    final = timeit.default_timer()
    inicio1 = timeit.default_timer()
    decryptor = cipher.decryptor()
    final1 = timeit.default_timer()
    decryptor.update(ct)
    tiempoFinal = final - inicio
    tiempoFinal1 = final1 - inicio1
    lista.append(tiempoFinal)
    lista1.append(tiempoFinal1)
    
print(lista)
print(lista1)
media = 0
for i in lista:
    media += i
print(media/len(lista))

media1 = 0
for i in lista1:
    media1 += i
print(media1/len(lista1)) 

