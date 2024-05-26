-- 6.1 Trigger to Notify Member about Interest Rate Change
DROP TRIGGER IF EXISTS InterestRateNotification;
DROP TRIGGER IF EXISTS update_manager_details;
DELIMITER //
CREATE TRIGGER InterestRateNotification
AFTER UPDATE ON Accounts
FOR EACH ROW
BEGIN
    DECLARE balance_threshold DECIMAL(15, 2);
    SET balance_threshold = 1000.00;

    IF NEW.Balance < balance_threshold THEN
        INSERT INTO NotificationLog (CustomerID, NotificationMessage, NotificationDate)
        VALUES (NEW.CustomerID, 'Your account balance has fallen below $1000. Please be aware of the interest rate change.', NOW());
    END IF;
END;

//

-- 6.2  Update manager details
DELIMITER //
CREATE TRIGGER update_manager_details AFTER UPDATE ON Employees FOR EACH ROW 
BEGIN     
    IF NEW.ManagerSSN IS NOT NULL AND OLD.ManagerSSN <> NEW.ManagerSSN THEN
        UPDATE Branches 
        SET ManagerSSN = NEW.ManagerSSN 
        WHERE BranchID = (SELECT BranchID FROM Employees WHERE ManagerSSN = NEW.ManagerSSN LIMIT 1);
    END IF;
END;

//
