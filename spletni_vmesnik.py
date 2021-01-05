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
    return bottle.template('poskus.tpl')



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
