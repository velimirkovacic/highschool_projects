from datetime import *



def uhr(s):
    s = s.replace("[", "ć").replace("]", "č").replace("|", "đ")
    return s.replace('?', "Ć").replace("#", "Č").replace("&", "Đ")
def izhr(s):
    s = s.replace('ć', "[").replace("č", "]").replace("đ", "|")
    return s.replace('Ć', "?").replace("Č", "#").replace("Đ", "&")


class Knjiga:
    def __init__(self, p):
        self.id = p[0]
        self.naslov = uhr(p[1].replace("_", " "))
        self.autorIme = uhr(p[2].replace("_", " "))
        self.autorPrez = uhr(p[3].replace("_", " "))
        self.knjizevnost = uhr(p[4])
        self.vrsta = uhr(p[5])
        self.ukupno = p[6]
        self.posudeno = p[7:]
        
    def posudi(self, os):
        self.posudeno.append(os)
        
    def vrati(self, os):
        self.posudeno.remove(os)
        
    def __str__(self):
        st = "{:7} {:33} {:33} {:13} {:15} {:5}".format(self.id, self.naslov, self.autorIme + " " + self.autorPrez, self.knjizevnost, self.vrsta, str(int(self.ukupno)-len(self.posudeno))).replace("_", " ")
        return st

    def save(self):
        st = "{}/{}/{}/{}/{}/{}/{}/".format(self.id, self.naslov, self.autorIme, self.autorPrez, self.knjizevnost, self.vrsta, self.ukupno).replace(" ", "_")
        if(len(self.posudeno) > 0):
            for i in self.posudeno:
                st += "{}/".format(i)
        return izhr(st)


class Datum(date):
    def __init__(self, y, m, d):
        super().__init__()
        return
    
    def __str__(self):
        return "{}.{}.{}.".format(str(self.day), str(self.month), str(self.year))


class Osoba:
    def __init__(self, p):
        self.id = p[0]
        self.ime = uhr(p[1]).replace("_", " ")
        self.prezime = uhr(p[2]).replace("_", " ")
        self.rod = Datum(int(p[3]), int(p[4]), int(p[5]))
        self.posudio = p[6:]
        
    def vrati(self, knj):
        self.posudio.remove(knj)
        
    def __str__(self):
        st = "{:7} {:15} {:15} {:10}".format(self.id, self.ime, self.prezime, self.rod.__str__())
        return st
    
    def save(self):
        st = "{}/{}/{}/{}/{}/{}/".format(self.id, self.ime, self.prezime, self.rod.year, self.rod.month, self.rod.day).replace(" ", "_")
        if(len(self.posudio) > 0):
            for i in self.posudio:
                st += "{}/".format(i)
        return izhr(st)


def update(s, n):
    if(s == "popisKnjiga.txt"):
        global nK
        if n >= nK: nK = n+1
    else:
        global nC
        if n >= nC: nC = n+1


def unos(s):
    dat = open(s, "r")
    popis = []
    line = dat.readline()
    podaci = []
    
    while(line != ""):
        podaci = line.split("/")
        podaci = podaci[:len(podaci)-1]
        update(s, int(podaci[0][1:]))
        if(s == "popisKnjiga.txt"):
            popis.append(Knjiga(podaci))
        else:
            popis.append(Osoba(podaci))
            
        podaci *=0
        line = dat.readline()
    dat.close()
    return popis


def startup():
    return unos("popisKnjiga.txt"), unos("popisClanova.txt")


def ispis_knjiga(opt):
    global popisKnjiga
    tmp = popisKnjiga[:]
    print("\n{:7} {:33} {:33} {:13} {:15} {:5} \n".format("ID:", "Naslov:", "Autor:", "Književnost:", "Vrsta:", "Dostupno:"),"-"*114, sep="")
    if(opt == 2): tmp = sorted(popisKnjiga, key = lambda p : p.naslov)
    elif(opt == 3): tmp = sorted(popisKnjiga, key = lambda p : p.autorPrez)
    for i in tmp:
        print(i)

        
def ispis_clanova(opt):
    print("\n{:7} {:15} {:15} {:10} \n".format("ID:", "Ime:", "Prezime:", "Datum rođenja:"), "-"*57, sep="")
    global popisClanova
    tmp = popisClanova[:]
    if(opt == 2): tmp = sorted(popisClanova, key = lambda p : p.prezime)
    elif(opt == 3): tmp = sorted(popisClanova, key = lambda p : p.rod)
    for i in tmp:
        print(i)


