class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)
    
fila = Queue()

for i in range(1, 11):
    num = int(input("Insira o "+ str(i) + "º número da fila (" + str(11-i) + " número(s) restantes para inserir ou 0 para sair): "))
    
    if num == 0:
        break
    
    fila.enqueue(num)

for i in range(1, fila.size()+1):
    print("O " + str(i) + " inserido foi: " + str(fila.dequeue()))
    