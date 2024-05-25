times = ('Cor', 'Pal', 'San', 'Gre', 'Cru', 'Fla', 'Vas',
         'Cha', 'Atl-MG', 'Bot', 'Atl-PR', 'Bah', 'SãoP',
         'Flu', 'Sport', 'Vitória', 'Coritiba', 'Avaí', 'Ponte',
         'Atl-GO')
for t in times:
    print(t)
print('-='*15)
print(f'Lista de times: {times}')
print('-='*15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-='*15)
print(f'Os 4 últimos colocados são {times[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*15)
print(f'O Chapecoense está na {times.index("Cha")+1}ª posição')