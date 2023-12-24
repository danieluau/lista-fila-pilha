class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacidade

    def push(self, item):
        if not self.is_full():
            self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def top(self):
        if not self.is_empty():
            return self.items[-1]

# Exemplo de uso
pilha = Pilha(capacidade=5)
pilha.push(1)
pilha.push(2)
pilha.push(3)
print("topo da pilha:", pilha.top())
pilha.pop()
print("topo da pilha após pop:", pilha.top())

