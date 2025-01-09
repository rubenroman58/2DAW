import sqlite3
# Conexión a la base de datos (se crea si no existe)
conn = sqlite3.connect('mi_base_de_datos.db')
# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()
# Crear una tabla
""" cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
id INTEGER PRIMARY KEY AUTOINCREMENT,
nombre TEXT,
edad INTEGER
)
''')
# Insertar datos
cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', ('Alice',
25)) """
# Confirmar cambios
conn.commit()
# Consultar datos
cursor.execute('SELECT * FROM usuarios')
print(cursor.fetchall())
# Cerrar conexión
conn.close()