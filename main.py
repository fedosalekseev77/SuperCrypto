import os
import pyAesCrypt
import hashlib
import secrets
abc = int(input("Введите PIN_CODE"))
if abc == 0000:
    print("Привет")
else:
        print('Неправильно введен PIN')
        exit()

n=16
a=secrets.token_hex(n)
print("Ваш код ",a)

choose = int(input("Расшифровать/зашифровать(1/2)"))
if choose == 1:
    bufferSize = 64 * 1024
    password = input("Введите ключ")
    # decrypt
    name = input("Введите имя файла")
    name2 = input("Введите имя файла для расшифровки")
    pyAesCrypt.decryptFile(name, name2, password, bufferSize )
elif choose == 2:
    def crypt(dir):
         print('-----------------------------------')
         password = input('Введите ключ для зашифровки') # Вводим ключ шифрования
         bufferSize = 512*1024 #Размер буфера 512 килобайт, не нужно его делать очень большим
         pyAesCrypt.encryptFile(str(dir),str(dir)+'.aes',password, bufferSize) # Собственно сама функция шифрования, создаст зашифрованный файл с расширение .aes
         print('[Crypted] '+str(dir)+'.aes')
dir = input('Введите имя файла,который надо зашифровать ') # Вводим имя файла
crypt(dir)

