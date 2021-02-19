%rebase("glavna_stran.tpl")



<div class="container">
      
    
    <h4><center>Seznam vseh kokodajsev</center></h4>
    
    <br>
    
    %for indeks in range(len(kokodajsi) - 1, -1, -1):
     <ul class="list-group">
    <li class="list-group-item active" aria-current="true">
        <p style="text-align:left;">
                {{kokodajsi[indeks]['uporabnik']}}
            <span style="float:right;">
                {{kokodajsi[indeks]['cas']}}
            </span>
        </p>
    </li>
        <li class="list-group-item">{{kokodajsi[indeks]['tekst']}}
            <span style="float:right;">
                {{len(kokodajsi[indeks]['vsecki'])}} X všeč mi je
                <form action="/kokodajs_vseckanje_vsi_kokodajsi" method="POST"> 
                    <input type="hidden" value="{{ kokodajsi[indeks] }}" name="vsec_mi_je">
                    <input class="btn btn-primary" type="submit" value="všeč mi je">
                </form>
            </span>
        </li>
    </ul>
    <br>
    %end
    

</div>



