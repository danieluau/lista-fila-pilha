class Pilha:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

def decimal_para_binario(decimal):
    pilha = Pilha()

    while decimal > 0:
        resto = decimal % 2
        pilha.push(resto)
        decimal //= 2

    resultado = ""
    while not pilha.is_empty():
        resultado += str(pilha.pop())

    return resultado

# Leitura do número decimal
numero_decimal = int(input("Digite o número decimal: "))

# Conversão e exibição do resultado
resultado_binario = decimal_para_binario(numero_decimal)
print("O resultado em binário é:", resultado_binario)
