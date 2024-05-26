
-- Insert test data into Accounts
INSERT INTO Accounts (AccountNumber, AccountType, Balance, LastAccessDate, InterestRate, Overdraft, CustomerID)
VALUES (123456789, 'Savings', 900.00, '2023-12-02', 0.03, 50.00, 12346);
delete  from accounts where AccountNumber=123456789;
-- Insert test data into Employees
INSERT INTO Employees (EmployeeID, SSN, Name, Address, Telephone, Dependents, ManagerSSN, StartDate, LengthOfEmployment)
VALUES (77, '111-22-3333', 'John Doe', '123 Main St', '555-1234', 2, '111-22-4444', '2023-01-01', 2);

show columns  from employees;
-- Update the manager to trigger the update_manager_details trigger
UPDATE Employees SET ManagerSSN = '111-22-5555' WHERE EmployeeID = 77;

delete from Employees where employeeID=77;

select * from notificationlog;
delete from notificationlog;

CREATE TABLE NotificationLog (
    NotificationID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT,
    NotificationMessage VARCHAR(255) NOT NULL,
    NotificationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);


SHOW TRIGGERS LIKE 'InterestRateNotification';
SELECT * FROM Accounts WHERE Balance < 1000.00;
UPDATE Accounts SET Balance = 900.00 WHERE AccountNumber = 123456789;

SHOW TRIGGERS LIKE 'update_manager_details';





-- Drop the existing trigger
DROP TRIGGER IF EXISTS InterestRateNotification;

-- Set the delimiter to handle the CREATE TRIGGER statement
DELIMITER //
-- Create the new trigger
CREATE TRIGGER InterestRateNotification AFTER UPDATE ON Accounts FOR EACH ROW 
BEGIN     
    DECLARE balance_threshold DECIMAL(15, 2);
    SET balance_threshold = 1000.00;

    IF NEW.Balance < balance_threshold THEN
        INSERT INTO NotificationLog (CustomerID, NotificationMessage, NotificationDate)
        VALUES (NEW.CustomerID, 'Your account balance has fallen below $1000. Please be aware of the interest rate change.', NOW());
    END IF;
END;

//
