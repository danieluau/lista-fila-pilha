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

    def top(self):
        if not self.is_empty():
            return self.items[-1]

def editor_de_texto():
    texto = Pilha()

    while True:
        comando = input("digite um comando (# para voltar para o estado anterior, @ para apagar tudo, ou um caractere para adicionar): ")

        if comando == '#':
            texto.pop()
        elif comando == '@':
            texto.items = []
        else:
            texto.push(comando)

        print("texto atual:", "".join(reversed(texto.items)))

        continuar = input("deseja continuar? (S/N): ").upper()
        if continuar != 'S':
            break

editor_de_texto()
