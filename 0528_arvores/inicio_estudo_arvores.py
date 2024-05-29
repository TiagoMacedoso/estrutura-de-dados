import sys

def fatorial(num):
    """ if num == 0:
        return 1
    else:
        return num*fatorial(num-1) """
        
    resultado = num
    
    for i in range(num-1, 0, -1):
        resultado *= i
        
    return resultado
    
num_fatorial = int(input("Informe um número para ser calculado seu fatorial: "))

print(fatorial(num_fatorial))