SELECT
    E.EmployeeID,
    E.Name AS BankerName,
    E.Address,
    E.Telephone,
    COUNT(DISTINCT C.CustomerID) AS CustomerCount,
    MAX(A.Balance) AS HighestAccountBalance
FROM
    Employees E
JOIN
    Customers C ON E.EmployeeID = C.BranchID
LEFT JOIN
    Accounts A ON C.CustomerID = A.CustomerID
GROUP BY
    E.EmployeeID, E.Name
ORDER BY
    HighestAccountBalance DESC
LIMIT 5;
