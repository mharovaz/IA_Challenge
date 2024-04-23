import sqlite3

# Conexión a la base de datos (creará el archivo si no existe)
conn = sqlite3.connect('emps_cpy.db')
cursor = conn.cursor()

# Crear la tabla EMPS-CPY
cursor.execute('''CREATE TABLE EMPLOYEE_TABLE (
                    EMPLOYEE_ID INTEGER PRIMARY KEY,
                    EMPLOYEE_LASTNAME TEXT,
                    EMPLOYEE_FIRSTNAME TEXT,
                    EMPLOYEE_SALARY REAL,
                    EMPLOYEE_DEPARTMENT TEXT,
                    EMPLOYEE_LEVEL TEXT
                )''')

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos EMPS_CPY creada correctamente.")
