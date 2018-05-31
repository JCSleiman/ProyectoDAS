from peewee import *

db = SqliteDatabase('DbZoo.db')

class Zoo(Model):
	id_zoo = PrimaryKeyField(null=False)
	nombre = TextField()
	lugar = TextField()
	class Meta:
		database = db

	def __str__(self):
			return "ID: {}\n Zoo: {} {}\n Lugar: {}\n empleados:{}\n animales: {}\n".format(self.id_zoo, self.nombre, self.lugar)

class Empleados(Model):
	id_empleado = PrimaryKeyField(null=False)
	nombre = TextField()
	edad = TextField()
	rol = IntegerField()

	class Meta:
		database = db

	def __str__(self):
		return "ID:: {}\nNombre: {} {}\n:Edad {} {}\nRol: {}\nZoo: {}\n".format(self.id_empleado, self.nombre, self.edad, self.rol)

class Animales(Model):
	id_animal = PrimaryKeyField(null=False)
	epecie = DateField()
	meses = TextField()

	class Meta:
		database = db

	def __str__(self):
		return "ID:: {}\nEspecie: {} {}\nMeses: {} {}\nZoo: {}\n".format(self.id_animal, self.especie, self.meses)
		#return "No. consulta: {}\nDoctor: {}\nPaciente: {}\nFecha: {}\nDiagnóstico: {}\nMedicamento: {}\n".format(self.id_consulta, self.doctor, self.self.paciente, self.fecha_consulta, self.diagnostico, self.medicamento)


