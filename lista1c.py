#itens comprados em um mercado

Pao = False
Leite = False
Refrigerante = False
Cerveja = False
Carne = False
Fralda = False


def Fatos():
    global Carne, Refrigerante
    Carne = True
    Refrigerante = True

#encadeamento misto
Fatos()
for i in range(0, 10):
    if Cerveja and Leite:
        Fralda = True

    if Leite and Pao:
        Refrigerante = True
    
    if Cerveja:
        print(f'Cerveja = sim\n')
        break

    if Carne and Refrigerante:
        Cerveja = True

    if Fralda:
        Leite = True
        Pao = True
else:
    print(f'Cerveja = não\n')
    