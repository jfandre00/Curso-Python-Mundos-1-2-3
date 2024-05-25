palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ',end='')
    for letra in p:
        if letra.lower() in 'aeiou': #as palavras como áàâãéè deveriam entrar aqui para considerar a acentuação
            print(letra, end= ' ')
