%rebase("glavna_stran.tpl")


<br>
<div class="container">
      
      
    

  <center>
      <span style="float:left;">
      
        
        
        <form action="/uporabniki" method="POST">
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          <input type="hidden" value="sledim" name="sledim">
          <input class="btn btn-primary" type="submit" value="sledim">
          
        </form>
        
        
        
      </span>
      
      <span style="float:right;"> 
     
        <form action="/uporabniki" method="POST">
        
          <input type="hidden" value="ne_sledim" name="sledim">
          <input class="btn btn-primary" type="submit" value="ne sledim">
          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        </form>
      </span>
  </center>
    

  <br>
  <br>
  %if sledenje is True:
  <h4><center>Seznam vseh uporabnikov, ki jim že slediš</center></h4>
  %else:
  <h4><center>Seznam vseh uporabnikov, ki jim ne slediš</center></h4>
  %end
  %if sledenje is True:
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
        %for uporabnik in uporabniki.seznam:
        %if uporabnik.uporabnisko_ime in trenutni_uporabnik.sledeci:
        <tr>
          <th scope="row">{{trenutni_uporabnik.sledeci.index(uporabnik.uporabnisko_ime) + 1}}</th>
          <td>{{uporabnik.uporabnisko_ime}}</td>
          <td><span class="badge bg-primary rounded-pill">{{uporabnik.sledilci}}</span></td>
          <td>
            <form action="/sledeci" method="POST"> 
            % sledeci_u = uporabnik.uporabnisko_ime                 
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

  %else:
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
      %for uporabnik in uporabniki.seznam:
          %if uporabnik.uporabnisko_ime not in trenutni_uporabnik.sledeci and uporabnik.uporabnisko_ime != trenutni_uporabnik.uporabnisko_ime:
        % zaporedna_stevilka += 1
        <tr>
          <th scope="row">{{zaporedna_stevilka}}</th>
          <td>{{uporabnik.uporabnisko_ime}}</td>
          <td><span class="badge bg-primary rounded-pill">{{uporabnik.sledilci}}</span></td>
          <td><form action="/ne_sledeci" method="POST"> 
                % sledeci_u = uporabnik.uporabnisko_ime                 
              <input type="hidden" value="{{ sledeci_u }}" name="sledeci_uporabnik">
                  <input class="btn btn-primary" type="submit"  value="sledi">
              </form>
          </td>
        </tr>
        %end
      %end
      </tbody>
    </table>
  </center>
  %end

</div>