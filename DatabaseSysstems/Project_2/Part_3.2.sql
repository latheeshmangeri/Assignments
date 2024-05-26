SELECT
    B.BranchName,
    C.CustomerID,
    C.Name AS CustomerName,
    A.AccountNumber,
    A.AccountType,
    A.Balance,
    L.LoanAmount
FROM
    Branches B
JOIN
    Customers C ON B.BranchID = C.BranchID
LEFT JOIN
    Accounts A ON C.CustomerID = A.CustomerID
LEFT JOIN
    Loans L ON C.CustomerID = L.CustomerID
    
LIMIT 5;

