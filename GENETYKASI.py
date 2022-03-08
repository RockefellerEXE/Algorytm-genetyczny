import random
import datetime

max_pop = 0
dlugosc_gen = 0
minimalna_sila = 0
generacja = 1
koniec = False
populacja = []
populacja_tymczasowa = []


def set_pop():
    x = input("Podaj ilość populacji (min 3): ")
    try:
        x = int(x)
        if x <= 2:
            set_pop()
        return x
    except:
        set_pop()


def set_dl():
    x = input("Podaj długość chromosomu (min 3): ")
    try:
        x = int(x)
        if x <= 2:
            set_dl()
        return x
    except:
        set_dl()


def set_sil():
    print("Podaj minimalną siłę zakończenia algorytmu (min 1 max",
          dlugosc_gen, "): ", end="")
    x = input("")
    try:
        x = int(x)
        if x > dlugosc_gen or x <= 0:
            set_sil()
        return x
    except:
        set_sil()


class Osobnik:
    pass


def stworz():
    for x in range(max_pop):  # generowanie osobników
        z = Osobnik()
        z.chromosom = ""
        for y in range(dlugosc_gen):
            z.chromosom = z.chromosom + str(random.randrange(0, 2))
        populacja.append(z)
    set_sila()


def set_sila():
    for x in range(max_pop):
        populacja[x].sila = populacja[x].chromosom.count("1")


def set_sila_t():
    for x in range(len(populacja_tymczasowa)):
        populacja_tymczasowa[x].sila = populacja_tymczasowa[x].chromosom.count(
            "1")


def mutuj():
    for x in range(max_pop):
        populacja[x].chromosom = mutacja(populacja[x].chromosom)
    set_sila()


def mutacja(chromosom):
    czy_bd = random.randrange(1, 101)
    nowychromosom = ""
    # ((chromosom.count("0")/dlugosc_gen)*100)  im więcej 0 tym większa szansa na mutację // do testów
    if czy_bd <= 20:  # szansa na mutację w chromosomie (ustaw na ok 20%
        #print("Mutacja z : ", chromosom)
        i = 0
        for x in chromosom:
            if 95 <= random.randrange(1, 101):  # szansa na mutację genu
                if x == "0":
                    x = "1"
                else:
                    x = "0"
            nowychromosom = nowychromosom + x
        #print("Mutacja w : ", nowychromosom)
        return nowychromosom

    else:
        return chromosom


def wypisz():
    set_sila()
    print("\tPOPULACJA")
    for x in range(max_pop):
        print("%11s %2s %8s " % ("Osobnik nr:", x + 1, "Genom:"), end="")
        print(populacja[x].chromosom, end=" ")
        print("\tSiła :", populacja[x].sila)
    print("\n")


def wypisz_t():
    set_sila_t()
    print("POPULACJA TYMCZASOWA")
    for x in range(len(populacja_tymczasowa)):
        print("%11s %2s %8s " % ("Osobnik nr:", x + 1, "Genom:"), end="")
        print(populacja_tymczasowa[x].chromosom, end=" ")
        print("\tSiła :", populacja_tymczasowa[x].sila)
    print("\n")


def czykoniec():
    for x in range(max_pop):
        if populacja[x].sila >= minimalna_sila:
            return True
    return False


def sortowanie():
    set_sila()
    j = 0
    while j < max_pop - 1:
        i = 0
        while i < max_pop - 1:
            if populacja[i].sila < populacja[i + 1].sila:
                populacja[i], populacja[i + 1] = populacja[i + 1], populacja[i]
            i += 1
        j += 1


def selekcja():
    if max_pop % 2 == 0:
        for x in range(int(max_pop / 2 + 1)):
            populacja_tymczasowa.append(populacja[x])

    else:
        for x in range(int((max_pop - 1) / 2)):
            populacja_tymczasowa.append(populacja[x])

        populacja_tymczasowa.append(populacja[int((max_pop - 1) / 2 + 1)])


def krzyzowanie():
    pkt_krzyz = random.randrange(1, dlugosc_gen)
    print("PUNKT KRZYŻOWANIA: ", pkt_krzyz)
    global populacja_tymczasowa
    if max_pop % 2 == 0:
        pol = (max_pop / 2)
    else:
        pol = ((max_pop - 1) / 2)
    x = 0
    while x <= pol:
        p1 = Osobnik()
        p2 = Osobnik()
        A1 = populacja_tymczasowa[x].chromosom[0:pkt_krzyz]
        A2 = populacja_tymczasowa[x].chromosom[pkt_krzyz::]
        B1 = populacja_tymczasowa[x + 1].chromosom[0:pkt_krzyz]
        B2 = populacja_tymczasowa[x + 1].chromosom[pkt_krzyz::]
        p1.chromosom = A1 + B2
        p2.chromosom = B1 + A2
        populacja_tymczasowa.append(p1)
        populacja_tymczasowa.append(p2)

        x += 2
    global populacja
    populacja = None
    populacja = populacja_tymczasowa

    git = False
    while git == False:
        git = True
        if len(populacja) > max_pop:
            populacja.pop()
            git = False


def idealni():
    print("SPIS OSOBNIKÓW IDEALNYCH : ")
    for x in range(max_pop):
        if populacja[x].sila >= minimalna_sila:
            print("%11s %2s %8s " % ("Osobnik nr:", x + 1, "Genom:"), end="")
            print(populacja[x].chromosom, end=" ")
            print("\tSiła :", populacja[x].sila)


def nazwa():
    x = datetime.datetime.now().strftime("%d_%m_%Y-%H_%M_%S") + ".txt"
    return x


################################################


max_pop = set_pop()
dlugosc_gen = set_dl()
minimalna_sila = set_sil()

print("GENERACJA: ", generacja)
stworz()  # PIERWSZA GEMERACJA
wypisz()
koniec = czykoniec()
while koniec == False:
    # SELEKCJA ( połowa najlepszych METODA RANKINGOWA)
    sortowanie()
    selekcja()
    #print("PRZED MUTACJĄ")
    # wypisz()
    #print("MOMENT MUTACJI")
    mutuj()
    #print("PO MUTACJI")
    # wypisz()
    #print("PRZED KRZYŻOWANIEM")
    # wypisz_t()
    #print("MOMENT KRZYŻOWANIA")
    krzyzowanie()
    set_sila()
    #print("PO KRZYŻOWANIU")
    # wypisz_t()
    populacja_tymczasowa = []
    generacja += 1
    print("GENERACJA: ", generacja)
    sortowanie()
    wypisz()
    koniec = czykoniec()

idealni()
input("Naciśnij dowolny klawisz aby zakończyć")
