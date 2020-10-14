import os
import pyAesCrypt 
import secrets
import socket
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)



abc = int(input("Введите PIN_CODE"))
if abc == 5040:
    print("Ваш IP",IP)
else:
        print('Неправильно введен PIN')
        exit()
abcd = 1
while abcd==1:
    n=16
    a=secrets.token_hex(n)

    choose = int(input("Расшифровать/зашифровать(1/2)"))
    if choose == 1:
        f = open("ключ.txt", "r")
        password = f.read()
        f.close()
        bufferSize = 64 * 1024
        # decrypt
        name = input("Введите имя зашифрованного файла")+".txt.aes"
        name2 = input("Введите имя итогового файла ")+".txt"
        pyAesCrypt.decryptFile(name, name2, password, bufferSize )
        
        print("Успешно!")
        print("Нажмите Ctrl+C для закрытия")
        os.remove(name)
        os.remove("ключ.txt")
    elif choose == 2:
        def crypt(dir):
            print('-----------------------------------')
            print("Ключ находится в Ключ.txt")
            my_file = open('ключ.txt', 'w')
            text_for_file = a
            my_file.write(text_for_file)
            my_file.close()
            print('-----------------------------------')
            password = a # Вводим ключ шифрования
            bufferSize = 512*1024 #Размер буфера 512 килобайт, не нужно его делать очень большим
            pyAesCrypt.encryptFile(str(dir),str(dir)+'.aes',password, bufferSize) # Собственно сама функция шифрования, создаст зашифрованный файл с расширение .aes
            print('[Crypted] '+str(dir)+'.aes')
            os.remove(dir)
    dir = input('Введите имя файла,который надо зашифровать ')+".txt" # Вводим имя файла
    crypt(dir)
    print("Успешно!")
    print("Нажмите Ctrl+C для закрытия")

