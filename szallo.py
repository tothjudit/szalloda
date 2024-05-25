from datetime import datetime

class Szoba:
    def __init__(self, szobsz, price):
        self.szobsz = szobsz
        self.price = price

class EgyagyasSzoba(Szoba):
    def __init__(self, szobsz, bath):
        super().__init__(szobsz, 20000)
        self.bath = bath

class KetagyasSzoba(Szoba):
    def __init__(self, szobsz, extra):
        super().__init__(szobsz, 35000)
        self.extra = extra

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.fgs_ok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    
    def fgs(self, szobsz, datum):
        for fgs in self.fgs_ok:
            if fgs.szoba.szobsz == szobsz and fgs.datum == datum:
                print("A szoba már foglalt ezen a napon. Válasszon másik szobát vagy dátumot!")
                return
        for szoba in self.szobak:
            if szoba.szobsz == szobsz:
                self.fgs_ok.append(Foglalas(szoba, datum))
                print("Sikeres foglalás!")
                return szoba.price
        print("A megadott szobaszám nem létezik!")

    def lemond(self, szobsz, datum):
        for fgs in self.fgs_ok:
            if fgs.szoba.szobsz == szobsz and fgs.datum == datum:
                self.fgs_ok.remove(fgs)
                return True
        return False
    
    def list_fgs_ok(self):
        for fgs in self.fgs_ok:
            print(f"Szoba: {fgs.szoba.szobsz}, Időpont: {fgs.datum}")

hotel = Szalloda("Hotel")

hotel.add_szoba(EgyagyasSzoba("11","Bath"))
hotel.add_szoba(EgyagyasSzoba("12","Shower"))
hotel.add_szoba(KetagyasSzoba("13","Bar"))
hotel.add_szoba(KetagyasSzoba("14","Balcony"))

hotel.fgs("11", datetime(2024, 5, 20))
hotel.fgs("12", datetime(2024, 5, 10))
hotel.fgs("13", datetime(2024, 5, 16))
hotel.fgs("14", datetime(2024, 5, 15))
hotel.fgs("12", datetime(2024, 5, 20))

while True:

    print("Válassz a lehetőségek közül:")
    print("1. Szoba foglalása")
    print("2. Foglalás lemondása")
    print("3. Foglalások listázása")
    print("4. Szobák listázása")
    print("5. Kilépés")
    case = input("Melyik lehetőséget választod? (1/2/3/4/5): ")

    if case == "1":
        szobsz = input("Add meg a szoba számát: ")
        datum = input("Add meg a dátumot (ÉÉÉÉ-HH-NN, csak egy napot): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            if datum < datetime.now():
                print("Hibás dátum! A foglalás csak jövőbeni időpontra lehetséges.")

            else:
                price = hotel.fgs(szobsz, datum)
                if price:
                    print(f"Sikeres foglalás! Az ár: {price} Ft")
                else:
                    print("Hibás szobaszám!")

        except ValueError:
            print("Hibás dátum formátum!")

    elif case == "2":
        szobsz = input("Add meg a lemondandani kívánt szoba számát: ")
        datum = input("Add meg a lemondandani kívánt dátumot (ÉÉÉÉ-HH-NN): ")
        try:
            datum = datetime.strptime(datum, "%Y-%m-%d")
            siker = hotel.lemond(szobsz, datum)
            if siker:
                print("Sikeresen lemondva!")
            else:
                print("Nincs ilyen foglalás!")
                
        except ValueError:
            print("Hibás dátum formátum!")

    elif case == "3":
        hotel.list_fgs_ok()

    elif case == "4":
            print("Szobák száma:")
            print(len(hotel.szobak))
            print("Egyágyas szobák:")
            for szoba in hotel.szobak:
                if isinstance(szoba, EgyagyasSzoba):
                    print(f"Szobaszám: {szoba.szobsz}, Ár: {szoba.price} Ft, (Fürdő: {szoba.bath})")
            print("Kétágyas szobák:")
            for szoba in hotel.szobak:
                if isinstance(szoba, KetagyasSzoba):
                    print(f"Szobaszám: {szoba.szobsz}, Ár: {szoba.price} Ft, (Extra: {szoba.extra})")

    elif case == "5":
        break
    else:
        print("Hibás választás!")