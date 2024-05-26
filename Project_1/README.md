
**Databse System Project 1**

In this project, you will get started on how to use a relational DBMS. You can either use the ORACLE RDBMS, or the MySQL system (if you want to use a different system, check with the instructor first). You will use the interactive SQLPLUS facility, and the SQL programming facility, by creating tables, populating them with data, and querying and updating the tables. You should do the following:

1. Create the following tables for the World Cup SOCCER (upto 2014 information) database whose schema diagram is specified below: WorldCups, WorldCupMatches, and WorldCupPlayers. Write your CREATE TABLE statements in a text file and execute the commands from the file through SQLPLUS. You should capture the execution in a spool file that will be turned in. Specify appropriate key and referential integrity constraints. The data types for each attribute can be inferred from the data sheet provided. Primary keys have been underlines and referential integrity constraints have been given at the end. Attributes in each table have been separated by comma.

1. Write one or more database programs to **load the records** that will be provided to you into each of the tables that you created.  You can use any programming or scripting language you are familiar with (JAVA with JDBC, PHP, Python, etc.).

1. Write down the queries for the English queries that are listed later. Execute each query and display its results. Capture your commands in spool files for turning in.

1. Execute 3 more Insert commands that attempt to insert 3 more records, such that the records **violate the integrity constraints**. Make each of the 3 records violate a *different type* of integrity constraint. Capture your commands in spool files for turning in.

1. Execute a SQL command to Delete a record that violates a referential integrity constraint. Capture your command in a spool file for turning in.

1. Repeat 5, but Insert three new records that **do not violate any integrity constraints**. Capture your commands in spool files for turning in.

You should upload the Spool files to Canvas as part of the assignment, including creating the tables and the query results. You should also turn in the source code for the programming part of the assignment for loading the data. 

Document your output when needed by writing down an explanation for each step (by editing the spool file); for example, explain the integrity constraints violated in item 5.

Make a zip file with all the files together and submit it through canvas.

Important Notes:

1) This project is an **individual** project.
1) Copying from other students is not permitted and will result in a grade of zero for the entire project.

Due Date: **October 14, 2023** is the due date for submitting all items 1 through 6 above. (Note: it will be better if you try some or all of the queries before the test so you can practice for the test).

Submit your assignment in canvas any time before midnight of the due date. You should follow the instructions on how to turn in your project (One Zipped folder containing all files together). 

Late policy: -5% out of 100 for each day late.

**For item 3)**

Apply the following queries and display the result of each query

1) Print the name of the country, year it was played, and place where it was played for the country that won maximum number of times with the given data.

1) Print the player details who scored the maximum goal in wining matches

1) Print the world cup year, player who scored maximum goals in any match and order by the number of goals

1) Retrieve the names of countries participated (qualified) most number of times in 21<sup>st</sup> century.

1) How many times (years) USA qualified to play world cups?

1) How many times USA has played a game as away team?

1) Who has scored maximum number of goals?

1) Which city has hosted the game most number of times?

1) Find all the matches played with country ‘Brazil’.

1) Retrieve the names of the players who have scored at least one goal, the player’s country, and the number of goals each player scored. Order the result by number of goals scored in descending order.

1) Repeat 10. But only for the players who have more than 2 goals.

1) Make a list of participating countries and their population, ordered in descending order of population.



**WORLD CUPS**

**Year**, Country,	Winner,	Runners-Up,	Third,	Fourth,	GoalsScored,	QualifiedTeams,	MatchesPlayed,	Attendance


**WORD CUP MATCHES**

Year, Datetime,  Stage, Stadium, City, HomeTeamName, HomeTeamGoals, AwayTeamGoals, AwayTeamName, WinConditions, Attendance, Half-time Home Goals, Half-time Away Goals, Referee, Assistant1, Assistant 2, **RoundID, MatchID**, Home Team Initials, Away Team Initials



**WORLD CUP PLAYERS**

**RoundID**,	**MatchID,**	Team Initials,	Coach Name,	Line-up,	Shirt Number,	Player Name,	Position,	Event



REFERENTIAL INTEGRITIES

1. WORLD\_CUP\_MATCHES.YEAR REFERENCES WORLD\_CUPS.YEAR
1. WORLD\_CUP\_PLAYERS.ROUND\_ID REFERENCES WORLD\_CUP\_MATCHES.ROUND\_ID
1. WORLD\_CUP\_PLAYERS.MATCHCH\_ID REFERENCES WORLD\_CUP\_MATCHES.MATCH\_ID





