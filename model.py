from datetime import datetime
import json

class Kokodajs():
    
    def __init__(self, besedilo, uporabnik):
        self.besedilo = besedilo
        self.uporabnik = uporabnik



class Uporabnik():

    def __init__(self, uporabnisko_ime, geslo, sledeci=[], ):
        self.uporabnisko_ime = uporabnisko_ime
        self.geslo = geslo
        self.sledeci = sledeci
