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
    
Fila = Queue() #Instancia a variável fila como um objeto Queue
Fila.enqueue(1) #Insere o número 1 como primeira variável na fila
Fila.enqueue(2) #Insere o número 2 como segunda variável na fila
Fila.enqueue(3) #Insere o número 3 como terceira variável na fila
Fila.enqueue(Fila.dequeue()) #Remove a primeira variável atual da fila (1) e insere como a terceita (basicamente passou o primeiro para o último)
Fila.enqueue(Fila.dequeue()) #Remove a primeira variável atual da fila (2) e insere como a terceita (basicamente passou o primeiro para o último)
print(Fila.dequeue()) # Remove a primeira variável atual da fila (3)