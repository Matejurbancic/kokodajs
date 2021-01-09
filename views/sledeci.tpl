%rebase("glavna_stran.tpl")



<div class="container">
      
    
    <h4><center>Seznam vseh uporabnikov, ki jim že slediš</center></h4>
    

    <center>
    <ul class="list-group" r="100px">
        <li class="list-group-item d-flex justify-content-between align-items-center" width=>
            uporabnik
            <p class="text-center">število sledilcev</p>
            <p class="text-right">ne sledi</p>
        </li>
        %for uporabnik in uporabniki:
         %if uporabnik['uporabnisko_ime'] in trenutni_uporabnik['sledeci']:

        <li class="list-group-item d-flex justify-content-between align-items-center">
         {{uporabnik['uporabnisko_ime']}}
            <span class="badge bg-primary rounded-pill">{{uporabnik['sledilci']}}</span>
            <form action="/sledeci" method="POST"> 
            % sledeci_u = uporabnik['uporabnisko_ime']                 
            <input type="hidden" value="{{ sledeci_u }}" name="ne_sledeci_uporabnik">
                <input class="btn btn-primary" type="submit"  value="ne sledi">
            </form>
        </li>
        %end
    </ul>
    </center>

</div>