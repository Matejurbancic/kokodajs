%rebase("glavna_stran.tpl")



<div class="container">
      
    
    <h4><center>Seznam vseh uporabnikov, ki jim še ne slediš</center></h4>
    

    <center>
    <ul class="list-group" r="100px">
        <li class="list-group-item d-flex justify-content-between align-items-center" width=>
            uporabnik
            <p class="text-center">število sledilcev</p>
            <p class="text-right">sledi</p>
        </li>
        %for uporabnik in uporabniki:
         %if uporabnik['uporabnisko_ime'] not in trenutni_uporabnik['sledeci'] and uporabnik['uporabnisko_ime'] != trenutni_uporabnik['uporabnisko_ime']:

        <li class="list-group-item d-flex justify-content-between align-items-center">
         {{uporabnik['uporabnisko_ime']}}
            <center> <span class="badge bg-primary rounded-pill">{{uporabnik['sledilci']}}</span> </center>
            <form action="/ne_sledeci" method="POST"> 
            % sledeci_u = uporabnik['uporabnisko_ime']                 
            <input type="hidden" value="{{ sledeci_u }}" name="sledeci_uporabnik">
                <input class="btn btn-primary" type="submit"  value="sledi">
            </form>
        </li>
        %end
        %end
    </ul>
    </center>

</div>