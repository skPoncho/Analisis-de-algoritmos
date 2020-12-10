import random
f = open ('datos.txt','w')
for i in range(40000):
    numero  = random.randrange(0, 20000, 1);
    print(numero)
    f.write(str(numero)+"\n")



f.close()
