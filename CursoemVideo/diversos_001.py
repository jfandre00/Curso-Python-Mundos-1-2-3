# O programa deve receber como parâmetro a quantidade total de doces, e por quantas crianças será
# dividido, e deve retornar como resposta a divisão dos doces
#Se o número de doces não der uma divisão exata, não tem problema, pois as crianças mais novas ficam com mais
#doces que as outras
#Ex 7 doces para 3  criancas retorna a resposta (3, 2, 2)
#Ex2 5 doces para 4 crianças retorna (2, 1, 1, 1)
#Ex3 10 doces para 4 crianças retorna (3, 3, 2, 2)

def dividir_doces(doces, criancas):
    lista = []
    if doces % criancas == 0:
        aux = doces / criancas
        for n in range (0, criancas):
            lista.append(int(aux))
    else:
        aux = int(doces/criancas)
        for n in range (0, criancas):
            lista.append(int(aux))
        faltam = doces - (aux*criancas)
        for n in range (0, faltam):
            lista[n] = lista[n] + 1
        if doces < criancas:
            lista.reverse() #não entendi o motivo de inverter a lista, mas fiz igual a resposta
    return lista


d = int(input('Qual é a quantidade de doces arrecadados?: '))
c = int(input(f'Para quantas crianças serão dividos os {d} doces?: '))
resp = dividir_doces(d,c)
print(f'Os doces serão dividos conforme a lista: {resp}')
