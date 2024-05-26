import pymysql
from datetime import datetime

# Connect to the MySQL database
db = pymysql.connect(
    host="academicmysql.mysql.database.azure.com",
    user="lxm6009",
    password="Lathi2525@",
    database="lxm6009"
)

# Create a cursor object
cursor = db.cursor()

# 5.1 Create a new account for a business
def create_business_account():
    try:
        # Assuming BusinessCustomer table is populated appropriately
        cursor.execute("insert into Accounts (AccountNumber, AccountType, Balance, LastAccessDate, InterestRate, Overdraft, CustomerID) values (%s, %s, %s, %s, %s, %s, %s);",
                                             (6965778831, 'Business',92355.93, datetime.now().strftime('%Y-%m-%d'),36.78, 73.12,12346))
        db.commit()
        print("New business account created successfully.")
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")

# 5.2 Create a new account for an individual with an initial deposit of $1000
def create_individual_account():
    try:
        # Assuming IndividualCustomer table is populated appropriately
        cursor.execute(
            "insert into Accounts (AccountNumber, AccountType, Balance, LastAccessDate, InterestRate, Overdraft, CustomerID) values (%s, %s, %s, %s, %s, %s, %s);",
            (6965778832, 'Individual', 1000, datetime.now().strftime('%Y-%m-%d'), 46.78, 83.12, 12346))

        db.commit()
        print("New individual account created successfully.")
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")

# 5.3 Issue a loan of $20,000 from a branch to a specific customer from a specific city
def issue_loan():
    try:
        # Assuming LoanCustomer and Customer tables are populated appropriately
        cursor.execute("INSERT INTO Loans (LoanNumber, CustomerID, LoanAmount, BranchID) "
                                   "VALUES(%s,(SELECT CustomerID FROM Customers WHERE Name = %s AND Address = %s),%s,(SELECT BranchID FROM Branches WHERE BranchName = %s));",
                       (842013326,'Liesa Duerden','77835 Blaine Alley',20000.00,'Bowman'))
        db.commit()
        print("Loan issued successfully.")
    except Exception as e:
        db.rollback()
        print(f"Error: {e}")

# Call the functions to perform the transactions
create_business_account()
create_individual_account()
issue_loan()

# Close the database connection
db.close()