def nova_knjiga():
    p = []
    p.append(input("Naslov: "))
    p.append(input("Ime autora: "))
    p.append(input("Prezime autora: "))
    p.append(input("Književnost: "))
    p.append(input("Vrsta: "))
    p.append(input("Broj primjeraka: "))

    global nK
    iden = str(nK)
    while(len(iden) < 4): iden = '0'+iden
    iden = 'k'+iden
    nK+=1
    global popisKnjiga
    popisKnjiga.append(Knjiga([iden]+p+[]))


def novi_clan():
    p = []
    p.append(input("Ime: "))
    p.append(input("Prezime: "))
    p.extend(reversed(input("Datum rođenja (npr. 1.1.2002.): ").split('.')[:3]))
    
    global nC
    iden = str(nC)
    while(len(iden) < 4): iden = '0'+iden
    iden = 'c'+iden
    nC+=1
    global popisClanova
    popisClanova.append(Osoba([iden]+p+[]))


def pohrana():
    dat = open("PopisKnjiga.txt", "w")
    global popisKnjiga
    for i in popisKnjiga:
        dat.write(i.save()+"\n")
    dat.close()
    dat = open("PopisClanova.txt", "w")
    global popisClanova
    for i in popisClanova:
        dat.write(i.save()+"\n")
    dat.close()


def odabir(izbor):
    iz = input('\nOdabir: ')
    while iz not in izbor:
        iz = input('Odabir: ')
    return int(iz)


def pronadi(f, popis):
    lo, hi = 0, len(popis)-1
    while(lo < hi):
        mid = (lo+hi)//2
        if(f == popis[mid].id): return mid
        elif(f > popis[mid].id): lo = mid+1
        else: hi = mid
    return lo


def posudba_vracanje(x, clanID, knjigaID):
    global popisKnjiga, popisClanova

    clanIND = pronadi(clanID, popisClanova)
    knjigaIND = pronadi(knjigaID, popisKnjiga)

    if(clanID == popisClanova[clanIND].id and knjigaID == popisKnjiga[knjigaIND].id):
        if(x == 0):
            if(int(popisKnjiga[knjigaIND].ukupno) - len(popisKnjiga[knjigaIND].posudeno) < 1):
                print("\nNije dostupan ni jedan primjerak ove knjige")
                return

            if(len(popisClanova[clanIND].posudio) == 4):
                print("\nNije moguće posuditi više od 4 knjige")
                return

            popisKnjiga[knjigaIND].posudeno.append(clanID)
            popisClanova[clanIND].posudio.append(knjigaID)
            print("\n", popisClanova[clanIND].ime + " "+popisClanova[clanIND].prezime," je posudio/la ", popisKnjiga[knjigaIND].naslov, sep="")
        else:     
            popisKnjiga[knjigaIND].posudeno.remove(clanID)
            popisClanova[clanIND].posudio.remove(knjigaID)
            print("\n", popisClanova[clanIND].ime.replace("_", " ") + " "+popisClanova[clanIND].prezime," je vratio/la ", popisKnjiga[knjigaIND].naslov, sep="")

    else: print(("\nNe postoji knjiga i/ili član s ovim ID-jem"))


def radnje_clana(x):
    ident = input("ID člana: ")
    indeks = pronadi(ident, popisClanova)
    
    if(ident == popisClanova[indeks].id):
        if(x == 0):
            print("\n", ident, " je obrisan", sep="")
            for i in popisClanova[indeks].posudio:
                posudba_vracanje(1, ident, i)
            popisClanova.pop(indeks)
    
        else:
            k = popisClanova[indeks]
            print("{:15} {}".format("Ime:", k.ime))
            print("{:15} {}".format("Prezime:", k.prezime))
            print("{:15} {}".format("Rođen/a:", k.rod))
            print("{:15} {}".format("Posuđeno:", len(k.posudio)))
            if(len(k.posudio) > 0):
                print("{:15} {} ({})".format("Posudio:", k.posudio[0], popisKnjiga[pronadi(k.posudio[0], popisKnjiga)].naslov))
                for i in k.posudio[1:]:
                    print(" "*16, i, " (", popisKnjiga[pronadi(i, popisKnjiga)].naslov, ")", sep = "")
        
    else: print("\nNe postoji član s ovim ID-jem")


