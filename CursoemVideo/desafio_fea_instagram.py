def funcao_misteriosa(n):
    resultado = []
    for i in range(n):
        if i % 2 == 0:
            resultado.append(i*2)
        else:
            resultado.insert(0,i)
    return resultado

n = int(input(f'Digite o número: '))
print(funcao_misteriosa(n))
