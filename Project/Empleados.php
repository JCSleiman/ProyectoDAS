<?php
   class MyDB extends SQLite3 {
      function __construct() {
         $this->open('Zoologico.db');
      }
   }
   $db = new MyDB();
   if($db) {
   } else {
      echo $db->lastErrorMsg();
   }
?>

<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Mostrar Datos</title>
  </head>
  <body bgcolor="#ABF0F9">
            <h1>
            Datos de Empleados
    </h1>
    <br>
      <table border="1" cellpadding="2" cellspacing="0">
        <tr bgcolor="#FFFFFF">
          <td>Id</td >
          <td>Nombre</td>
          <td>Edad</td>
          <td>Rol</td>
          <td>Zoológico</td>

        </tr>

        <?php
        $sql="SELECT * from Empleados";
        $result= $db->query($sql);


        while($mostrar=$result->fetchArray())
        {
          ?>

        <tr bgcolor="#FFFFFF">
          <td><?php echo $mostrar['id']?></td>
          <td><?php echo $mostrar['nombre']?></td>
          <td><?php echo $mostrar['edad']?></td>
          <td><?php echo $mostrar['rol']?></td>
          <td><?php echo $mostrar['zoo']?></td>
        </tr>
      <?php
      }
        ?>
      </table>
  </body>
</html>