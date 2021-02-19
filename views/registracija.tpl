<!doctype html>
<html lang="sl">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">

    <title>Kokodajs</title>
  </head>
  <body>
    <div class="container">
      
    
      <h1><center>Registracija</center></h1>

      <center>
        <div class="container">
        %if vrednost_napake == 1:
          <p style="color:red"><b>Vneseno uporabniško ime je že zasedeno!</b></p>
        %elif vrednost_napake == 2:
          <p style="color:red"><b>Registracija ni pravilno izpolnjena</b></p>
          %elif vrednost_napake == 3:
          <p style="color:red"><b>Uporabniško ime lahko vsebuje le ASCII znake</b></p>
          %end

          <form action="/registracija/" method="post">
            <label for="novo_up_ime"><b>uporabniško ime</b></label>
            <input type="text" placeholder="vpiši uporabniško ime" name="novo_up_ime" required>

            <label for="geslo"><b>geslo</b></label>
            <input type="password" placeholder="vpiši geslo" name="geslo" required>

            <label for="geslo_ponovno"><b> ponovi geslo</b></label>
            <input type="password" placeholder="ponovno vpiši geslo" name="geslo_ponovno" required>

          <input value="Registracija" type="submit" />





            <!--   Username: <input name="username" type="text" />
              Password: <input name="password" type="password" />
              <input value="Login" type="submit" /> -->
          </form>
        </div>
      </center>
    </div>



    <!-- Optional JavaScript; choose one of the two! -->

    <!-- Option 1: Bootstrap Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js" integrity="sha384-ygbV9kiqUc6oa4msXn9868pTtWMgiQaeYH7/t7LECLbyPA2x65Kgf80OJFdroafW" crossorigin="anonymous"></script>

    <!-- Option 2: Separate Popper and Bootstrap JS -->
    <!--
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js" integrity="sha384-q2kxQ16AaE6UbzuKqyBE9/u/KzioAlnx2maXQHiDX9d4/zp8Ok3f+M7DPm+Ib6IU" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-pQQkAEnwaBkjpqZ8RU1fF1AKtTcHJwFl3pblpTlHXybJjHpMYo79HY3hIi4NKxyj" crossorigin="anonymous"></script>
    -->
  </body>
</html>