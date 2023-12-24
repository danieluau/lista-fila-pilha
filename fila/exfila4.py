from typing import Union

class Fila:
    def __init__(self):
        self.items = []

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def enqueue(self, item: Union[int, str]):
        self.items.append(item)

    def dequeue(self) -> Union[int, str, None]:
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def front(self) -> Union[int, str, None]:
        if not self.is_empty():
            return self.items[0]
        return None

# Exemplo de uso
fila = Fila()
fila.enqueue(5)
fila.enqueue("hello")
fila.enqueue(3)
print("frente da fila:", fila.front())

while not fila.is_empty():
    print("desenfileirando:", fila.dequeue())
