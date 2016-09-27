def encriptar(mensaje, llave):
    mensaje = mensaje.upper()
    llave = llave.upper()
    nuevoString = ""
    contador = 0
    for letra in mensaje:
        letraASCII = ord(letra)-65
        #print("letra: "+letra)
        #print("ascii: "+str(letraASCII))
        llaveASCII = ord(llave[contador%len(llave)])-65
        #print("llave"+llave[contador%len(llave)])
        #print("llave ASCII: " + str(llaveASCII))
        ASCII = ((letraASCII)+(llaveASCII))%26
        nuevoString += chr(ASCII+65)
        #print("nuevoASCII: " + str(ASCII))
        #print("nuevaletra: "+ chr(ASCII+65))
        contador += 1
        #print("-----------")
    return nuevoString

def desencriptar(texto,key):
    texto = texto.upper()
    key = key.upper()
    nuevoString = ""
    contador = 0
    for letra in texto:
        letraASCII = ord(letra)-65
        #print("letra: "+letra)
        #print("ascii: "+str(letraASCII))
        llaveASCII = ord(key[contador%len(key)])-65
        #print("llave"+llave[contador%len(llave)])
        #print("llave ASCII: " + str(llaveASCII))
        ASCII = ((letraASCII)-(llaveASCII))%26
        nuevoString += chr(ASCII+65)
        #print("nuevoASCII: " + str(ASCII))
        #print("nuevaletra: "+ chr(ASCII+65))
        contador += 1
        #print("-----------")
    return nuevoString

def separador (texto,num):
    lista1 = ""
    lista2 = ""
    lista3 = ""
    lista4 = ""
    counter = 1
    if num == 1:
        for letra in texto:
            if(counter % 4 == 1):
                lista1 += letra
            elif(counter % 4 == 2):
                lista2 += letra
            elif(counter %4 == 3):
                lista3 += letra
            elif(counter % 4 == 0):
                lista4 += letra
            counter += 1
    elif num == 2:
        for letra in texto:
            if(counter % 2 == 1):
                lista1 += letra
            elif(counter % 4 == 0):
                lista2 += letra
            counter += 1
    elif num == 3:
        for letra in texto:
            if(counter % 3 == 1):
                lista1 += letra
            elif(counter % 3 == 2):
                lista2 += letra
            elif(counter %3 == 0):
                lista3 += letra
            counter += 1
    elif num == 4:
        for letra in texto:
            if(counter % 4 == 1):
                lista1 += letra
            elif(counter % 4 == 2):
                lista2 += letra
            elif(counter %4 == 3):
                lista3 += letra
            elif(counter % 4 == 0):
                lista4 += letra
            counter += 1
    return [lista1,lista2,lista3,lista4]

def llavefounder(char):
    charASCII = ord(char)-4
    return chr(((charASCII-65)%25)+65)

mensaje = "legionariosaztecas"
llave = "buzo"
mensajeEncriptado = "MYFWPHZFJIROANDQBM"

mensaje2 = "TVBVOMEXZAVQFTNXPMAMRUNVZBBVDMNGSZBXZZQVFUBJEPRFZUOISIQXHWPSXXYIEMFIEABJNWAXLKGWZVRJZZVRACGXZENVOAGLPZRJWMPXZZNROBUIZBUICNBVZCGTFBSVZUGLPZRJWMPXZZFSEPNXEPRVPNYINBRHDQTRLTPSFTQTLAFFLKXXSZBYRPNWPXNVLBRWPBBJNWAXLKGWPIPLOZHQSIQSYMUYYLEIOIAHQWHVHQEIMZHWSMFASQPLXIQINWAXLKGATBUXSMCPLBRSYBBASQPLEPRCHMEIWWNHPLGLPJEYDPRWLVQXSMPSCZRWAWAHTVTWPBBJNWAXLKGWZVGLPXYEEMJICMNVCIAKPLVRQWHVNWAGPVGVTKPMCKYIDWSXHMAXJAVBEPRSFBRVAIVVZNPMCKYIDQATFBNROWHXACGAPZRIBCVZLTRREBBXSMPYCZRREQAEYMAMRUNTLAFMYOVRZVRHTZRGEQBREPESFOUXSMFGCIZFWMEEYLGLPQARPZCETZRUFQIEWMAXEWGLPKHVCMAXQTBATVTMYBUIZXCSDQGIOQEINBVSY"
llave1 = "L" #L o V
llave2 = "LN" #L o N, T o E
llave3 = "WLV" #W o N, L o T, V o R
llave4 = "LINE" #L o V, I o X, N o W, T o E
print(separador(mensaje2,4))
print(llavefounder("P"))
##print(encriptar(mensaje,llave))
print(desencriptar(mensaje2,llave4))
