notas = [20,15,12,12,8,4,1]

for general in range (1,len(notas)):
    for i in range (len(notas)-general):
        if notas[i] > notas[i+1]:
            #print(notas[i],notas[i+1] )
            nota = notas[i]
            notas[i] = notas[i+1]
            notas[i+1] = nota

print(notas)