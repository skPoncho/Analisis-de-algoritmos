def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        print("numpasada  : "+str(numPasada))
        for i in range(numPasada):
            print(" si : "+str(unaLista[i])+" es mayor que : "+str(unaLista[i+1]))
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp
            print(unaLista)

unaLista = [54,26,93,17]
ordenamientoBurbuja(unaLista)
print(unaLista)
