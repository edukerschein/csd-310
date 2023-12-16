"""
GROUP 5
OUTLAND ADVENTURES
"""

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "outland_user",
    "password": "adventure",
    "host": "127.0.0.1",
    "database": "outland_adventures",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"], ))

    cursor = db.cursor()

    # DELETE TABLES IF THEY ALREADY EXIST
    cursor.execute("DROP TABLE IF EXISTS customers;")
    cursor.execute("DROP TABLE IF EXISTS employees;")
    cursor.execute("DROP TABLE IF EXISTS equipment;")
    cursor.execute("DROP TABLE IF EXISTS trips;")


    # CREATE TABLES
    # customers
    cursor.execute("""CREATE TABLE customers (
        customer_ID     INT             NOT NULL        AUTO_INCREMENT,
        first_Name   VARCHAR(25)     NOT NULL,
        last_Name    VARCHAR(25),        
        address    VARCHAR(40),       
        email     VARCHAR(50),
        phone_Number     VARCHAR(50),
        visa_Obtained   VARCHAR(50),
        trip_ID     INT,

        PRIMARY KEY(customer_ID)
    ); """)

    # employees
    cursor.execute("""CREATE TABLE employees (
        employee_ID     INT             NOT NULL        AUTO_INCREMENT,
        first_name   VARCHAR(25)     NOT NULL,
        last_Name   VARCHAR(25)     NOT NULL,
        job_Title      VARCHAR(25),
        home_Address   VARCHAR(40),
        work_Email  VARCHAR(50),

        PRIMARY KEY(employee_ID)
    );""")

    # equipment
    cursor.execute("""CREATE TABLE equipment (
        equipment_id   INT             NOT NULL     AUTO_INCREMENT,
        equipment_name  VARCHAR(50),
        rental  INT,
        purchase   INT,
        equipment_age INT ,
        inventory      INT,

        PRIMARY KEY(equipment_id)
    );""")

    # trips
    cursor.execute("""CREATE TABLE trips (
        trip_ID   INT             NOT NULL        AUTO_INCREMENT,
        location  VARCHAR(75),
        airfare   INT,
        visa_requirements     VARCHAR(75),
        inoculations     VARCHAR(75),
        needed_equipment     VARCHAR(75),
        employee_ID     INT,
        current_month_bookings      INT,
        previous_month_bookings    INT,

        PRIMARY KEY(trip_ID)
    );""")


    # POPULATE TABLES
    # EMPLOYEES
    cursor.execute("""INSERT INTO employees (first_Name, last_Name, job_Title, home_Address, work_Email) 
        VALUES ('Blythe','Timmerson', 'Owner', '55 Woodland Lane', 'BTimmerson@outlandadventures.com');""")

    cursor.execute("""INSERT INTO employees (first_name, last_Name)
        VALUES('Jim', 'Ford');""")

    cursor.execute("""INSERT INTO employees (first_name, last_Name)
        VALUES('John', 'MacNell');""")

    cursor.execute("""INSERT INTO employees (first_name, last_Name)
        VALUES('Duke', 'Marland');""")

    cursor.execute("""INSERT INTO employees (first_name, last_Name)
        VALUES('Anita', 'Gallegos');""")

    cursor.execute("""INSERT INTO employees (first_name, last_Name)
        VALUES('Dimitrios', 'Stravopolous');""")

    cursor.execute("""INSERT INTO employees (first_name, last_Name)
        VALUES('Mei', 'Wong');""")

    # CUSTOMERS
    cursor.execute("""INSERT INTO customers(first_Name, last_Name, address, email, phone_Number, visa_Obtained, trip_ID)
        VALUES('John', 'Doe', '123 Avenue', 'jdoe@mail.com', '123-123-123', 'cleared', 1);""")

    cursor.execute("""INSERT INTO customers(first_Name, last_Name, address, email, phone_Number, visa_Obtained, trip_ID)
        VALUES('Jane', 'Doe', '123 Avenue', 'janedoe@mail.com', '123-123-123', 'cleared', 1);""")

    cursor.execute("""INSERT INTO customers(first_Name, last_Name, address, email, phone_Number, visa_Obtained, trip_ID)
        VALUES('James', 'Smith', '321 Main Street', 'jsmith@mail.com', '321-321-321', 'cleared', 2);""")

    cursor.execute("""INSERT INTO customers(first_Name, last_Name, address, email, phone_Number, visa_Obtained, trip_ID)
        VALUES('Sandra', 'Vargas', '586 Tremblay Dr', 'hikingmama@hotmail.com', '403-684-9473', 'not cleared', 2);""")

    cursor.execute("""INSERT INTO customers(first_Name, last_Name, address, email, phone_Number, visa_Obtained, trip_ID)
        VALUES('Geoffrey', 'Miller', '5938 Rainey Ln', 'geoffmiller@gmail.com', '486-395-2956', 'not cleared', 3);""")

    cursor.execute("""INSERT INTO customers(first_Name, last_Name, address, email, phone_Number, visa_Obtained, trip_ID)
        VALUES('Veronica', 'Mercury', '99 San Antonio Way', 'vmercury98@gmail.com', '594-265-2436', 'cleared', 3);""")

    # EQUIPMENT
    cursor.execute("""INSERT INTO equipment(rental, equipment_name, purchase, equipment_age, inventory)
        VALUES(5, 'Canteen', 16, 1, 50);""")

    cursor.execute("""INSERT INTO equipment(rental, equipment_name, purchase, equipment_age, inventory)
            VALUES(9, 'Walking Sticks', 5, 6, 20);""")

    cursor.execute("""INSERT INTO equipment(rental, equipment_name, purchase, equipment_age, inventory)
            VALUES(3, 'Tent', 21, 3, 15);""")

    cursor.execute("""INSERT INTO equipment(rental, equipment_name, purchase, equipment_age, inventory)
                VALUES(5, 'GPS', 3, 2, 25);""")

    cursor.execute("""INSERT INTO equipment(rental, equipment_name, purchase, equipment_age, inventory)
                VALUES(7, 'Kayak', 0, 8, 4);""")

    cursor.execute("""INSERT INTO equipment(rental, equipment_name, purchase, equipment_age, inventory)
                VALUES(6, 'Hiking Backpack', 2, 4, 13);""")

    # TRIPS
    cursor.execute("""INSERT INTO trips(trip_ID, location, airfare, inoculations, needed_equipment, employee_ID, current_month_bookings, previous_month_bookings)
        VALUES(1, 'Africa', 1000, 'Cleared', 'Canteen', 3, 5, 9);""")

    cursor.execute("""INSERT INTO trips(trip_ID, location, airfare, inoculations, needed_equipment, employee_ID, current_month_bookings, previous_month_bookings)
            VALUES(2, 'Asia', 975, 'Cleared', 'Tent', 3, 9, 9);""")

    cursor.execute("""INSERT INTO trips(trip_ID, location, airfare, inoculations, needed_equipment, employee_ID, current_month_bookings, previous_month_bookings)
            VALUES(3, 'Southern Europe', 1300, 'Cleared', 'Walking Sticks', 4, 9, 9);""")

    cursor.execute("""INSERT INTO trips(trip_ID, location, airfare, inoculations, needed_equipment, employee_ID, current_month_bookings, previous_month_bookings)
            VALUES(4, 'Africa', 1150, 'Cleared', 'Tent', 4, 5, 4);""")

    cursor.execute("""INSERT INTO trips(trip_ID, location, airfare, inoculations, needed_equipment, employee_ID, current_month_bookings, previous_month_bookings)
            VALUES(5, 'Asia', 975, 'Cleared', 'Canteen', 3, 6, 2);""")

    cursor.execute("""INSERT INTO trips(trip_ID, location, airfare, inoculations, needed_equipment, employee_ID, current_month_bookings, previous_month_bookings)
            VALUES(6, 'Southern Europe', 1450, 'Cleared', 'Walking Sticks', 4, 3, 3);""")

    # PRINT RESULTS
    # CUSTOMERS
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()

    print("\n\n-- DISPLAYING CUSTOMERS RECORDS --")
    for customer in customers:
        print("Customer ID: " + str(customer[0]))
        print("First Name: " + str(customer[1]))
        print("Last Name: " + str(customer[2]))
        print("Address: " + str(customer[3]))
        print("Email: " + str(customer[4]))
        print("Phone Number: " + str(customer[5]))
        print("Visa Obtained: " + str(customer[6]))
        print("Trip ID: " + str(customer[7]))
        print("")

    # EMPLOYEES
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    print("\n-- DISPLAYING EMPLOYEES RECORDS --")
    for employee in employees:
        print("Employee ID: " + str(employee[0]))
        print("First Name: " + str(employee[1]))
        print("Last Name: " + str(employee[2]))
        print("Job Title: " + str(employee[3]))
        print("Home Address: " + str(employee[4]))
        print("Work Email: " + str(employee[5]))
        print("")

    # EQUIPMENT
    cursor.execute("SELECT * FROM equipment")
    equipment = cursor.fetchall()

    print("\n-- DISPLAYING EQUIPMENT RECORDS --")
    for item in equipment:
        print("Equipment ID: " + str(item[0]))
        print("Equipment name: " + str(item[1]))
        print("Rental: " + str(item[2]))
        print("Purchase: " + str(item[3]))
        print("Equipment Age: " + str(item[4]))
        print("Inventory: " + str(item[5]))
        print("")

    # TRIPS
    cursor.execute("SELECT * FROM trips")
    trips = cursor.fetchall()

    print("\n-- DISPLAYING TRIPS RECORDS --")
    for trip in trips:
        print("Trip ID: " + str(trip[0]))
        print("Location: " + str(trip[1]))
        print("Airfare: " + str(trip[2]))
        print("Inoculations: " + str(trip[4]))
        print("Equipment Needed: " + str(trip[5]))
        print("Employee ID: " + str(trip[6]))
        print("Number of Bookings for Current Month: " + str(trip[7]))
        print("Number of Bookings for Previous Month: " + str(trip[8]))
        print("")

    print("\n-- DISPLAYING REPORTS --")
    # EQUIPMENT AGE
    cursor.execute("""SELECT equipment_id, equipment_name, equipment_age FROM equipment
       WHERE equipment_age > 5;
       """)

    report1 = cursor.fetchall()

    print("-- REPORT 1 --")
    for x in report1:
        print("Equipment ID: " + str(x[0]))
        print("Equipment Name: " + str(x[1]))
        print("Equipment Age: " + str(x[2]))
        print("")
    print("")

    # TREK BOOKINGS
    cursor.execute("SELECT location, SUM(previous_month_bookings), SUM(current_month_bookings) FROM trips GROUP BY location")
    report2 = cursor.fetchall()


    print("-- REPORT 2 --")

    for x in report2:
        print("Location: " + str(x[0]))
        print("Previous Bookings: " + str(x[1]))
        print("Current Bookings: " + str(x[2]))
        print("Difference: " + str(x[2] - x[1]))
        if ((x[2] - x[1]) < 0):
            print("Trend: Downward")
        elif ((x[2] - x[1])== 0):
            print("Trend: Stable")
        else:
            print("Trend: Upward")
        print("")

    print("")

    # EQUIPMENT SALES
    cursor.execute("SELECT purchase, rental, equipment_name FROM equipment")
    report3 = cursor.fetchall()

    print("-- REPORT 3 --")
    for x in report3:
        print("Equipment Name: "+ str(x[2]))
        print("Purchases: "+ str(x[0]))
        print("Rentals: "+ str(x[1]))
        print("")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)

finally:
    db.close()