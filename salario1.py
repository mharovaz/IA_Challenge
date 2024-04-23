import sqlite3

import csv
import sqlite3

# Definir la ruta de la base de datos
DATABASE_FILE = "emps_cpy.db"


def read_employee_data():
    """
    Lee los datos de empleados desde la base de datos.
    Retorna una lista de diccionarios con los datos de cada empleado.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM EMPS_CPY ORDER BY EMPLOYEE_DEPARTMENT, EMPLOYEE_LEVEL, EMPLOYEE_LASTNAME")
    employee_data = [dict(row) for row in cursor.fetchall()]
    conn.close()
    print(cursor.fetchall) 
    print(employee_data)
    return employee_data

def main():
    # Leer datos de empleados
    employee_data = read_employee_data()
 

if __name__ == "__main__":
    main()


def read_employee_data():
    """
    Lee los datos de empleados desde la base de datos.
    Retorna una lista de diccionarios con los datos de cada empleado.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM EMPS_CPY ORDER BY EMPLOYEE_DEPARTMENT, EMPLOYEE_LEVEL, EMPLOYEE_LASTNAME")
    employee_data = [dict(row) for row in cursor.fetchall()]
    conn.close()
    print(cursor.fetchall) 
    return employee_data