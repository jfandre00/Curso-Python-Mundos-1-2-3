'''Regras para o cálculo dos dígitos verificadores do CPF - É utilizado como exemplo o número: 123456789.
Calcule a soma dos produtos dos nove digitos utilizando peso 2 para unidade, peso 3 para dezena, peso 4 para centena
e assim sucessivamente. Exemplo: 9*2+8*3+7*4+6*5+5*6+4*7+3*8+2*9+1*10 = 210
A dezena do número verificador é 0 caso o resto da divisão por 11 da soma dos produtos seja 0 ou 1;
caso contrario a dezena corresponde a subtrair de 11 o resto da divisão por 11 da soma dos produtos.
Exemplo: resto da divisão de 210 por 11 é 1 então a dezena do número verificador é 0.

Calcule a soma dos produtos dos dez digitos, onde o digito menos significativo passa a ser a dezena dos digitos
verificadores, utilizando os seguintes pesos: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11;
Exemplo: 2*0+3*9+4*8+5*7+6*6+7*5+8*4+9*3+10*2+11*1=255.

A unidade do número verificador é 0 caso o resto da divisão da soma dos produtos seja 0 ou 1; caso contrário
a unidade corresponde a 11 menos o resto da divisão por 11 da soma dos produtos.
Exemplo:resto da divisão de 255 por 11 é 2 então a unidade do número verificador é 11-2=9.'''

def verificar_cpf(teste, tipo):
    if tipo == 'dezena':
        c = 10
    elif tipo == 'unidade':
        c = 11
    soma = i = 0
    while c >= 2:
        soma = int(teste[i])*c + soma
        i += 1
        c -= 1
    if soma % 11 == 0 or soma % 11 == 1:
        verificador = 0
    else:
        verificador = 11 - (soma%11)
    return verificador


def tratar_cpf(ncpf):
    ncpf = ncpf.replace('.','')
    ncpf = ncpf.replace('-','')
    ncpf = ncpf.replace('/','')
    ncpf = ncpf.replace(' ', '')
    return ncpf


cpf = str(input('Entre com o CPF no formato: xxx.xxx.xxx-xx: ')).strip()
cpf_tratado = tratar_cpf(cpf)
teste = cpf_tratado.isnumeric()
if teste == False or len(cpf_tratado) != 11:
    print('CPF Inválido! Saindo...')
else:
    digito = cpf_tratado[9:11]
    dezena_ver = verificar_cpf(cpf_tratado[0:9], 'dezena')
    unidade_ver = verificar_cpf(cpf_tratado[0:10], 'unidade')
    digito_calculado = str(dezena_ver) + str(unidade_ver)
    if digito_calculado == digito:
        print('CPF Válido!!!')
    else:
        print('CPF Inválido!!')
