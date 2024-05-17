#This will be what will send the data to mailbox
# Exemplo de BackEnd da nossa arquitetura
# Esse programa pode ser desrito em um 
# loop de 3 ações
# 1) Escrever no arquivo
# 2) Aguardar a tela marcar que leu 
# 3) Volta à primeira etapa
import json
from random import randint

# Mailer: a ideia é que ele é o "mensageiro" que entrega as mensagens
# para a bridge, e ele segue um protocolo simples
# 1° Linha é um 0 ou 1, que significa respectivamente Lido / Não Lido
# 2° Linha é um ID que representa o n° da mensagem enviada, sequencialmente 1, depois 2, depois 3 ...
# 3° e as posteriores são o conteudo em JSON
# Exemplo de arquivo:
# 0
# 100
# {
#    "atributo1": "valor1",
#    "atributo2": 2
# }
class Sender:
    def __init__(self):
        self.currentId = 0
    
    def save(self, obj):
        while True:
            with open('../mailbox','r+', encoding='utf-8' ) as file:
                if file.read(1) == '0':
                    file.close()
                    continue
                file.seek(0)
                file.write(f"0\n{self.currentId}\n{json.dumps(obj)}\n")
                self.currentId = self.currentId + 1
                file.close()
                break

if __name__ == '__main__':
    data = {
        "a":1
    }
    mailer = Sender()
    while True:
        a = randint(0,100)
        data['a'] = a
        mailer.save(data)
