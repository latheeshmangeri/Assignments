DROP TABLE  LoanPayments;
DROP TABLE  Loans;
DROP TABLE  Accounts;
DROP TABLE  Employees;
DROP TABLE  Customers;
DROP TABLE  Branches;






-- Create table for branches
CREATE TABLE Branches (
    BranchID INT PRIMARY KEY,
    BranchName VARCHAR(50) NOT NULL,
    City VARCHAR(50) NOT NULL,
    Assets DECIMAL(15, 2)
);

-- Create table for customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    SSN VARCHAR(20) UNIQUE NOT NULL,
    CustomerType VARCHAR(20) NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    BranchID INT,
    FOREIGN KEY (BranchID) REFERENCES Branches(BranchID)
);

-- Create table for employees
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    SSN VARCHAR(20) UNIQUE NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    Telephone VARCHAR(20),
    Dependents INT,
    ManagerSSN VARCHAR(20),
    StartDate DATE,
    LengthOfEmployment INT
);

-- Create table for accounts
CREATE TABLE Accounts (
    AccountNumber BIGINT PRIMARY KEY,
    AccountType VARCHAR(20) NOT NULL,
    Balance DECIMAL(15, 2) NOT NULL,
    LastAccessDate DATE,
    InterestRate DECIMAL(5, 2),
    Overdraft DECIMAL(15, 2),
    CustomerID INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create table for loans
CREATE TABLE Loans (
    LoanNumber INT PRIMARY KEY,
    CustomerID INT,
    LoanAmount DECIMAL(15, 2) NOT NULL,
    BranchID INT,
    FOREIGN KEY (BranchID) REFERENCES Branches(BranchID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create table for loan payments
CREATE TABLE LoanPayments (
    PaymentNumber INT PRIMARY KEY,
    LoanNumber INT,
    PaymentDate DATE,
    PaymentAmount DECIMAL(15, 2) NOT NULL,
    FOREIGN KEY (LoanNumber) REFERENCES Loans(LoanNumber)
);
