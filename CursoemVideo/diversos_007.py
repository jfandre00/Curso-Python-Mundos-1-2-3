#Exercicio de DNA e RNA
#Dado o DNA, o RNA transcrito é formado pela substituição de cada nucleotídeo pelo seu complemento
# G -> C // C -> G // T -> A // A -> U  - exemplo ACGTGGTCTTAA - Saída UGCACCAGAAUU

rna = []
cont = 0
dna = str(input('Entre com o DNA: ')).upper().strip()
for c in range(0, len(dna)):
    if dna[c] not in 'ATCG':
        cont += 1
if cont > 0:
    print('ERRO! O DNA INFORMADO NÃO EXISTE!')
if cont == 0:
    for c in range(0, len(dna)):
        if dna[c] == 'G':
            rna.append('C')
        elif dna[c] == 'C':
            rna.append('G')
        elif dna[c] == 'T':
            rna.append('A')
        else:
            rna.append('U')
rna_alterado = ''.join(rna)
print(f'O RNA é: {rna_alterado}')