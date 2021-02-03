stringa = input('per favore scrvi una stringa')
lista_lettere = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
print('I numeri delle lettere che si ripetono sono:')
stringa = list(stringa.upper())
for letter in lista_lettere:
    if stringa.count(lettera)>0:
        print(lettera, ' = ',stringa.count(lettera))
