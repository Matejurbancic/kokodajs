from PIL import Image
from datetime import datetime
import json
import os



uporabniki_datoteka =  os.path.join("data", "uporabniki.json")
print(os.path.join("data", "uporabniki.json"))
kokodajsi_datoteka =  os.path.join("data", "kokodajsi.json")


def preberi_datoteko(json_datoteka):  #prebere json datoteko
    with open(json_datoteka, "r") as datoteka:
        vsebina_datoteke = json.load(datoteka)
        '''
        if json_datoteka == uporabniki_datoteka:
            dekodirana_vsebina = {'uporabniki': []}
            for uporabnik in vsebina_datoteke['uporabniki']:
                dekodiran_uporabnik = {}
                dekodiran_uporabnik['uporabnisko_ime'] = uporabnik['uporabnisko_ime']#.encode().decode()
                dekodiran_uporabnik['geslo'] = uporabnik['geslo']#.encode().decode()
                dekodiran_uporabnik['sledilci'] = uporabnik['sledilci']
                sledeci_dekodirani = []
                for up_ime in uporabnik['sledeci']:
                    sledeci_dekodirani.append(up_ime)#.encode().decode())
                dekodiran_uporabnik['sledeci'] = sledeci_dekodirani
                dekodirana_vsebina['uporabniki'].append(dekodiran_uporabnik)
        elif json_datoteka == kokodajsi_datoteka:
            dekodirana_vsebina = {'kokodajsi': []}
            for kokodajs in vsebina_datoteke['kokodajsi']:
                dekodiran_kokodajs = {}
                dekodiran_kokodajs['uporabnik'] = kokodajs['uporabnik']#.encode().decode()
                dekodiran_kokodajs['tekst'] = kokodajs['tekst']#.encode().decode()
                dekodiran_kokodajs['cas'] = kokodajs['cas']
                vsecki_dekodirani = []
                for up_ime in kokodajs['vsecki']:
                    vsecki_dekodirani.append(up_ime)#.encode().decode())
                dekodiran_kokodajs['vsecki'] = vsecki_dekodirani
                dekodirana_vsebina['kokodajsi'].append(dekodiran_kokodajs)
        '''

        return vsebina_datoteke


def napisi_datoteko(vsebina_datoteke, json_datoteka):  #python kodo prenese nazaj v json datoteko

    '''
    if json_datoteka == uporabniki_datoteka:
        kodirana_vsebina = {'uporabniki': []}
        for uporabnik in vsebina_datoteke['uporabniki']:
            kodiran_uporabnik = {}
            kodiran_uporabnik['uporabnisko_ime'] = uporabnik['uporabnisko_ime'].encode().decode()
            kodiran_uporabnik['geslo'] = uporabnik['geslo'].encode().decode()
            kodiran_uporabnik['sledilci'] = uporabnik['sledilci']
            sledeci_kodirani = []
            for up_ime in uporabnik['sledeci']:
                sledeci_kodirani.append(up_ime.encode().decode())
            kodiran_uporabnik['sledeci'] = sledeci_kodirani
            kodirana_vsebina['uporabniki'].append(kodiran_uporabnik)
    elif json_datoteka == kokodajsi_datoteka:
        kodirana_vsebina = {'kokodajsi': []}
        for kokodajs in vsebina_datoteke['kokodajsi']:
            kodiran_kokodajs = {}
            kodiran_kokodajs['uporabnik'] = kokodajs['uporabnik'].encode().decode()
            kodiran_kokodajs['tekst'] = kokodajs['tekst'].encode().decode()
            kodiran_kokodajs['cas'] = kokodajs['cas']
            vsecki_kodirani = []
            for up_ime in kokodajs['vsecki']:
                vsecki_kodirani.append(up_ime.encode().decode())
            kodiran_kokodajs['vsecki'] = vsecki_kodirani
            kodirana_vsebina['kokodajsi'].append(kodiran_kokodajs)
    '''
    with  open(json_datoteka, "w") as datoteka:
        json.dump(vsebina_datoteke, datoteka, indent=2)


def dodaj_uporabnika(uporabnisko_ime, geslo): # doda novega uporabnika v json
    prebrana_dat = preberi_datoteko(uporabniki_datoteka)
    nov_uporabnik = {"uporabnisko_ime": uporabnisko_ime, "geslo" : geslo, "sledeci" : [], "sledilci" : 0}
    prebrana_dat["uporabniki"].append(nov_uporabnik)
    napisi_datoteko(prebrana_dat, uporabniki_datoteka)



def veljavno_uporabnisko_ime(novo_up_ime, geslo): #preveri ali je uporabniško ime v jsonu že zasedeno
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
    nov_kokodajs = {"uporabnik": uporabnisko_ime, "tekst" : tekst_kokodajs, "vsecki" : [], "cas": cas_kokodajsa}
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



def dodaj_vsecek(kokodajs, uporabnisko_ime, json_datoteka):
    kokodajsi = preberi_datoteko(json_datoteka)
    for koko in kokodajsi['kokodajsi']:
        if str(koko) == kokodajs:
            print(koko)
            if uporabnisko_ime not in koko['vsecki']:
                koko['vsecki'].append(uporabnisko_ime)
    napisi_datoteko(kokodajsi, json_datoteka=json_datoteka)








