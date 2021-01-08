%rebase("glavna_stran.tpl")

<div class="container">
      
    
    <h4><center>Živijo {{uporabnik}}!</center></h4>
    <h7>Napiši kokodajs: max 140 znakov</h7>

    <center>
      <div class="container">
      <form action="/kokodajs" method="post">
        <div class="input-group">
            <span class="input-group-text"></span>
            <textarea class="form-control" aria-label="With textarea" name="kokodajs" rows="2" cols="40"></textarea>
            <input class="btn btn-primary" type="submit" value="kokodajsni">
        </div>
      </form>
    
      </div>
    </center>
    %if napaka:
    <p style="color:red"><b>Oddani kokodajs je predolg!</b></p>
    %end
    <br>
    <h7>Tvoji kokodajsi in kokodajsi oseb, ki jim slediš:</h7>

</div>