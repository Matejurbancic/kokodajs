import bottle
from datetime import datetime
from model import *



@bottle.get('/')
def osnovna_stran():
    if bottle.request.cookies.uporabnik:
        bottle.redirect('/kokodajs')
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
    novo_up_ime = bottle.request.forms.novo_up_ime
    geslo = bottle.request.forms.geslo
    geslo_pon = bottle.request.forms.geslo_ponovno


    #if not novo_up_ime.isascii():
    #    return bottle.template('registracija.tpl', vrednost_napake=3)


    if geslo == geslo_pon:
        if veljavno_uporabnisko_ime(novo_up_ime, geslo):

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
    uporabnisko_ime = bottle.request.forms.uporabnisko_ime
    geslo = bottle.request.forms.geslo
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
    if not bottle.request.cookies.uporabnik:
        bottle.redirect('/')
    else:
        uporabnisko_ime = bottle.request.cookies.uporabnik
        #print(uporabnisko_ime)
        vsi_kokodajsi = preberi_datoteko(kokodajsi_datoteka)['kokodajsi']
        for uporabnik in preberi_datoteko(uporabniki_datoteka)['uporabniki']:
            if uporabnik['uporabnisko_ime'] == uporabnisko_ime:
                uporabnik_niz = uporabnik

        return bottle.template('doma.tpl', uporabnik = uporabnisko_ime, napaka=0, kokodajsi=vsi_kokodajsi, uporabnik_niz=uporabnik_niz)


@bottle.post('/kokodajs')
def nov_kokodajs():
    kokodajs_tekst = bottle.request.forms.kokodajs
    uporabnisko_ime = bottle.request.cookies.uporabnik
    cas_kokodajsa = str(datetime.now())[:-7]




    if len(kokodajs_tekst) > 140:
        vsi_kokodajsi = preberi_datoteko(kokodajsi_datoteka)['kokodajsi']
        for uporabnik in preberi_datoteko(uporabniki_datoteka)['uporabniki']:
            if uporabnik['uporabnisko_ime'] == uporabnisko_ime:
                uporabnik_string = uporabnik

        return bottle.template('doma.tpl', uporabnik = uporabnisko_ime, napaka=1, uporabnik_niz=uporabnik_string, kokodajsi=vsi_kokodajsi)
        
    else:
        dodaj_kokodajs(kokodajs_tekst, uporabnisko_ime, cas_kokodajsa)
        bottle.redirect('/kokodajs')


@bottle.post('/kokodajs_vseckanje')
def vseckanje():
    uporabnisko_ime = bottle.request.cookies.uporabnik
    kokodajs_vseckan = bottle.request.forms.vsec_mi_je
    dodaj_vsecek(kokodajs_vseckan, uporabnisko_ime, kokodajsi_datoteka)
    bottle.redirect('/kokodajs')

@bottle.post('/kokodajs_vseckanje_vsi_kokodajsi')
def vseckanje():
    uporabnisko_ime = bottle.request.cookies.uporabnik
    kokodajs_vseckan = bottle.request.forms.vsec_mi_je
    dodaj_vsecek(kokodajs_vseckan, uporabnisko_ime, kokodajsi_datoteka)
    bottle.redirect('/vsi_kokodajsi')



    

@bottle.get('/ne_sledeci')
def vsi_ne_sledeci():
    if not bottle.request.cookies.uporabnik:
        bottle.redirect('/')
    trenutno_up_ime = bottle.request.cookies.uporabnik
    for uporabnik in preberi_datoteko(uporabniki_datoteka)['uporabniki']:
        if trenutno_up_ime == uporabnik['uporabnisko_ime']:
            t_uporabnik = uporabnik
            return bottle.template('ne_sledeci.tpl', uporabniki=preberi_datoteko(uporabniki_datoteka)['uporabniki'], trenutni_uporabnik=t_uporabnik)



@bottle.post('/ne_sledeci')
def dodaj_sledenje():
    t_uporabnik = bottle.request.cookies.uporabnik
    sledeci_uporabnik = bottle.request.forms.sledeci_uporabnik
    dodaj_sledilca(t_uporabnik, sledeci_uporabnik, uporabniki_datoteka)
    bottle.redirect('/ne_sledeci')




@bottle.get('/sledeci')
def vsi_sledeci():
    if not bottle.request.cookies.uporabnik:
        bottle.redirect('/')
    trenutno_up_ime = bottle.request.cookies.uporabnik

    for uporabnik in preberi_datoteko(uporabniki_datoteka)['uporabniki']:
        if trenutno_up_ime == uporabnik['uporabnisko_ime']:
            t_uporabnik = uporabnik
            return bottle.template('sledeci.tpl', uporabniki=preberi_datoteko(uporabniki_datoteka)['uporabniki'], trenutni_uporabnik=t_uporabnik)



@bottle.post('/sledeci')
def dodaj_sledenje():
    t_uporabnik = bottle.request.cookies.uporabnik
    sledeci_uporabnik = bottle.request.forms.ne_sledeci_uporabnik
    odstrani_sledilca(t_uporabnik, sledeci_uporabnik, uporabniki_datoteka)
    bottle.redirect('/sledeci')



@bottle.get('/vsi_kokodajsi')
def kokodajs():
    if not bottle.request.cookies.uporabnik:
        bottle.redirect('/')
    else:
        uporabnisko_ime = bottle.request.cookies.uporabnik
        vsi_kokodajsi = preberi_datoteko(kokodajsi_datoteka)['kokodajsi']
        print(len(vsi_kokodajsi))
        return bottle.template('vsi_kokodajsi.tpl', kokodajsi=vsi_kokodajsi)



@bottle.get('/odjava')
def odjava():
    bottle.response.delete_cookie("uporabnik")
    bottle.redirect('/')
























bottle.run(debug=True, reloader=True)
