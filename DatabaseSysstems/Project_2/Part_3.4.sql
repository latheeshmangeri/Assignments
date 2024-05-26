SELECT
    L.LoanNumber,
    L.BranchID,
    A.CustomerID,
    B.BranchName,
    (L.LoanAmount - COALESCE(SUM(LP.PaymentAmount), 0)) AS RemainingBalance
FROM
    Loans L
JOIN
    Branches B ON L.BranchID = B.BranchID
JOIN
    Accounts A ON L.CustomerID = A.CustomerID
LEFT JOIN
    LoanPayments LP ON L.LoanNumber = LP.LoanNumber
GROUP BY
    L.LoanNumber, L.BranchID, A.CustomerID, B.BranchName
ORDER BY
    RemainingBalance DESC
LIMIT 5;