def radnje_knjige(x):
    ident = input("ID knjige: ")
    indeks = pronadi(ident, popisKnjiga)
    
    if(ident == popisKnjiga[indeks].id):
        if(x == 0):
            print("\n", ident, " je obrisan", sep="")
            for i in popisKnjiga[indeks].posudeno:
                posudba_vracanje(1, ident, i)
            popisKnjiga.pop(indeks)
        else:
            k = popisKnjiga[indeks]
            print("{:15} {}".format("Naslov:", k.naslov))
            print("{:15} {}".format("Autor:", k.autorIme + " " + k.autorPrez))
            print("{:15} {}".format("Vrsta:", k.vrsta))
            print("{:15} {}".format("Književnost:", k.knjizevnost))
            print("{:15} {}".format("Ukupno:", k.ukupno))
            print("{:15} {}".format("Posuđeno:", len(k.posudeno)))
            if(len(k.posudeno) > 0):
                print("{:15} {} ({})".format("Posudili:", k.posudeno[0], popisClanova[pronadi(k.posudeno[0], popisClanova)].prezime))
                for i in k.posudeno[1:]:
                    print(" "*16, i, " (", popisClanova[pronadi(i, popisClanova)].prezime, ")", sep = "")
    else: print("\nNe postoji knjiga s ovim ID-jem")


def main_menu():
    iz = -1
    while(iz != 0):
        print("\nGLAVNI IZBORNIK")
        print("1 - Unos (novo)")
        print("2 - Brisanje")
        print("3 - Posudi knjigu")
        print("4 - Vrati knjigu")
        print("5 - Ispiši")
        print("6 - Informacije")
        print("0 - Izlaz")
        iz = odabir(["0", "1", "2", "3", "4", "5", "6"])

        if(iz == 1):
            x = -1
            while(x != 3):
                print("\nIZBORNIK UNOSA\n1 - Nova knjiga\n2 - Novi član\n3 - Povrtak na glavni izbornik")
                x = odabir(["1", "2", "3"])
                if(x == 1): nova_knjiga()
                elif(x == 2): novi_clan()
                
        elif(iz == 2):
            x = -1
            while(x != 3):
                print("\nIZBORNIK BRISANJA\n1 - Brisanje knjige\n2 - Brisanje člana\n3 - Povrtak na glavni izbornik")
                x = odabir(["1", "2", "3"])
                if(x == 1): radnje_knjige(0)
                elif(x == 2): radnje_clana(0)

        elif(iz == 3):
            clanID = input("ID člana: ")
            knjigaID = input("ID knjige: ")
            posudba_vracanje(0, clanID, knjigaID)

        elif(iz == 4):
            clanID = input("ID člana: ")
            knjigaID = input("ID knjige: ")
            posudba_vracanje(1, clanID, knjigaID)
            
        elif(iz == 5):
            x = -1
            while(x != 3):
                print("\nIZBORNIK ISPISA\n1 - Ispis knjiga\n2 - Ispis članova\n3 - Povrtak na glavni izbornik")
                x = odabir(["1", "2", "3"])
                if(x == 1):
                    print("\nIZBORNIK ISPISA KNJIGA\n1 - Po ID-jevima\n2 - Po naslovima\n3 - Po prezimenima autora")
                    y = odabir(["1", "2", "3"])
                    ispis_knjiga(y)
                    
                elif(x == 2):
                    print("\nIZBORNIK ISPISA ČLANOVA\n1 - Po ID-jevima\n2 - Po prezimenima\n3 - Po datumu rođenja")
                    y = odabir(["1", "2", "3"])
                    ispis_clanova(y)

        elif(iz == 6):
            x = -1
            while(x != 3):
                print("\nINFO IZBORNIK\n1 - Informacije o knjizi\n2 - Informacije o članu\n3 - Povrtak na glavni izbornik")
                x = odabir(["1", "2", "3"])
                if(x == 1): radnje_knjige(1)
                elif(x == 2): radnje_clana(1)
    
        pohrana()


nC = 1
nK = 1

popisKnjiga, popisClanova = startup()

main_menu()
