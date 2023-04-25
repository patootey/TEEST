import matplotlib.pyplot as py


def Vt(m, g, Aird, cd, A):
    return ((2 * m * g) / (Aird * cd * A)) ** (1 / 2)


def Lmkraft(m, A, cd, tetthet, v):
    return m * A * cd * tetthet * (v**2) / 2


def Tfart(m, g, tetthet, cd, A):
    return ((2 * m * g) / (tetthet * cd * A)) ** 0.5


def taksel(g, m, q, y):
    return round((g - (q / m) * (y**2)), 10)


def epformel(a, x, x1, y1):
    return a * (x - x1) + y1

tid = []
hoyde = []
fart = []
akselerasjon = []
def main():
    g = 9.81
    Aird = 1.225

    m = float(5)
    A = float(10)
    cd = float(0.34)

    h = float(20)

    v = 0
    t = 0
    a = 0
    q = (1 / 2) * Aird * cd * A
    d = 0.1



    while h > 0:
        tid.append(t)
        hoyde.append(h)
        fart.append(v)

        a = taksel(g, m, q, v)
        v = epformel(a, t + d, t, v)
        t = t + d
        h = h - (v * d)

        akselerasjon.append(a)

    py.plot(tid, fart)
    py.xlabel("Tid")
    py.ylabel("Fart i m/s")
    py.grid()
    py.show()

    py.plot(tid, hoyde)
    py.xlabel("Tid")
    py.ylabel("HÃ¸yde i m")
    py.grid()
    py.show()

    py.plot(tid, akselerasjon)
    py.xlabel("Tid")
    py.ylabel("Akselerasjon")
    py.grid()
    py.show()

    print("Hastighet nadd =", round(fart[len(fart) - 1], 3))
    print("Terminalhastighet =", round(Vt(m, g, Aird, cd, A), 3))



if __name__ == "__main__":
    main()
    print(fart)
