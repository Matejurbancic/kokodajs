from datetime import datetime
import json
import os



uporabniki_datoteka = "uporabniki.json"

kokodajsi_datoteka = "kokodajsi.json"


def preberi_datoteko(json_datoteka):  #prebere json datoteko
    with open(json_datoteka, "r") as datoteka:
        vsebina_datoteke = json.load(datoteka)
        return vsebina_datoteke


def napisi_datoteko(vsebina_datoteke, json_datoteka):  #python kodo prenese nazaj v json datoteko
    with  open(json_datoteka, "w") as datoteka:
        json.dump(vsebina_datoteke, datoteka, indent=2)


def dodaj_uporabnika(uporabnisko_ime, geslo): # doda novega uporabnika v json
    prebrana_dat = preberi_datoteko(uporabniki_datoteka)
    nov_uporabnik = {"uporabnisko_ime": uporabnisko_ime, "geslo" : geslo, "sledeci" : [], "sledilci" : 0}
    prebrana_dat["uporabniki"].append(nov_uporabnik)
    napisi_datoteko(prebrana_dat, uporabniki_datoteka)



def veljavno_uporabniško_ime(novo_up_ime, geslo): #preveri ali je uporabniško ime v jsonu že zasedeno
    prebrana_dat = preberi_datoteko(uporabniki_datoteka)
    for uporabnik in prebrana_dat["uporabniki"]:
        if uporabnik["uporabnisko_ime"] == novo_up_ime:
            return False
    return True



def veljavna_registracija(uporabnisko_ime, geslo): # preveri če se uporabniško ime ujema z geslom
    prebrana_dat = preberi_datoteko(uporabniki_datoteka)
    for uporabnik in prebrana_dat["uporabniki"]:
        if uporabnik["uporabnisko_ime"] == uporabnisko_ime and uporabnik["geslo"] == geslo:
            return True
    return False

'''
def dodaj_kokodajs(tekst_kokodajs, uporabnisko_ime): # doda nov kokodajs v kokodajsi.json
    prebrana_dat = preberi_datoteko(kokodajsi_datoteka)
    nov_kokodajs = {"uporabnik": uporabnisko_ime, "tekst" : tekst_kokodajs, "vsecki" : 0}
    prebrana_dat["kokodajsi"].append(nov_kokodajs)
    napisi_datoteko(prebrana_dat, kokodajsi_datoteka)
'''





def dodaj_kokodajs(tekst_kokodajs, uporabnisko_ime, cas_kokodajsa): # doda nov kokodajs v kokodajsi.json
    prebrana_dat = preberi_datoteko(kokodajsi_datoteka)
    nov_kokodajs = {"uporabnik": uporabnisko_ime, "tekst" : tekst_kokodajs, "vsecki" : 0, "cas": cas_kokodajsa}
    prebrana_dat["kokodajsi"].append(nov_kokodajs)
    napisi_datoteko(prebrana_dat, kokodajsi_datoteka)




def dodaj_sledilca(trenutni_uporabnik, uporabnik_sledimo, json_datoteka):
    prebrana_dat = preberi_datoteko(json_datoteka)
    for uporabnik in prebrana_dat['uporabniki']:
        if uporabnik['uporabnisko_ime'] == trenutni_uporabnik:
            #print(uporabnik['uporabnisko_ime'])
            uporabnik['sledeci'].append(uporabnik_sledimo)
        if  uporabnik['uporabnisko_ime'] == uporabnik_sledimo:
            uporabnik['sledilci'] += 1
    
    napisi_datoteko(prebrana_dat, json_datoteka)

    
def odstrani_sledilca(trenutni_uporabnik, uporabnik_sledimo, json_datoteka):
    prebrana_dat = preberi_datoteko(json_datoteka)
    for uporabnik in prebrana_dat['uporabniki']:
        if uporabnik['uporabnisko_ime'] == trenutni_uporabnik:
            
            uporabnik['sledeci'].remove(uporabnik_sledimo)
        if  uporabnik['uporabnisko_ime'] == uporabnik_sledimo:
            uporabnik['sledilci'] -= 1

    napisi_datoteko(prebrana_dat, json_datoteka)



class Kokodajs():
    
    def __init__(self, besedilo, uporabnik):
        self.besedilo = besedilo
        self.uporabnik = uporabnik



class Uporabnik():

    def __init__(self, uporabnisko_ime, geslo, sledeci=[], ):
        self.uporabnisko_ime = uporabnisko_ime
        self.geslo = geslo
        self.sledeci = sledeci






