print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo),end='')
        termo = termo + razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? 0 para sair: '))
print('Progressão finalizada com {} termos mostrados'.format(total))