
**Project 2 Description**

In this project, you will design and implement a database for a banking system. The detailed requirements for this system is as follows. You will first design an ER/EER schema diagram for this database application. Then, you will map the ER/EER schema into a relational database schema and implement it on ORACLE/MySQL in Omega. Finally, you will load some data into your database, and create some queries and update transactions.

Assume that the following requirements were collected for this application:

1. The bank is organized into branches. Each branch is located in a city and is identified a name. The bank monitors the assets of the branch.
1. Bank has several types of customers, individuals and businesses. The individual customers are identified by their Social Security number. The bank stored it's customers name and address. Similarly the businesses are identified with their unique name and listed address.
1. The customers may have accounts and can take out loans. And the customers may have their personal bankers who acts as their loan officer. 
1. Bank will have employees who are identified by their Social Security numbers. The name, address and telephone number of employees are also maintained. The bank also keeps track of employees’ dependents and also the manager of each employee. The bank also keeps track of employees’ start date and length of employment. 
1. The bank offers two types of accounts savings and checking accounts for individuals and business accounts for businesses. The accounts can be held by more than one customer and the customer can have more than one account. The account is identified by an unique account number. The bank maintains record of each account’s balance and the most recent date on which the account was accessed by each customer holding the account. In addition each savings account has an interest rate and overdrafts are recorded for each checking account. 
1. A loan originates at a particular branch and can be held by one or more customers. The loan is identified by a unique loan number. For each loan, the bank keeps track of the loan amount and the loan payments. Although a loan payment number does not uniquely identify a particular payment among those for all the banks loans, a payment number does identify a particular payment for a specific loan. The date and amount are recorded for each payment.


In **first part** of the assignment, you will first design an EER schema diagram based upon the Bank database requirements specified above and create an EER schema diagram and documentation report describing your design choices. As part of this assignment, you should identify any missing or incomplete requirements, and explicitly state them in your documentation. You should also explicitly state any assumptions you made that were not part of the requirements listed above. (33%)

The **second part** of the assignment will be to map the EER schema design to a relational database schema, and create the tables corresponding to the relational schema using the ORACLE/MySQL DBMS. You will add to your report a listing of the CREATE TABLE statements. Specify as many constraints (key, referential integrity) as you can in the relational schema. You should state the choices you made during the EER-to-relational mapping, and the reasons for your choices. (33%)

The **third part** of the project is to load some data into the database, and apply certain update transactions and retrieval queries. You will create your own data. Include at least 10 branches, 40 employees, and at least 15 accounts of various types. (34%)

The following are the tasks for the third part of the project:

1. Load some initial data (as discussed above) into the database tables that you created in Part 2 of the assignment. You can either write a loading program, or use SQL/PLUS (insert command). Your data should be kept in files so that it can easily be reloaded during debugging. The data format should be designed by you. (Note: You can also use the transactions created by you in item 3 below to load some of the data).
1. Generate a report listing all branches with their customers, their account details and the loaned amount if there is. 
1. Report showing top 5 personal bankers who has have customers who holds highest account balance. 
1. Report showing top 5 accounts that owes (difference of loaned amount and sum of all payment amounts) the most to the bank with their corresponding branches that loaned that amount.
1. Write the following database update transactions using any suitable programming or scripting language (JAVA/JDBC, PHP or Python).
   1. Create a new account for a business.
   1. Create a new account for an individual with an initial deposit of $1000.
   1. Issue a loan of $20, 000 from a branch to a specific customer from a specific city.
1. Write following two triggers – 
   1. To notify a member about the interest rate change due to balance falling below certain amount, say $1000. 
   1. Updating the manager details (manager SSN) in the event of a new manager replacing one existing one.
1. Each transaction should have a user friendly interface to enter the information needed by the transaction. This can either be a Web-based interface, a command line interface, or a forms interface.

Due Dates:

1. Parts 1 and 2 Due Date: Sunday Nov 12, 2023. This should include for Part 1 the EER diagrams for your designs as well as documentation describing any assumptions you made, and the reasons for your design choices. Draw the EER diagrams using the notation in the textbook. You can also use UML class diagrams notation. You can use any drawing tool for drawing your diagrams. For part 2, what you turn in should include your relational schema diagram design and your CREATE table statements, and documentation describing your EER-to-relational mapping choices.
1. Part 3 Due Date: Sunday Nov 19, 2023. This will include a demo demonstrating that your implementation works, as well as demonstrating your transactions to the grader. Source code of all your transactions should be submitted, as well as the data files. A demo schedule will be determined before the due date.

The work need to be submitted in Canvas, for which the TA will create a link and make an announcement. 

Late penalty: -5% per day late for each parts.

Project teams: Each project can be done in a team of 2 persons, or individually.
