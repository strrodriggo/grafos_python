# usando a bliblioteca intertools, função permutations para conseguir os caminhos possiveis dentro do grafo
from itertools import permutations

# essa função é responsavel por criar o grafo, recebe o vertice, e pede o priemeiro e o segundo vertice interligado para formar o grafo

def criar_grafo(num_vertices):
    grafo = {}
    for i in range(num_vertices):
        grafo[i] = set()
    while True:
        v1 = int(input("digite o pimeiro vertice da aresta: "))
        if v1 == -1:
            break
        v2 = int(input("digite o segundo vertice da aresta: "))
        grafo[v1].add(v2)
        grafo[v2].add(v1)
    return grafo

# essa função é responsavel por achar os caminhos possiveis dentro do grafo, atravez de testes de permutações, dentro da função permutations dentro de intertools
#ou sejá, ela fica reordedando os vertices para testar se os caminhos são possiveis baseado na função criar grafo onde pasamos os parametros dentro do array
def buscar_caminhos(grafo, origem, destino):
    caminhos = []
    visitados = set()
    def buscar(vertice_atual, caminho_atual):
        if vertice_atual == destino:
            caminhos.append(caminho_atual)
        else:
            visitados.add(vertice_atual)
            for proximo_vertice in grafo[vertice_atual] - visitados:
                buscar(proximo_vertice, caminho_atual + [proximo_vertice])
            visitados.remove(vertice_atual)
    buscar(origem, [origem])
    return caminhos

# essa função sorted resposavel por organizar a lista, a função len é reponsavel por determinar a quantidade de intens dentro do array
# quanto menor for o tamanho do array, menor o caminho sera
def ordenar_caminhos(caminhos):
    return sorted(caminhos, key=lambda caminho: len(caminho))

# sistema de armazenamento das informações principais
num_vertices = int(input("quantidade de vertices do grafo: "))
grafo = criar_grafo(num_vertices)
origem = int(input("vertice de origem: "))
destino = int(input("vertice de destino: "))
caminhos = buscar_caminhos(grafo, origem, destino)
caminhos_ordenados = ordenar_caminhos(caminhos)
# printa todos os caminhos encontrados(os arrays) em ordem de tamanho
print("caminhos encontrados:")
for caminho in caminhos_ordenados:
    print(caminho)
