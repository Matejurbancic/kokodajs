from datetime import datetime
import json
import os

json_datoteka = "uporabniki.json"



def preberi_datoteko():
    with open(json_datoteka, "r") as datoteka:
        vsebina_datoteke = json.load(datoteka)
        return vsebina_datoteke


def napisi_datoteko(vsebina_datoteke):
    with  open(json_datoteka, "w") as datoteka:
        json.dump(vsebina_datoteke, datoteka, indent=2)


def dodaj_uporabnika(uporabnisko_ime, geslo):
    prebrana_dat = preberi_datoteko()
    nov_uporabnik = {"uporabnisko_ime": uporabnisko_ime, "geslo" : geslo, "kokodajsi" : []}
    prebrana_dat["uporabniki"].append(nov_uporabnik)
    napisi_datoteko(prebrana_dat)



def veljavno_uporabniško_ime(novo_up_ime, geslo):
    prebrana_dat = preberi_datoteko()
    for uporabnik in prebrana_dat["uporabniki"]:
        if uporabnik["uporabnisko_ime"] == novo_up_ime:
            return False
    return True









class Kokodajs():
    
    def __init__(self, besedilo, uporabnik):
        self.besedilo = besedilo
        self.uporabnik = uporabnik



class Uporabnik():

    def __init__(self, uporabnisko_ime, geslo, sledeci=[], ):
        self.uporabnisko_ime = uporabnisko_ime
        self.geslo = geslo
        self.sledeci = sledeci
