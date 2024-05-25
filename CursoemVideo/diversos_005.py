#Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao
# aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos
# e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta
# se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# a - Maior e Menor Acerto;
# b - Total de Alunos que utilizaram o sistema;
# c - A Média das Notas da Turma.

def cabecalho(txt, tracos, n=0):
    print('-'*tracos)
    if n == 0:
        print(f'{txt}'.center(tracos))
    else:
        print(f'{txt} {n}'.center(tracos))
    print('-'*tracos)


media = cont_aluno = nota = menoracerto = maioracerto = 0
gabarito = ('A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A')
continuar = 'S'

cabecalho(' G A B A R I T O ', 50)
print(gabarito)
while True:
    if continuar == 'N':
        break
    aluno = []
    nota = 0
    cont_aluno += 1
    cabecalho('ALUNO', 20, cont_aluno)
    for c in range(1,11):
        n = str(input(f'Entre com a {c}º resposta: ')).upper().strip()[0]
        aluno.append(n)
    print(f'Respostas do Aluno: {aluno}')
    for c in range(0,10):
        if gabarito[c] == aluno[c]:
            nota += 1
    print(f'Nota do Aluno {cont_aluno}: {float(nota)}')
    media += nota
    if cont_aluno == 1:
        maioracerto = menoracerto = nota
    if nota > maioracerto:
        maioracerto = nota
    if nota < menoracerto:
        menoracerto = nota


    continuar = str(input('Deseja Inserir Mais Um Aluno? [S/N]: ')).upper().strip()[0]

print(f'contador de alunos: {cont_aluno}\nmaior nota: {float(maioracerto)}\nmenor nota: {float(menoracerto)}\nmédia dos {cont_aluno} alunos: {media/cont_aluno}')
