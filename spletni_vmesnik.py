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
    return bottle.template('registracija.tpl', vrednost_napake=0)

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
            return bottle.template('registracija.tpl', vrednost_napake=1)
    else:
        return bottle.template('registracija.tpl', vrednost_napake=2)
        




@bottle.get('/prijava/')
def prijava():
    return bottle.template('prijava.tpl', napaka=False)




@bottle.post('/prijava/')
def prijava_preverjanje():
    uporabnisko_ime = bottle.request.forms.get('uporabnisko_ime')
    geslo = bottle.request.forms.get('geslo')
    if veljavna_registracija(uporabnisko_ime, geslo):

        bottle.response.set_cookie("uporabnik", uporabnisko_ime, path='/')
        return bottle.redirect('/kokodajs')
    else:
        return bottle.template('prijava.tpl', napaka=True)




#@bottle.get('/prijava/napaka')
#def registracija():
#    return bottle.template('prijava_napaka.tpl')




@bottle.get('/kokodajs')
def kokodajs():
    if not bottle.request.get_cookie('uporabnik'):
        bottle.redirect('/')
    else:
        uporabnisko_ime = bottle.request.get_cookie('uporabnik')
        return bottle.template('doma.tpl', uporabnik = uporabnisko_ime, napaka=False)


@bottle.post('/kokodajs')
def nov_kokodajs():
    kokodajs_tekst = bottle.request.forms.get('kokodajs')
    uporabnisko_ime = bottle.request.get_cookie('uporabnik')
    cas_kokodajsa = str(datetime.now())

    if len(kokodajs_tekst) > 140:
        return bottle.template('doma.tpl', uporabnik=uporabnisko_ime, napaka=True)
    else:
        dodaj_kokodajs(kokodajs_tekst, uporabnisko_ime, cas_kokodajsa)
        return bottle.template('doma.tpl', uporabnik = uporabnisko_ime, napaka=False)



    

@bottle.get('/ne_sledeci')
def vsi_ne_sledeci():
    if not bottle.request.get_cookie('uporabnik'):
        bottle.redirect('/')
    trenutno_up_ime = bottle.request.get_cookie('uporabnik')
    for uporabnik in preberi_datoteko(uporabniki_datoteka)['uporabniki']:
        if trenutno_up_ime == uporabnik['uporabnisko_ime']:
            t_uporabnik = uporabnik
            return bottle.template('ne_sledeci.tpl', uporabniki=preberi_datoteko(uporabniki_datoteka)['uporabniki'], trenutni_uporabnik=t_uporabnik)



@bottle.post('/ne_sledeci')
def dodaj_sledenje():
    t_uporabnik = bottle.request.get_cookie('uporabnik')
    sledeci_uporabnik = bottle.request.forms['sledeci_uporabnik']
    dodaj_sledilca(t_uporabnik, sledeci_uporabnik, uporabniki_datoteka)
    bottle.redirect('/ne_sledeci')




@bottle.get('/sledeci')
def vsi_sledeci():
    if not bottle.request.get_cookie('uporabnik'):
        bottle.redirect('/')
    trenutno_up_ime = bottle.request.get_cookie('uporabnik')
    
    for uporabnik in preberi_datoteko(uporabniki_datoteka)['uporabniki']:
        if trenutno_up_ime == uporabnik['uporabnisko_ime']:
            t_uporabnik = uporabnik
            return bottle.template('sledeci.tpl', uporabniki=preberi_datoteko(uporabniki_datoteka)['uporabniki'], trenutni_uporabnik=t_uporabnik)





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
