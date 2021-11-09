
def dv(ean):
    ean = str(ean)
    sum1,sum3,soma,eanNovo = 0,0,0,''
    for i in range(len(ean)):
        if i % 2 == 0:
            sum1 += int(ean[i])
        else:
            sum3 += (int(ean[i]) * 3)
    eanAux = ean[0:13]
    dig = (((sum1+sum3) // 10)*10+10) - (sum1+sum3)
    if dig == 10:
        dig = 0
    eanNovo = eanAux + str(dig)
    return eanNovo


def checa(ean):
    ean = str(ean)
    if len(ean) == 14:
        ean = ean[1:13]
        eanNovo = dv(ean)
    elif len(ean) == 13:
        ean = ean[0:13]
        eanNovo  = dv(ean)
    else:
        eanNovo = dv(ean)
    return eanNovo


e = input('Digite seu EAN-13:  ')
print(checa(e))
s=''
while s != 's':
    s = input("sair? [S/N]: ")
    if s.lower() == 'n':
        e = input('Digite seu EAN-13:  ')
        print(checa(e))
