# ENTRADA DE DADOS ,
nome = input('Informe o seu nome:')

# exibir a lista de filmes

print("LISTA DE FILMES\n")

print('Sala 1 - A Volta dos Que Não Foram. ')
print('Sala 2 - A Roda Quadrada.')
print('Sala 3 -  Poeira em Alto Mar.')
print('Sala 4 - As Tranças do Rei Careca. ')
print('Sala 5 - A Vingaça do Peixe Frito.'  )

# recebe a sala escolhida

sala = int(input('Informe a sala desejada: '))

# Match case para selecionar a sala

match sala: 
    case 1:
        print(f'Filme escolhido por {nome}: A Volta dos Que Não Foram.')
    case 2:
        print(f'Filme escolhido por {nome}: A Roda Quadrada')
    case 3:
        print(f'Filme escolhido por {nome}: Poeira em Alto Mar.')
    case 4:
        print(f'Filme escolhido por {nome}: As Tranças do Rei Careca.')
    case 5: print(f'Filme escolhido por {nome}: A vingança do Peixe Frito.'
    )
    case _:
        print(f'Opção Não Existente.')
        
        