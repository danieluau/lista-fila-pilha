#Exercício 4.5: Fila Genérica para Biblioteca

from collections import deque

class Livro:
    def __init__(self, nome, disponibilidade=True):
        self.nome = nome
        self.disponibilidade = disponibilidade
        self.fila_espera = deque()

class Biblioteca:
    def __init__(self):
        self.livros = {}

    def cadastra_livro(self, nome):
        if nome not in self.livros:
            self.livros[nome] = Livro(nome)

    def retira_livro(self, nome):
        if nome in self.livros:
            livro = self.livros[nome]
            if livro.disponibilidade:
                livro.disponibilidade = False
                return f"livro '{nome}' retirado com sucesso."
            else:
                return f"livro '{nome}' não disponível. adicionado à fila de espera."
        else:
            return f"livro '{nome}' não encontrado."

    def devolve_livro(self, nome):
        if nome in self.livros:
            livro = self.livros[nome]
            livro.disponibilidade = True
            if livro.fila_espera:
                proximo_na_fila = livro.fila_espera.popleft()
                livro.disponibilidade = False
                return f"livro '{nome}' devolvido. '{proximo_na_fila}' retirou da fila de espera."
            else:
                return f"livro '{nome}' devolvido. não há pessoas na fila de espera."
        else:
            return f"livro '{nome}' não encontrado."

def main_biblioteca():
    biblioteca = Biblioteca()
    
    while True:
        print("\n----- menu biblioteca -----")
        print("1. cadastrar livro")
        print("2. retirar livro")
        print("3. devolver livro")
        print("4. sair")

        escolha = input("digite sua escolha (1-4): ")

        if escolha == "1":
            nome_livro = input("digite o nome do livro a cadastrar: ")
            biblioteca.cadastra_livro(nome_livro)
        elif escolha == "2":
            nome_livro_retirar = input("digite o nome do livro a retirar: ")
            print(biblioteca.retira_livro(nome_livro_retirar))
        elif escolha == "3":
            nome_livro_devolver = input("digite o nome do livro a devolver: ")
            print(biblioteca.devolve_livro(nome_livro_devolver))
        elif escolha == "4":
            print("encerrando o programa. adeus!")
            break
        else:
            print("escolha inválida. digite um número entre 1 e 4.")

if __name__ == "__main__":
    main_biblioteca()
