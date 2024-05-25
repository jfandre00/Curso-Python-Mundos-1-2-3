#colocar cores nos erros!!! // criar funções para dividir o codigo // usar arquivo externo para listas

from random import choice
lista_facil = ['Amor', 'Alfa', 'Bola', 'Bicho', 'Carro', 'Prego', 'Tenis', 'Pera', 'Mola', 'Sofa', 'Cama', 'Bala',
         'Cola', 'Peru', 'Pilha', 'Lapis', 'Livro', 'Cafe', 'Curso', 'Limao', 'Dedo', 'Deus', 'Pneu', 'Porta',
         'Bomba', 'Mesa', 'Dedo', 'Rato', 'Selo', 'Sino', 'Luva', 'Lobo', 'Lata', 'Unha', 'Vovo', 'Frio',
         'Meio', 'Mala', 'Bolsa', 'Tralha', 'Urso', 'Teia', 'Foco']
lista_medio = ['Amarelo', 'Amiga', 'Namorado', 'Alimento', 'Aviao', 'Capacete', 'Balao', 'Bebida', 'Bolada', 'Branco', 'Camisa', 'Caneca',
         'Celular', 'Comida', 'Clube', 'Esfera', 'Dromedario', 'Elefante', 'Escola', 'Estojo', 'Garfo', 'Colher', 'Manteiga', 'Geleia',
         'Girafa', 'Janela', 'Limonada', 'Marido', 'Melado', 'Noite', 'Oculos', 'Onibus', 'Omelete', 'Porteiro', 'Padaria', 'Parque',
         'Passarinho', 'Peixe', 'Pijama', 'Cachorro', 'Refrigerante', 'Corrida', 'Biscoito']
lista_dificil = ['Tangerina', 'Abacate', 'Caramelo', 'Carambola', 'Televisao', 'Borboleta', 'Enfraquecer', 'Politica', 'Telefonema',
         'Matematica', 'Inteligencia', 'Relacionamento', 'Colecionador', 'Condicionador', 'Paralelepipedo', 'Proposito', 'Maturidade',
         'Pandemia', 'Ratificar', 'Plenitude', 'Hermetico', 'Extraordinario', 'Deferido', 'Remanescente','Escrupulo', 'Paradigma',
         'Alameda', 'Paradoxo', 'Necessidade', 'Nostalgia', 'Resolucao', 'Relevante', 'Harmonia']
resp = 'S'
pontos = 0
while True:
    if resp == 'S':
        while True:
            palavras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U',
                        'V', 'X', 'Y', 'W', 'Z']
            acerto = erro = 0
            desafio = []
            print('-' * 40)
            print(f'Bem vindo ao jogo de Forca v1.0!'.center(40))
            print('-' * 40)
            print('Escolha o Nível de Dificuldade: \n1 - Fácil\n2 - Médio\n3 - Difícil')
            escolha = int(input('Digite aqui (1, 2 ou 3): '))
            if escolha == 1:
                palavra = choice(lista_facil).upper()
                break
            elif escolha == 2:
                palavra = choice(lista_medio).upper()
                break
            elif escolha == 3:
                palavra = choice(lista_dificil).upper()
                break
            else:
                print('Escolha Inválida. Tente Novamente!')
        for c in range (0, len(palavra)):
            desafio.append('-')
        print(desafio)
        while True:
            palpite = str(input('Digite um palpite: ')).upper()
            if palpite not in palavras:
                print('Esse palpite já foi registrado! Tente Novamente!')
                print(f'Opções Disponíveis: {palavras}')
                print(desafio)
            else:
                if palpite in palavra:
                    for c in range (0, len(palavra)):
                        if palpite == palavra[c]:
                            desafio[c] = palpite
                            acerto += 1
                            print(desafio)
                else:
                    erro += 1
                    print(f'Erro {erro} de 5')
                    print(desafio)
                palavras.remove(palpite)
                print(f'Opções Disponíveis: {palavras}')
                if acerto == len(palavra):
                    print(f'Parabéns você venceu!! A palavra era {palavra}')
                    if escolha == 1:
                        pontos = pontos + (100 - 20*erro)
                    if escolha == 2:
                        pontos = pontos + (150 - 30*erro)
                    if escolha == 3:
                        pontos = pontos + (200 - 40*erro)
                    print(f'Você está com {pontos} pontos!')
                    break
                if erro == 5:
                    print(f'PERDEU, 5 erros, a palavra era {palavra}')
                    break
    elif resp == 'N':
        print(f'Obrigado por Jogar! Você fez {pontos} pontos hoje!')
        break
    else:
        print('Entrada Inválida! Tente Novamente!')
    resp = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]