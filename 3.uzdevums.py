"""Izveidojiet Python programmu,
kas pārbauda, vai ievadītais skaitlis ir nepāra,
izmantojot if priekšrakstu."""

skaitlis = int(input("Ievadiet skaitli: "))


if skaitlis % 2 != 0:
    print("ir nepāra skaitlis.")
else:
    print("ir pāra skaitlis.")