from flask	import Flask
from flask import request
from peewee import *

db = SqliteDatabase('Zoologico.db')

class Zoo(Model):
	id= PrimaryKeyField(null=False)
	nombre = TextField()
	lugar = TextField()
#	empleados = ForeignKeyField(Empleados, related_name="empleados_zoo")
#	animales = ForeignKeyField(Animales, related_name="animales_zoo")

	class Meta:
		database = db

	def __str__(self):
		return "ID: {}  Zoo: {}  Lugar:{} ".format(self.id, self.nombre, self.lugar)

class Empleados(Model):
	id = PrimaryKeyField(null=False)
	nombre = TextField()
	edad = TextField()
	rol = IntegerField()
	zoo = ForeignKeyField(Zoo, related_name="empleados_zoo")

	class Meta:
		database = db

	def __str__(self):
		return "ID:: {}\nNombre: {} {}\n:Edad {} {}\nRol: {}\nZoo: {}\n".format(self.id_empleado, self.nombre, self.edad, self.rol, self.zoo.nombre)

class Animales(Model):
	id = PrimaryKeyField(null=False)
	epecie = DateField()
	meses = TextField()
	zoo = ForeignKeyField(Zoo, related_name="animales_zoo")

	class Meta:		

		database = db

	def __str__(self):
		return "ID:: {}\nEspecie: {} {}\nMeses: {} {}\nZoo: {}\n".format(self.id_animal, self.especie, self.meses, self.zoo.nombre)


#####################################################################################################################
#app = Flask(__name__)
#
#@app.route('/Select<int: ids>')
#
#def show_Zoo(*ids):
#
#	if ids:
#		return [str(zoo) for zoo in Zoo.select().where(*ids)]
#
#
#	select = request.args.get("id=", Zoo.select().where(*ids))

###################################################################################################################

class CRUD:
	@staticmethod
	def insert(model, **datos):
		model = model.lower()
		print(model)
		if model == 'zoo':
			return Zoo.create(**datos)
		if model == 'Animales':
			return Empleados.create(**datos)
		if model == 'Empleados':
			return Animales.create(**datos)
		else:
			return 'Modelo no existe. Intenta de nuevo.'

	def select(model, *ids):
		model = model.lower()

		if model == 'zoo':
			if ids:
				return [str(zoo) for zoo in Zoo.select().where(*ids)]
			return [str(zoo) for zoo in Zoo.select()]
	
			if model == 'empleados':
				if ids:
					return [str(emp) for emp in Empleados.select().where(*ids)]
				return [str(pcte) for emp in Empleados.select()]
			if model == 'animales':
				if ids:
					return [str(ani) for ani in Animales.select().where(*ids)]
				return [str(con) for ani in Animales.select()]
			else:
				return 'Modelo no existe. Intenta de nuevo.'


	@staticmethod
	def update(model, *condicion, **datos):
		model = model.lower()

		if model == 'empleados':
			return Empleados.update(**datos).where(*condicion).execute()

		if model == 'animales':
			return Animales.update(**datos).where(*condicion).execute()

		if model == 'zoo':
			return Zoo.update(**datos).where(*condicion).execute()
		else:
			return 'Modelo no existe. Intenta de nuevo.'

	@staticmethod
	def delete(model, *condicion):
		model = model.lower()

		if model == 'empleados':
			return Empleados.delete().where(*condicion).execute()

		if model == 'animales':
			return Animales.delete().where(*condicion).execute()

		if model == 'zoo':
			return Zoo.delete().where(*condicion).execute()
		else:
			return 'Modelo no existe. Intenta de nuevo.'




#Insertando registros
#print(CRUD.insert('Zoo',id= 103,nombre='Young', lugar='General'))

#Select
#print(Zoo.select().where(Zoo.id == 101).get())
#print(CRUD.select('Zoo', Zoo.id == 101))
#
##Update
update_zoo = {'nombre': 'Zoologico chapultepec'}
print(CRUD.update('Zoo', Zoo.id == 102, **update_zoo))
print(Zoo.select().where(Zoo.id == 102).get())
#
##Delete
#print(CRUD.delete('Zoo', Zoo.id == 102))
#print(CRUD.select('Zoo', Zoo.id == 102))
#