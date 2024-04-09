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

fila.enqueue(4)
fila.enqueue('dog')
fila.enqueue(True)
print(fila.size())
print(fila.isEmpty())
fila.enqueue(8.4)
fila.dequeue()
print(fila.dequeue())
print(fila.size())