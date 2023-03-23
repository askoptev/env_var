"""
    Модуль запускается из демона: 
    /etc/systemd/system/env_test.service

    Демон загружает переменные окружения из фала конфигурации:
    /etc/systemd/env_test.conf

    Если переменная загрузилать, то в файл env.txt 
    будет сохраняться ее значение "SUCCESSFUL"

    проверка журналов systemd
    $ sudo journalctl -f
"""
import os
import time

def main():
    loop = 1
    count = 0
    while loop == 1:
        env = os.getenv("TOKEN_API")    
        print(count, env)
        with open("env.txt", "a") as file:
            file.write(f'{count} {env}\n')
        time.sleep(1)
        count += 1
    
if __name__ == "__main__":
    main()
