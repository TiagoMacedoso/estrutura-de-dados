#Criação de listas
elementos = [1, 3, 7, 15, 20, 22]

#Exibição de ítens que estão na lista
print(elementos)
print(elementos[3])
print(elementos[-3])

#Cálculos com listas
zeros = [0] * 50
print(zeros)

#Contagens de ítens dentro de uma lista
print(len(zeros))

#Concatenação entre listas
texto0 = ['ADS na Facens']
texto1 = ['é nota 5 no MEC']
""" Nesse modo criasse uma lista que junta as duas listas """
print(texto0 + texto1)
""" Dessa forma são extraídos os ítens que estão na primeira casa da lista """
print(texto0[0] + texto1[0])

#Remoção de ítens em uma lista
valores = [10, 20, 30, 40, 50]
print(valores)
""" Dessa forma remove através do valor que compõe o ítem """
valores.remove(10)
""" Dessa forma remove através do index """
del valores[0]
print(valores)

#Intervalos de listas
palavras = ["Cadeira", "Mesa", "Lousa", "Luminária"]
""" Imprime toda a lisa """
print(palavras)
""" Imprime um intervalo de lista (o número após o : não é incluso) """
print(palavras[1:4])
""" Inverte a lista. (::) representa todo o intervalo, (::-1) representa o intervalo da lista começando do último(-1) """
print(palavras[::-1])

#Criação de matriz
matriz = [[1,2,3], [4,5,6], [7,8,9]]
print(matriz)
print(matriz[0][0], matriz[1][0], matriz[2][0])