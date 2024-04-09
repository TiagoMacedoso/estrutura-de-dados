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
    
fila1 = Queue()
fila2 = Queue()

while True:
    fila1.enqueue((int(input("Insira um número inteiro na PRIMEIRA fila: "))))
    
    teste = input("Deseja inserir mais um número na fila? (Sim/Não)")
    
    if teste == "Não" or teste == "não" or teste == "n" or teste == "Nao" or teste == "nao":
        break
    
while True:
    fila2.enqueue((int(input("Insira um número inteiro na SEGUNDA fila: "))))
    
    teste = input("Deseja inserir mais um número na fila? (Sim/Não)")
    
    if teste == "Não" or teste == "não" or teste == "n" or teste == "Nao" or teste == "nao":
        break    
    
if fila1.size() == fila2.size():
    print("\n\nAs duas filas têm o mesmo tamanho!")

elif fila1.size() > fila2.size():
    print("\n\nA PRIMEIRA fila é MAIOR que a segunda fila")

else:
    print("\n\nA SEGUNDA fila é MAIOR que a segunda fila")
    