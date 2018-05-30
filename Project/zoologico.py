#bultin library
import os
#external libraries
import pony.orm as pony
#from models import Zoo, Animales, Empleados

# Definiendo nuestra db
basedir = os.path.abspath(os.path.dirname("C:\sql\ejemplo"))
PONY_DATABASE_URI = os.path.join(basedir, "Zoologico.db")

database = pony.Database("sqlite", PONY_DATABASE_URI, create_db=True)

#Definiendo los modelos de  zoo, animales y empleados
class Zoo(database.Entity):
    """zoo, it is asociated with the animales and empleados"""
    nombre = pony.Required(str, 50, unique=True)
    lugar = pony.Required(str, 50)
    empleados = pony.Set("Empleados")
    animales = pony.Set("Animales")

    ##def __repr__(self):
    ##    return "".format(self.nickname, self.email)
##########################################################################
class Empleados(database.Entity):

    nombre = pony.Required(str, 50, unique=True)
    edad = pony.Required(int)
    rol = pony.Required(str, 50)
    zoo = pony.Required(Zoo)

    #def __repr__(self):
    #    return "".format(self.nombre, self.edad, self.rol)
##########################################################################
class Animales(database.Entity):

    especie = pony.Required(str, 50, unique=True)
    meses = pony.Required(int)
    zoo = pony.Required(Zoo)

    #def __repr__(self):
    #    return "".format(self.nombre, self.edad, self.rol)
##########################################################################
# enciende el debug
pony.sql_debug(True)
# crea la tabla si no existe
database.generate_mapping(create_tables=True)
