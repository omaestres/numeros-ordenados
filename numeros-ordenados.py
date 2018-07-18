#!/usr/bin/env python

with open('entrada.txt', 'r') as in_file:
    numeros = in_file.readlines()

with open('salida.txt', 'w') as out_file:
    for j in range(1, int(numeros[0]) + 1):
        N = numeros[j].strip()
        flag = True
        O = int(N)
        while flag:
            flag = False
            for i in range(len(str(O)) - 1):
                if str(O)[i] > str(O)[i + 1]:
                    O -= int(str(O)[i + 1:])
                    O -= 1
                    flag = True
                    break
        while not (list(str(O)) == sorted(str(O))):
            O -= 1
        out_file.write("Caso {}: N={}, O={}\n".format(j, N, O))

