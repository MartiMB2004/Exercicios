#Tupla dentro de Tupla
loc = (('Casa', -21.119574, -44.224794), ('Trabalho', -21.129347, -44.162196), ('Senac', -21.134943, -44.261105 ), ('Sitio', -21.048978, -44.200247))
#Acessando a idade do segundo elemento (índice 1)
latitude = loc[1][1]
longitude = loc[1][2]
dados = loc[1][0]
print(f'Seu local é: {dados}')
print(f'A latitude do {dados} o é: {latitude}')
print(f'A longitude do {dados} é: {longitude}')
