"""Izveidojiet Python programmu,
kas saskaita no 1 līdz lietotāja ievadītam skaitlim,
izmantojot for ciklu."""



lietotaja_skaitlis = int(input("Ievadi skaitli: "))


summa = 0


for skaitlis in range( lietotaja_skaitlis + 1):
    summa += skaitlis


print(summa)


