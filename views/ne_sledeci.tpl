%rebase("glavna_stran.tpl")



<div class="container">
      
    
    <h4><center>Seznam vseh uporabnikov, ki jim še ne slediš</center></h4>
    

    <center>
    <table class="table">
  <thead>
    <tr>
      <th scope="col"></th>
      <th scope="col">uporabniško ime</th>
      <th scope="col">število sledilcev</th>
      <th scope="col"></th>
    </tr>
  </thead>
  <tbody>
  % zaporedna_stevilka = 0
   %for uporabnik in uporabniki:
         %if uporabnik['uporabnisko_ime'] not in trenutni_uporabnik['sledeci'] and uporabnik['uporabnisko_ime'] != trenutni_uporabnik['uporabnisko_ime']:
    % zaporedna_stevilka += 1
    <tr>
      <th scope="row">{{zaporedna_stevilka}}</th>
      <td>{{uporabnik['uporabnisko_ime']}}</td>
      <td><span class="badge bg-primary rounded-pill">{{uporabnik['sledilci']}}</span></td>
      <td><form action="/ne_sledeci" method="POST"> 
            % sledeci_u = uporabnik['uporabnisko_ime']                 
            <input type="hidden" value="{{ sledeci_u }}" name="sledeci_uporabnik">
                <input class="btn btn-primary" type="submit"  value="sledi">
            </form></td>
    </tr>
    %end
    %end
    </tbody>
    </table>
    </center>

</div>