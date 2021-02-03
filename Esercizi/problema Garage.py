print ('Problema delnoleggio degli scooter')
print ('Per quanto tempo vuoi noleggiare uno scooter?')
giorni = int(input('Inserisci il numero di giorni'))
if giorni==1:
             print ('Il costo ammonta a 45,00 euro')
if giorni==2:
             print (' Il costo ammonta a 80,00 euro')
if giorni==3:
             print (' Il costo ammonta a 120,00 euro')
if giorni==4:
             print (' Il costo ammonta a 160,00 euro')
Prezzo_extra_giorni = 160+40*(giorni-4)
if giorni > 4:
          print (' Il costo ammonta per ',giorni,' ammonta a',Prezzo_extra_giorni, 'euro')                            
