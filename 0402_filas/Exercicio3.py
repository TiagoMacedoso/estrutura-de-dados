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

Fila = Queue()

menor = 10000000000000000000
maior = -10000000000000000000

for i in range(1, 6):
    num = (int(input("Insira o "+ str(i) + "º número da fila (" + str(6-i) + " número(s) restantes para inserir): ")))
    
    if num<menor:
        menor = num
        
    if num>maior:
        maior = num
        
    Fila.enqueue(num)

tamanhoFila = Fila.size()
soma = 0

for i in range(tamanhoFila):
    soma += Fila.dequeue()
    
print("\n\n\nO MAIOR valor digitado é: " + str(maior))
print("\nO MENOR valor digitado é: " + str(menor))
print("\nA média da fila é: " + str(soma/tamanhoFila) + "\n\n\n")