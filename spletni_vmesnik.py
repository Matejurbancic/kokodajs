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

    uporabniki = Seznam_objektov.iz_json(uporabniki_datoteka)

    if geslo == geslo_pon:
        if uporabniki.veljavno_uporabnisko_ime(novo_up_ime):

            uporabniki.dodaj_uporabnika(novo_up_ime, geslo)

            uporabniki.v_json(uporabniki_datoteka)
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

    uporabniki = Seznam_objektov.iz_json(uporabniki_datoteka)

    if uporabniki.veljavna_registracija(uporabnisko_ime, geslo):

        bottle.response.set_cookie("uporabnik", uporabnisko_ime, path='/')
        return bottle.redirect('/kokodajs')
    else:
        return bottle.template('prijava.tpl', napaka=True)


@bottle.get('/kokodajs')
def kokodajs():
    if not bottle.request.cookies.uporabnik:
        bottle.redirect('/')
    else:
        uporabnisko_ime = bottle.request.cookies.uporabnik
        uporabniki = Seznam_objektov.iz_json(uporabniki_datoteka)
        trenutni_uporabnik = uporabniki.najdi_uporabnika(uporabnisko_ime)

        vsi_kokodajsi = Seznam_objektov.iz_json(kokodajsi_datoteka)
        return bottle.template('doma.tpl',
                               uporabnik=uporabnisko_ime,
                               napaka=0,
                               kokodajsi=vsi_kokodajsi,
                               uporabnik_objekt=trenutni_uporabnik)


@bottle.post('/kokodajs')
def nov_kokodajs():
    kokodajs_tekst = bottle.request.forms.kokodajs
    uporabnisko_ime = bottle.request.cookies.uporabnik
    cas_kokodajsa = str(datetime.now())[:-7]

    vsi_kokodajsi = Seznam_objektov.iz_json(kokodajsi_datoteka)
    vsi_uporabniki = Seznam_objektov.iz_json(uporabniki_datoteka)
    trenutni_uporabnik = vsi_uporabniki.najdi_uporabnika(uporabnisko_ime)

    if len(kokodajs_tekst) > 140:
        return bottle.template('doma.tpl',
                               uporabnik=uporabnisko_ime,
                               napaka=1,
                               uporabnik_niz=trenutni_uporabnik,
                               kokodajsi=vsi_kokodajsi)

    else:
        vsi_kokodajsi.dodaj_kokodajs(kokodajs_tekst,
                                     uporabnisko_ime, cas_kokodajsa)
        vsi_kokodajsi.v_json(kokodajsi_datoteka)
        bottle.redirect('/kokodajs')


@bottle.post('/kokodajs_vseckanje')
def vseckanje():
    uporabnisko_ime = bottle.request.cookies.uporabnik
    kokodajs_vseckan = bottle.request.forms.vsec_mi_je

    kokodajsi = Seznam_objektov.iz_json(kokodajsi_datoteka)

    for i in range(len(kokodajsi.seznam)):
        if str((kokodajsi.seznam[i].uporabnik, kokodajsi.seznam[i].tekst,
                kokodajsi.seznam[i].cas)) == kokodajs_vseckan:

            if uporabnisko_ime not in kokodajsi.seznam[i].vsecki:
                kokodajsi.seznam[i].vsecki.append(uporabnisko_ime)
                kokodajsi.v_json(kokodajsi_datoteka)
                break

    bottle.redirect('/kokodajs')


@bottle.post('/kokodajs_vseckanje_vsi_kokodajsi')
def vseckanje():
    uporabnisko_ime = bottle.request.cookies.uporabnik
    kokodajs_vseckan = bottle.request.forms.vsec_mi_je

    kokodajsi = Seznam_objektov.iz_json(kokodajsi_datoteka)

    for i in range(len(kokodajsi.seznam)):
        if str((kokodajsi.seznam[i].uporabnik, kokodajsi.seznam[i].tekst,
                kokodajsi.seznam[i].cas)) == kokodajs_vseckan:

            if uporabnisko_ime not in kokodajsi.seznam[i].vsecki:
                kokodajsi.seznam[i].vsecki.append(uporabnisko_ime)
                kokodajsi.v_json(kokodajsi_datoteka)
                break

    bottle.redirect('/vsi_kokodajsi')


