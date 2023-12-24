class no:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class listasimplesmenteencadeada:
    def __init__(self):
        self.inicio = None

    # Inserção no início da lista
    def inserir_no_inicio(self, dado):
        novo_no = no(dado)
        novo_no.proximo = self.inicio
        self.inicio = novo_no

    # Inserção após um valor específico
    def inserir_apos_valor(self, valor, dado):
        novo_no = no(dado)
        atual = self.inicio

        while atual:
            if atual.dado == valor:
                novo_no.proximo = atual.proximo
                atual.proximo = novo_no
                return
            atual = atual.proximo

        print(f"valor {valor} não encontrado na lista.")

    # Remoção do último elemento
    def remover_ultimo(self):
        if not self.inicio or not self.inicio.proximo:
            # Se a lista estiver vazia ou contiver apenas um elemento
            self.inicio = None
        else:
            atual = self.inicio
            while atual.proximo.proximo:
                atual = atual.proximo
            atual.proximo = None

    # Remoção por valor
    def remover_por_valor(self, valor):
        if not self.inicio:
            print("lista vazia.")
            return

        if self.inicio.dado == valor:
            self.inicio = self.inicio.proximo
            return

        atual = self.inicio
        while atual.proximo:
            if atual.proximo.dado == valor:
                atual.proximo = atual.proximo.proximo
                return
            atual = atual.proximo

        print(f"valor {valor} não encontrado na lista.")

    # Função para imprimir a lista
    def imprimir_lista(self):
        atual = self.inicio
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("none")

# Exemplo de uso
if __name__ == "__main__":
    lista_encadeada = listasimplesmenteencadeada()

    while True:
        print("1. inserir elemento no início")
        print("2. inserir após valor")
        print("3. remover último elemento")
        print("4. remover por valor")
        print("5. imprimir lista")
        print("6. sair")

        escolha = input("digite a sua escolha (1-6): ")

        if escolha == "1":
            elemento = input("digite o elemento que você deseja inserir no início: ")
            lista_encadeada.inserir_no_inicio(elemento)
        elif escolha == "2":
            valor = input("digite o valor após o qual deseja inserir: ")
            elemento = input("digite o elemento que você deseja inserir: ")
            lista_encadeada.inserir_apos_valor(valor, elemento)
        elif escolha == "3":
            lista_encadeada.remover_ultimo()
        elif escolha == "4":
            valor = input("digite o valor que deseja remover: ")
            lista_encadeada.remover_por_valor(valor)
        elif escolha == "5":
            lista_encadeada.imprimir_lista()
        elif escolha == "6":
            print("encerrando o programa. adeus!")
            break
        else:
            print("escolha inválida. por favor, digite um número entre 1 e 6.")
