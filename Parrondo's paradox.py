import random
import matplotlib.pyplot as plt

eps = 0.005
p1 = 0.5
p2 = 0.75
p3 = 0.1

# wariacja dla gry A, z jedna moneta
def gameA(outcome):
    if random.random() < (p1 - eps):
        return outcome + 1  # w przypadku wygranej (ktora jest mniej prawdopodobna nasz kapital wzrasta o jeden
    else:
        return outcome - 1  # w przypadku przegranej tracimy

# wariacja dla gry B, z dwiema monetami
def gameB(outcome):
    if outcome % 3 == 0:  # jesli nasz kapital jest wielokrotnoscia M = 3 to rozwazamy przypadek z moneta 3
        if random.random() < (p3 - eps):
            return outcome + 1   # wygrana
        else:
            return outcome - 1  # przegrana
    else: # jesli kapital nie jest wielokrotnoscia M rozwazamy monete 2
        if random.random() < (p2 - eps):
            return outcome + 1
        else:
            return outcome - 1

def randomSwitchGame(outcome):
    if random.random() < 0.5:  # funckja random() losuje liczbe z zakresu 0:1, dlatego warunek "<0.5"
        return gameA(outcome)  # sprawia, ze jest rowna "szansa" na wylosowanie gry A i gry B
    else:
        return gameB(outcome)


outcome = []
for i in range(100):  # ta petla wylczy nam srednia
    outcome.append(0)
for _ in range(50000):  # w petli wykonujemy dla samej gry A 50 000 powtorzen
    capital = 0
    for i in range(100):
        capital = gameA(capital)
        outcome[i] += capital  # powiekszamy nasz poczatkowy budzet o kapital
for i in range(100):
    outcome[i] /= 50000.0

outcome1 = []
for i in range(100):  # srednia
    outcome1.append(0)
for _ in range(50000):  # w petli wykonujemy dla samej gry B 50 000 powtorzen
    capital = 0
    for i in range(100):
        capital = gameB(capital)
        outcome1[i] += capital
for i in range(100):
    outcome1[i] /= 50000.0

outcome2 = []
for i in range(100):
    outcome2.append(0)
for _ in range(50000):
    capital = 0
    for i in range(100):
        capital = randomSwitchGame(capital)
        outcome2[i] += capital
for i in range(100):
    outcome2[i] /= 50000.0

outcome3 = []
for i in range(100):
    outcome3.append(0)
for _ in range(50000):
    capital = 0
    for i in range(100):
        if i % 3 == 0:
            capital = gameA(capital)
        else:
            capital = gameB(capital)
        outcome3[i] += capital
for i in range(100):
    outcome3[i] /= 50000.0

# rysowanie wykresu
plt.plot(outcome, 'r', outcome3, 'b',outcome1, 'y', outcome2, 'g')
plt.legend(('Gra A','Cykliczne zmiany','Gra B', 'Przypadkowe zmiany'))
plt.xlabel('Ilosc gier')
plt.ylabel('Kapital')
plt.title('Paradoks Parrondo ')
plt.grid(True)
plt.show()

