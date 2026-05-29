import mysql.connector

conn = mysql.connector.connect(
    host="------",
    port=------,
    user="--------",
    password="------",
    database="python_db",
    use_pure=True
)

cursor = conn.cursor()

Employees = {}
count = 0

while True:

    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':

        count += 1

        Employees[count] = {}

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Employee Department: ")
        salary = float(input("Enter Employee Salary: "))
        bonus = float(input("Enter Employee Bonus: "))

        Employees[count]['ID'] = emp_id
        Employees[count]['Name'] = name
        Employees[count]['Department'] = department
        Employees[count]['Salary'] = salary
        Employees[count]['Bonus'] = bonus

        query = """
        INSERT INTO employees
        (employee_id, employee_name, department, salary, bonus)
        VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            Employees[count]['ID'],
            Employees[count]['Name'],
            Employees[count]['Department'],
            Employees[count]['Salary'],
            Employees[count]['Bonus']
        )

        cursor.execute(query, values)
        conn.commit()

        print("\nEmployee Added Successfully!")
        print("\nCurrent Dictionary:")
        print(Employees)

    elif choice == '2':

        print("Exiting Program...")
        break

    else:

        print("Invalid Choice! Try Again.")

# Close connection
cursor.close()
conn.close()