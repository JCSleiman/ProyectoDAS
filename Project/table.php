<?php
   class MyDB extends SQLite3 {
      function __construct() {
         $this->open('Zoologico.db');
      }
   }
   $db = new MyDB();
   if(!$db) {
      echo $db->lastErrorMsg();
   } else {
      echo "Opened database successfully\n";
   }
?>

<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Mostrar Datos</title>
  </head>
  <body>

    <br>

      <table border="1">
        <tr>
          <td>id</td>
          <td>nombre</td>
          <td>lugar</td>
          <td>empleados</td>
          <td>animales</td>
        </tr>

        <?php
        $sql="SELECT * from Zoo";
        #  $sql =<<<EOF
      #      SELECT * from COMPANY;
#EOF;
        $result=sqlite_query($conexion,$sql);

        while($mostrar=sqlite_fetch_array($result)){
          ?>

        <tr>
          <td><?php echo $mostrar['id']?></td>
          <td><?php echo $mostrar['nombre']?></td>
          <td><?php echo $mostrar['lugar']?></td>
          <td><?php echo $mostrar['empleados']?></td>
          <td><?php echo $mostrar['animales']?></td>
        </tr>
      <?php
      }
        ?>
      </table>

  </body>
</html>
