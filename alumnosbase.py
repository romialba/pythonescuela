import mysql.connector
import os
#conexion = mysql.connect ()
#cursor = conexion.cursor()
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "FESARAGON",
    database = "escuela"
)

cursor = conexion.cursor()

cursor.execute(
    """
    create table if not exists alumnos (
    id integer primary key auto_increment,
    nombre varchar (100) not null,
    matricula bigint,
    grupo int,
    carrera varchar (100) not null,
    correoinstitucional varchar (100) not null,
    telefonotutor bigint, 
    horainicio time,
    horafinal time,
    turno varchar (100),
    asistencia int,
    perfil longblob
    )
    """
)

archivo_imagenes = ["alumno1.jpeg", "alumno2.jpeg", "alumno3.jpeg", "alumno4.jpeg" ]
imagenes = []
for archivo in archivo_imagenes:
    with open(archivo, "rb") as f:
        imagenes.append (f.read())
        print (f"se leyeron {len (imagenes)} imagenes insertadas")

sql = "insert into alumnos(nombre, matricula, grupo, carrera, correoinstitucional, telefonotutor, horainicio, horafinal, turno, asistencia, perfil) values (%s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s)"
personas = [
    ("Alba Garfias Romina", 2400405920, 501, "Ciencia de Datos e Inteligencia Artificial","ralba024@df.conalep.edu.mx", 5629361270, "7:00", "13:20", "matutino", 5, imagenes[0]),
    ("Zarco Perez de Leon Yahel Arturo", 240040163, 501, "Ciencia de Datos e Inteligencia Artificial", "yzarco0524@df.conalep.edu.mx", 5643139201, "7:00", "13:20", "matutino", 5,imagenes[1]),
    ("Martinez Garcia Noely Jonuth", 2400405441, 501, "Ciencia de Datos e Inteligencia Artificial", "nmartinez0124@df.conalep.edu.mx", 568023451067, "7:00", "13:20", "matutino", 5, imagenes[2]), 
    ("Hernandez Ramirez Donovan",240040675, 501, "Ciencia de Datos e Inteligencia Artificial","dhramirez1506@df.conalep.edu.mx", 564036592178, "7:00", "13:20", "matutino", 5, imagenes[3])
]

cursor.executemany (sql, personas)
conexion.commit()
print(f"{cursor.rowcount} alumnos insertados")

cursor.execute("select id, nombre, perfil from alumnos")
resultados = cursor.fetchall()


for id, nombre, imagen in resultados: 
    if imagen:
        nombre_archivo = f"alumno{id}.jpeg" 
    with open(archivo, "wb") as f:
        f.write (imagen)
    print (f"imagen de {nombre} guardada como {nombre_archivo}")
else:
     print (f" {nombre} no tiene imagen")

cursor.execute ("describe alumnos")
print ("\n tablas alumnos")
for column in cursor.fetchall(): 
    print (column)
    cursor.close()

    conexion.close()