@bottle.post('/ne_sledeci')
def dodaj_sledenje():
    trenutno_uporabnisko_ime = bottle.request.cookies.uporabnik
    sledeci_uporabnik = bottle.request.forms.sledeci_uporabnik

    uporabniki = Seznam_objektov.iz_json(uporabniki_datoteka)

    for i in range(len(uporabniki.seznam)):
        if uporabniki.seznam[i].uporabnisko_ime == sledeci_uporabnik:
            uporabniki.seznam[i].sledilci += 1

        if uporabniki.seznam[i].uporabnisko_ime == trenutno_uporabnisko_ime:
            uporabniki.seznam[i].sledeci.append(sledeci_uporabnik)

    uporabniki.v_json(uporabniki_datoteka)
    bottle.response.set_cookie("sledenje", 'sledim', path='/')
    
    bottle.redirect('/uporabniki')


@bottle.post('/sledeci')
def odstrani_sledenje():
    t_uporabnik = bottle.request.cookies.uporabnik
    sledeci_uporabnik = bottle.request.forms.ne_sledeci_uporabnik

    uporabniki = Seznam_objektov.iz_json(uporabniki_datoteka)

    for i in range(len(uporabniki.seznam)):
        if uporabniki.seznam[i].uporabnisko_ime == sledeci_uporabnik:
            print(uporabniki.seznam[i].sledilci)
            uporabniki.seznam[i].sledilci -= 1

        if uporabniki.seznam[i].uporabnisko_ime == t_uporabnik:
            uporabniki.seznam[i].sledeci.remove(sledeci_uporabnik)

    uporabniki.v_json(uporabniki_datoteka)
    bottle.response.set_cookie("sledenje", 'ne_sledim', path='/')
    bottle.redirect('/uporabniki')


@bottle.get('/vsi_kokodajsi')
def kokodajs():
    if not bottle.request.cookies.uporabnik:
        bottle.redirect('/')
    else:
        uporabnisko_ime = bottle.request.cookies.uporabnik
        vsi_kokodajsi = Seznam_objektov.iz_json(kokodajsi_datoteka)

        return bottle.template('vsi_kokodajsi.tpl', kokodajsi=vsi_kokodajsi)


@bottle.get('/uporabniki')
def uporabniki():
    if not bottle.request.cookies.uporabnik:
        bottle.redirect('/')
    trenutno_up_ime = bottle.request.cookies.uporabnik

    vsi_uporabniki = Seznam_objektov.iz_json(uporabniki_datoteka)

    t_uporabnik = vsi_uporabniki.najdi_uporabnika(trenutno_up_ime)
    if bottle.request.cookies.sledenje == 'sledim':
        bottle.response.delete_cookie("sledenje")
        return bottle.template('uporabniki.tpl',
                               uporabniki=vsi_uporabniki,
                               trenutni_uporabnik=t_uporabnik,
                               sledenje=False)
    else:
        bottle.response.delete_cookie("sledenje")
        return bottle.template('uporabniki.tpl',
                               uporabniki=vsi_uporabniki,
                               trenutni_uporabnik=t_uporabnik,
                               sledenje=True)
    

@bottle.post('/uporabniki')
def uporabniki_post():
    trenutno_up_ime = bottle.request.cookies.uporabnik

    vsi_uporabniki = Seznam_objektov.iz_json(uporabniki_datoteka)

    t_uporabnik = vsi_uporabniki.najdi_uporabnika(trenutno_up_ime)

    vrednost = bottle.request.forms.sledim

    if vrednost == 'sledim':
        return bottle.template('uporabniki.tpl',
                               uporabniki=vsi_uporabniki,
                               trenutni_uporabnik=t_uporabnik,
                               sledenje=True)
    elif vrednost == 'ne_sledim':
        return bottle.template('uporabniki.tpl',
                               uporabniki=vsi_uporabniki,
                               trenutni_uporabnik=t_uporabnik,
                               sledenje=False)


@bottle.get('/odjava')
def odjava():
    bottle.response.delete_cookie("uporabnik")
    bottle.redirect('/')


bottle.run(debug=True, reloader=True)
