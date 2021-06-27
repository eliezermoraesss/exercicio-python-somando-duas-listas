"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

lista_A = [100, 2, 3, 4, 5]
lista_B = [1, 2, 3, 1.2, 5]
soma = []

if len(lista_A) <= len(lista_B):
    menor_lista = lista_A
else:
    menor_lista = lista_B

for i in range(len(menor_lista)):
    parcela = lista_A[i] + lista_B[i]
    soma.append(parcela)

print(soma)
