class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
    
pilha = Stack() #Cria um objeto do tipo pilha

for i in range(5):
    pilha.push(input("Digite um valor a ser inserido na pilha: "))
    
for i in range(pilha.size()):
    print(pilha.pop())