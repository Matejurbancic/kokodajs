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
      %if napaka == 1:
        <p style="color:red"><b>Oddani kokodajs je predolg!</b></p>
      %elif napaka == 2:
        <p style="color:red"><b>Kokodajs lahko vsebuje le ASCII znake</b></p>
      %end
        <br>

      <h7>Tvoji kokodajsi in kokodajsi oseb, ki jim slediš:</h7>

      %for indeks in range(len(kokodajsi.seznam) - 1, -1, -1):
       % if kokodajsi.seznam[indeks].uporabnik in uporabnik_objekt.sledeci or  kokodajsi.seznam[indeks].uporabnik == uporabnik:    
    
    <ul class="list-group">
      <li class="list-group-item active" aria-current="true"><p style="text-align:left;">
            {{kokodajsi.seznam[indeks].uporabnik}}
          <span style="float:right;">
                {{kokodajsi.seznam[indeks].cas}}
          </span>
        </p>
      </li>

      <li class="list-group-item">{{kokodajsi.seznam[indeks].tekst}}
        <span style="float:right;">
            {{len(kokodajsi.seznam[indeks].vsecki)}} X všeč mi je 
          <form action="/kokodajs_vseckanje" method="POST"> 
            <input type="hidden" value="{{indeks}}" name="vsec_mi_je">
            <input class="btn btn-primary" type="submit" value="všeč mi je">
          </form>
        </span>
      </li>
    </ul>
      <br>
      %end
    %end

</div>
<br>








