import bottle
from datetime import datetime
from model import *



@bottle.get('/')
def osnovna_stran():
    return bottle.template('osnovna.tpl')

@bottle.post('/prijava_post/')
def prijava_post():
    bottle.redirect('/prijava/')



@bottle.get('/prijava/')
def prijava():
    return bottle.template('prijava.tpl')


@bottle.post('/registracija_post/')
def prijava_post():
    bottle.redirect('/registracija/')



@bottle.get('/registracija/')
def registracija():
    return bottle.template('registracija_osnova.tpl')

@bottle.post('/registracija/')
def registracija_preverjanje():
    novo_up_ime = bottle.request.forms.get('novo_up_ime')
    geslo = bottle.request.forms.get('geslo')
    geslo_pon = bottle.request.forms.get('geslo_ponovno')

    if geslo == geslo_pon:
        if veljavno_uporabniško_ime(novo_up_ime, geslo):
            dodaj_uporabnika(novo_up_ime, geslo)
            bottle.response.set_cookie("uporabnik", novo_up_ime, path='/')
            return bottle.redirect('/kokodajs')
        else:
            bottle.redirect('/registracija/neveljavno')
    else:
        bottle.redirect('/registracija/napaka')
        

@bottle.get('/registracija/napaka')
def registracija():
    return bottle.template('registracija_napaka.tpl')


@bottle.get('/registracija/neveljavno')
def registracija():
    return bottle.template('registracija_neveljavno.tpl')


@bottle.get('/prijava/')
def prijava():
    return bottle.template('prijava_osnovna.tpl')




@bottle.post('/prijava/')
def prijava_preverjanje():
    uporabnisko_ime = bottle.request.forms.get('uporabnisko_ime')
    geslo = bottle.request.forms.get('geslo')
    if veljavna_registracija(uporabnisko_ime, geslo):

        bottle.response.set_cookie("uporabnik", uporabnisko_ime, path='/')
        return bottle.redirect('/kokodajs')
    else:
        bottle.redirect('/registracija/neveljavno')




@bottle.get('/prijava/napaka')
def registracija():
    return bottle.template('prijava_napaka.tpl')




@bottle.get('/kokodajs')
def kokodajs():
    if not bottle.request.get_cookie('uporabnik'):
        bottle.redirect('/')
    else:
        a = bottle.request.get_cookie('uporabnik')
        return bottle.template('glavna_stran.tpl', uporabnik = a)



#@bottle.post('/registracija/')
#uporabnik se registrira



#@bottle.get('/osnovna/')
#osnovna stran uporabnika



#@bottle.get('/vsi/')
#uporabnik lahko bere vse kokodajse



#@bottle.get('/sledeči/')
#uporabnik lahko bere kokodajse ostalih uporabnikov, ki jim sledi




#@bottle.get('/sledenje/')
#uporabnik lahko izbere komu bo sledil



bottle.run(debug=True, reloader=True)
