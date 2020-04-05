import requests
import time

print('')
print('#######################################################################')
print('[GATE 1]           CHECKER POWERED BY: iHamiltonRT             [GATE 1]')
print('#######################################################################')
print('')

list = open('Generadas.txt', 'r').readlines()
list = [line.replace('\n', '') for line in list]

for line in list:
    newline = line.split('|')

    CC = newline[0]
    MES = newline[1]
    ANO = newline[2]
    CVV = newline[3]

    aea = (CC+'|'+MES+'|'+ANO+'|'+CVV)

    session = requests.session()  # <--- Crea la sesion

    url = 'http://localhost/prueba//prueba.php?lista='+aea

    response = session.post(url)
    rpta = response.json()

    card = rpta['CC']
    Month = rpta['MES']
    year = rpta['Ano']
    Secure = rpta['CVV']
    Ip = rpta['Ip']

    song = (card+'|'+Month+'|'+year+'|'+Secure)

    Alert = rpta['Estado']
    Alert2 = rpta['suff']

    if 'Your card has insufficient funds.' in Alert:
        print('[WITHOUT FUNDS] ' + song + '  ' + Alert +' '+Ip)
    else:
        if 'Success' in Alert2:
            print('[LIVE] ' + song + '  ' + Alert2+' '+Ip)
        else:
            print('[DEAD] ' + song + '  ' + Alert+' '+Ip)
print('')
print('#######################################################################')
print('[GATE 1]                 F I N A L I Z A D O                   [GATE 1]')
print('#######################################################################')
