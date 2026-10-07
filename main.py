import csv
import math

filename = "ensemble.csv"

with open(filename, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    rows = list(reader)

y = rows[0][1:]

x = []
for row in rows[1:]:
    x.append(row[0])

P = [
    [float(value) for value in row[1:]]
    for row in rows[1:]
]

print("Совместный ансамбль:")
print("      ", end="")

for name in y:
    print(f"{name:>8}", end="")
print()

for i in range(len(x)):
    print(f"{x[i]:>6}", end="")
    for j in range(len(y)):
        print(f"{P[i][j]:8.2f}", end="")

    print()

total_P = sum(sum(row) for row in P)

print("\nПроверка суммы вероятностей:")
print(f"Сумма вероятностей = {total_P:.2f}")

P_X = [sum(row) for row in P]

P_Y= [
    sum(P[i][j] for i in range(len(P)))
    for j in range (len(P[0]))
]

print("\nМаргинальные вероятности:")

for i in range (len(x)):
    print(f"P({x[i]})) = {P_X[i]:.2f}")

print()

for i in range(len(y)):
    print(f"P({y[i]}) = {P_Y[i]:.2f}")

print("\nПроверка независимости")

