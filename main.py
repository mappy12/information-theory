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

independent = True

for i in range (len(x)):
    for j in range(len(y)):
        joint_p = P[i][j]
        product_p = P_X[i] * P_Y[j]

        print(f"P({x[i]}, {y[j]}) = {joint_p:.2f}")
        print(f"P({x[i]}) * P({y[j]}) = {product_p:.2f}")

        if not math.isclose(
            joint_p,
            product_p,
            rel_tol=1e-9,
            abs_tol=1e-9
        ):
            independent = False

if independent:
    print("\nАнсамбли X и Y независимы")

else:
    print("Ансамбли X и Y зависимы")

H_XY = 0

for row in P:
    for probability in row:
        if probability > 0:
            H_XY -= probability * math.log2(probability)

print("\nЭнтропия совместного ансамбля")
print(f"H(X, Y) = {H_XY:.6f}")

H_X = 0

for probability in P_X:
    if probability > 0:
        H_X -= probability * math.log2(probability)

print("\nЭнтропия ансамбля X")
print(f"H(X) = {H_X:.6f}")

H_Y = 0

for probability in P_Y:
    if probability > 0:
        H_Y -= probability * math.log2(probability)

print("\n6. Энтропия ансамбля Y")
print(f"H(Y) = {H_Y:.6f}")

print("\n7. Проверка H(X,Y) = H(X) + H(Y)")

print(f"H(X,Y)      = {H_XY:.6f}")
print(f"H(X) + H(Y) = {H_X + H_Y:.6f}")

if math.isclose(H_XY, H_X + H_Y):
    print("Равенство выполняется.")
else:
    print("Равенство не выполняется.")