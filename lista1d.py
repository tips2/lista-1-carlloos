#sintomas
dor_de_cabeca = False
garganta_inflamada = False
tosse = False
cansaco = False
tontura = False
dor_articulacao = False
febre = False
conjuntivite = False
coceira = False
perda_olfato = False

#doenças
gripe = False
estresse = False
mononucleose_infecciosa = False
amigdalite = False
estresse = False
dengue = False
chikungunya = False
zika = False
covid = False

def Fatos():
    global tontura,dor_articulacao,febre,conjuntivite,coceira,perda_olfato,tosse, cansaco, dor_de_cabeca
    cansaco = True
    dor_de_cabeca = True


Fatos()
while True:

    if cansaco & dor_de_cabeca:
        mononucleose_infecciosa = True
        print('Mononucleose Infecciosa = sim\n')
        break
    if cansaco & garganta_inflamada:
        amigdalite = True
        print('Amigdalite = sim\n')
        break
    if tontura & dor_articulacao & febre:
        dengue = True
        print('Dengue = sim\n')
        break

    if dor_articulacao & febre & conjuntivite & coceira:
        zika = True
        print('Covid = sim\n')
        break
    if dor_articulacao & febre & conjuntivite:
        chikungunya= True
        print('Covid = sim\n')
        break
    if dor_de_cabeca & garganta_inflamada & tosse & perda_olfato:
        covid = True
        print('Covid = sim\n')
        break
    if dor_de_cabeca & garganta_inflamada & tosse:
        gripe = True
        print('Gripe = sim\n')
        break

    if dor_de_cabeca: 
        print('Analgésico = sim\n')
        break

    if cansaco:
        estresse = True
        print('Estresse = sim\n')
        break

