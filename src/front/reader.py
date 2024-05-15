# Utilitário para acompanhar em tempo real
# a mudança do texto de um arquivo
import os
import time

clear = ""
if os.name == "posix":
    clear = 'clear'
if os.name == "nt":
    clear = 'cls'

# Fica lendo o arquivo em loop, quando ele mudar, limpa a tela e exibe o arquivo
last_content = ''
while True:
    with open('../bridge.txt','r') as file:
        content =file.read(-1)
        if content != last_content:
            os.system(clear)
            print(content)
            last_content = content
