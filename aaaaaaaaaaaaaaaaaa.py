#5.	Verifique se um elemento informado pelo usuário está presente dentro de uma tupla predefinida.
#6.	Crie dois conjuntos com números de 1 a 10 e de 5 a 15. Exiba a união, interseção e diferença entre eles.
#7.	Peça ao usuário para digitar 10 números (permitindo repetições). Armazene em um conjunto e exiba apenas os números únicos.
#8.	Verifique se dois conjuntos têm ao menos um elemento em comum. Caso positivo, mostre os elementos comuns.
#9.	Remova elementos repetidos de uma lista utilizando um conjunto.
#10.	Dado um conjunto de palavras, conte quantas palavras únicas ele contém.
#11.	Crie um dicionário com 5 alunos e suas respectivas notas. Calcule e exiba a média de cada aluno.
#12.	Solicite ao usuário nome e idade de 5 pessoas e armazene em um dicionário. Em seguida, exiba apenas as pessoas maiores de idade.
#13.	Crie um dicionário com os meses do ano como chave e a quantidade de dias como valor. Depois, permita que o usuário digite um mês e informe a quantidade de dias.
#14.	Cadastro de produtos (com while) (Até o usuário digitar Sair deve ser cadastro os produtos)
#15.	Soma dos valores do dicionário (com while) Crie um Carrinho de compras aonde você insere os produtos no dicionário por input e seu preço no final você deve calcular o valor de todos os produtos.

tupla = (1,2,3,2,4,2)
n1 = int(input('Digite o numero que seseja saber se esta na tupla: \n'))
n2 = tupla.count(n1)
if n2 != 0: 
    print('O numero não aparece na lista')
else:
    print('O numero aparece na lista')