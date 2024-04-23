import csv
import sqlite3
from datetime import datetime

# Definir la ruta de la base de datos
DATABASE_FILE = "emps_cpy.db"

# Obtener el mes y el año actuales
current_month_year = datetime.now().strftime('%m%Y')

def read_employee_data():
    """
    Lee los datos de los empleados desde la base de datos y los devuelve como una lista de diccionarios.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM EMPS_CPY''')
    rows = cursor.fetchall()

    employee_data = []
    for row in rows:
        employee_dict = {
            'EMPLOYEE_ID': row[0],
            'EMPLOYEE_LASTNAME': row[1],
            'EMPLOYEE_FIRSTNAME': row[2],
            'EMPLOYEE_SALARY': row[3],
            'EMPLOYEE_DEPARTMENT': row[4],
            'EMPLOYEE_LEVEL': row[5]
        }
        employee_data.append(employee_dict)

    conn.close()

    return employee_data


def calculate_monthly_salary(employee_data):
    """
    Calcula el salario mensual para cada empleado.
    Actualiza los datos en la lista de empleados y retorna la lista actualizada.
    """
    for employee in employee_data:
        annual_salary = float(employee['EMPLOYEE_SALARY'])
        monthly_salary = annual_salary / 12
        monthly_salary = round(monthly_salary, 2)
        employee['MONTHLY_SALARY'] = monthly_salary
    return employee_data


def write_payroll_data(employee_data, file_path):
    """
    Escribe los datos de nómina en el archivo de salida.
    """    
    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = employee_data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(employee_data)

def main():
    # Leer datos de empleados
    employee_data = read_employee_data()
 
    # Calcular salario mensual
    employee_data = calculate_monthly_salary(employee_data)
    
    # Escribir datos de nómina. fichero con mes y año actuales
    #output_file = "PAYROLL_ALL_MMAAAA.csv"
    output_file = f'PAYROLL_ALL_{current_month_year}.csv'
    write_payroll_data(employee_data, output_file)

    print(output_file)

print("Fichero generado OK.")

if __name__ == "__main__":
    main()
