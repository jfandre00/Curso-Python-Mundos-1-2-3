#primeiro e último nome de uma pessoa
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

#para pegar a ultima posição -> fazendo len(nome) eu sei quantas posições tem o nome (na lista), coloco o -1 pq começa em ZERO
#exemplo nome Andre L M Ferreira -> nome tem 4 posições, len(nome) = 4, mas o ferreira está na posição 3
#portanto -> nome[len(nome)-1] = nome[3] = Ferreira
