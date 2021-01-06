import bottle
from datetime import datetime



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
    upime = bottle.request.forms.get('uporabnisko_ime')
    geslo = bottle.request.forms.get('geslo')
    geslo_pon = bottle.request.forms.get('geslo_ponovno')
    if geslo == geslo_pon:
        bottle.redirect('/')
    else:
        bottle.redirect('/registracija/napaka')
        

@bottle.get('/registracija/napaka')
def registracija():
    return bottle.template('registracija_napaka.tpl')




#@bottle.get('/registracija/')



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
