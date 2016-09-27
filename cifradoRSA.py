import math

n = 1007
e = 335
d = 95

tn = 1457
te = 203

def encriptar (m,n,e):
    return ((m**e) %n)

def desencripta(c, n, d):
    return ((c**d) % n)

def getm(message):
    message = message.upper()
    accum = 0;
    contador = 1;
    for letra in message:
        letraASCII = ord(letra)-64
        accum += letraASCII*(math.pow(27,len(message)-contador))
        contador += 1
    return int(accum)

def getmessage(m, palabra):
    if (m % 27 == 0):
        palabra.append(int(m/27))
        print(palabra)
        return palabra
    palabra.append(m%27)
    getmessage(m-(m%27),palabra)

    
print(encriptar(getm("PY"),tn,te))
print(encriptar(getm("TH"),tn,te))
print(encriptar(getm("ON"),tn,te))
print(encriptar(getm("TA"),tn,te))
print(encriptar(getm("IL"),tn,te))

