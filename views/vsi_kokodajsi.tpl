%rebase("glavna_stran.tpl")



<div class="container">
      
    
    <h4><center>Seznam vseh kokodajsev</center></h4>
    
    <br>
    
    %for indeks in range(len(kokodajsi.seznam) - 1, -1, -1):
     <ul class="list-group">
    <li class="list-group-item active" aria-current="true">
        <p style="text-align:left;">
                {{kokodajsi.seznam[indeks].uporabnik}}
            <span style="float:right;">
                {{kokodajsi.seznam[indeks].cas}}
            </span>
        </p>
    </li>
        <li class="list-group-item">{{kokodajsi.seznam[indeks].tekst}}
            <span style="float:right;">
                {{len(kokodajsi.seznam[indeks].vsecki)}} X všeč mi je
                <form action="/kokodajs_vseckanje_vsi_kokodajsi" method="POST"> 
                    <input type="hidden" value="{{ (kokodajsi.seznam[indeks].uporabnik, kokodajsi.seznam[indeks].tekst, kokodajsi.seznam[indeks].cas) }}" name="vsec_mi_je">
                    <input class="btn btn-primary" type="submit" value="všeč mi je">
                </form>
            </span>
        </li>
    </ul>
    <br>
    %end
    

</div>



