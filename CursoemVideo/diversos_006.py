#validar numero de cartao de crédito pela formula de Luhn e converter a string para numeros removendo espacos e traços
#sequencias de comprimento 1 ou menos não são válidas - espaços são permitidos mas devem ser eliminados antes de verificar
#todos os outros caracteres que não sejam digitos não são permitidos
def validar_num(cartao):
    soma = 0
    lista = []
    cartao_lista = []
    substituir = []
    compr = len(cartao) - 2
    for l in range(0, len(cartao)):
        cartao_lista.append(cartao[l]) #criei uma lista com os numeros do cartão
    for l in range(compr, -1, -2):
        lista.append(int(cartao[l])) #1ºetapa -> PEGANDO CADA SEGUNDO DIGITO, COMEÇANDO PELA DIREITA
        substituir.append(l) # LISTA DE APOIO COM OS INDICES DOS NUMEROS QUE PEGUEI ACIMA
    for i, n in enumerate(lista):
        if n*2 > 9:     #DOBRANDO OS NUMEROS DA LISTA SEGUINDO A REGRA ABAIXO DE FOR MAIOR QUE 9
            a = n*2 - 9
            lista[i] = a
        else:
            a = n*2
            lista[i] = a
    for n in range(0, len(substituir)):
        cartao_lista[substituir[n]] = lista[n] #VAMOS MANTER OS OUTROS NUMEROS E SUBSTITUIR SOMENTE OS DA LISTA
    for n in range (0, len(cartao_lista)):
        soma += int(cartao_lista[n])  #SOMANDO TODOS OS DIGITOS DESSE NOVO CARTAO
    if soma % 10 == 0:      #SENDO DIVISIVEL POR 10, O CARTAO É VÁLIDO
        print('Cartão é Valido!')
    else:
        print('Cartão INVÁLIDO!!')


while True:
    cartao = str(input('Digite o número do cartão: ')).strip()
    for i in cartao:
        cartao = cartao.replace('-', '')
        cartao = cartao.replace(' ', '')
    if cartao.isdigit() == False:
        print('Erro! Esse cartão contém Letras!!')
        break
    if len(cartao) <= 1:
        print('Erro! Esse cartão contém 1 número ou menos!!')
        break
    validar_num(cartao)
    break



