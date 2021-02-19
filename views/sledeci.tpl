%rebase("glavna_stran.tpl")



<div class="container">
      
    
  <h4><center>Seznam vseh uporabnikov, ki jim že slediš</center></h4>
    

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
        %for uporabnik in uporabniki:
        %if uporabnik['uporabnisko_ime'] in trenutni_uporabnik['sledeci']:
        <tr>
          <th scope="row">{{trenutni_uporabnik['sledeci'].index(uporabnik['uporabnisko_ime']) + 1}}</th>
          <td>{{uporabnik['uporabnisko_ime']}}</td>
          <td><span class="badge bg-primary rounded-pill">{{uporabnik['sledilci']}}</span></td>
          <td>
            <form action="/sledeci" method="POST"> 
            % sledeci_u = uporabnik['uporabnisko_ime']                 
              <input type="hidden" value="{{ sledeci_u }}" name="ne_sledeci_uporabnik">
              <input class="btn btn-primary" type="submit"  value="ne sledi">
            </form>
          </td>
        </tr>
        %end
        %end
      </tbody>
    </table>
  </center>
</div>


