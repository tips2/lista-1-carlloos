
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


#encadeamento para trás
Fatos()
for i in range(0, 10):

    if Carne and Refrigerante:
        Cerveja = True

    if Fralda:
        Leite = True
        Pao = True

    if Cerveja and Leite:
        Fralda = True

    if Leite and Pao:
        Refrigerante = True
    if Cerveja:
        print('Cerveja = sim\n')
        break
else:
    print('Cerveja = não\n')
