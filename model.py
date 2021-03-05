from datetime import datetime
import json
import os


uporabniki_datoteka = os.path.join("data", "uporabniki.json")

kokodajsi_datoteka = os.path.join("data", "kokodajsi.json")


class Seznam_objektov():

    def __init__(self, seznam):
        self.seznam = seznam

    def __repr__(self):
        return f"<Niz{self.seznam}>"

    @classmethod
    def iz_json(cls, json_datoteka):
        with open(json_datoteka, "r") as datoteka:
            vsebina_datoteke = json.load(datoteka)
            vsi_objekti = []
            for element in vsebina_datoteke:
                if json_datoteka == uporabniki_datoteka:
                    objekt = Uporabnik.iz_json(element)
                    vsi_objekti.append(objekt)
                elif json_datoteka == kokodajsi_datoteka:
                    objekt = Kokodajs.iz_json(element)
                    vsi_objekti.append(objekt)
            return cls(vsi_objekti)

    def v_json(self, json_datoteka):
        with open(json_datoteka, "w") as datoteka:
            seznam_slovarjev = []
            for objekt in self.seznam:
                seznam_slovarjev.append(objekt.v_json())
            json.dump(seznam_slovarjev, datoteka, indent=2)

    def dodaj_uporabnika(self, uporabnisko_ime, geslo):
        nov_uporabnik = Uporabnik(uporabnisko_ime, geslo, [], 0)
        self.seznam.append(nov_uporabnik)

    def veljavno_uporabnisko_ime(self, uporabnisko_ime):
        for uporabnik in self.seznam:
            if type(uporabnik) is Uporabnik:
                if uporabnik.uporabnisko_ime == uporabnisko_ime:
                    return False
            else:
                return print('Napaka')
        return True

    def veljavna_registracija(self, uporabnisko_ime, geslo):
        for uporabnik in self.seznam:
            if type(uporabnik) == Uporabnik:
                if uporabnik.uporabnisko_ime == uporabnisko_ime and uporabnik.geslo == geslo:
                    return True
        return False

    def dodaj_kokodajs(self, tekst_kokodajs, uporabnisko_ime, cas_kokodajsa):
        nov_kokodajs = Kokodajs(uporabnisko_ime, tekst_kokodajs, [], cas_kokodajsa)
        self.seznam.append(nov_kokodajs)

    def najdi_uporabnika(self, trenutni_uporabnik):
        for uporabnik in self.seznam:
            if trenutni_uporabnik == uporabnik.uporabnisko_ime:
                return uporabnik

    def najdi_kokodajs(self, iskani_kokodajs):
        for kokodajs in self.seznam:
            if iskani_kokodajs == kokodajs:
                return kokodajs


class Uporabnik():

    def __init__(self, uporabnisko_ime, geslo, sledeci, sledilci):
        self.uporabnisko_ime = uporabnisko_ime
        self.geslo = geslo
        self.sledeci = sledeci
        self.sledilci = sledilci

    def __repr__(self):
        return f'<Uporabnik { self.uporabnisko_ime }>'

    @classmethod
    def iz_json(cls, json_niz):
        json_slovar = json.loads(json_niz)
        return cls(**json_slovar)

    def kodiranje(self):
        return {"uporabnisko_ime": self.uporabnisko_ime,
                "geslo": self.geslo,
                "sledeci": self.sledeci,
                "sledilci": self.sledilci}

    def v_json(self):
        return json.dumps(self.kodiranje())

    def dodaj_sledilca(self, uporabnik_sledimo):
        self.sledeci = self.sledeci.append(uporabnik_sledimo)

    def odstrani_sledilca(self, uporabnik_ne_sledimo):
        self.sledeci = self.sledeci.remove(uporabnik_ne_sledimo)

    def povecaj_sledilce(self):
        self.sledilci += 1

    def zmanjsaj_sledilce(self):
        self.sledilci -= 1


class Kokodajs():

    def __init__(self, uporabnik, tekst, vsecki, cas):
        self.uporabnik = uporabnik
        self.tekst = tekst
        self.vsecki = vsecki
        self.cas = cas

    def __repr__(self):
        return f"Kokodajs({self.uporabnik}, {self.tekst}, {self.vsecki}, {self.cas})"

    @classmethod
    def iz_json(cls, json_niz):
        json_slovar = json.loads(json_niz)
        return cls(**json_slovar)

    def kodiranje(self):
        return {"uporabnik": self.uporabnik,
                "tekst": self.tekst,
                "vsecki": self.vsecki,
                "cas": self.cas}

    def v_json(self):
        return json.dumps(self.kodiranje())

    def dodaj_vsecek(self, uporabnisko_ime):
        self.vsecki = self.vsecki.append(uporabnisko_ime)

