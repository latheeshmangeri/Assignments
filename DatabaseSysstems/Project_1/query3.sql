-- Using Database lxm6009
use lxm6009;

-- Printing Tables from Database
Show tables;

-- Printing table world_cups
show columns from world_cups;

-- Printing table world_cup_matches
show columns from world_cup_matches;

-- Printing Tables world_cup_players
show columns from world_cup_players;

-- 1.Print the name of the country, year it was played, and place where it was played for the country that won maximum number of times with the given data.
SELECT Country, Year, Winner
FROM world_cups
WHERE Winner = (
    SELECT Winner
    FROM world_cups
    GROUP BY Winner
    ORDER BY COUNT(*) DESC
    LIMIT 1
);

-- 2.Print the player details who scored the maximum goal in wining matches
SELECT
  PlayerName,
  TeamInitials,
  COUNT(*) AS GoalsScored
FROM WORLD_CUP_PLAYERS
WHERE RoundID IN (
  SELECT RoundID
  FROM WORLD_CUP_MATCHES
  WHERE HomeTeamGoals > AwayTeamGoals
)
GROUP BY PlayerName, TeamInitials
ORDER BY GoalsScored DESC
LIMIT 1;

-- 3.Print the world cup year, player who scored maximum goals in any match and order by the number of goals
SELECT
  m.Year,
  p.PlayerName,
  COUNT(*) AS GoalsScored
FROM WORLD_CUP_PLAYERS p
JOIN WORLD_CUP_MATCHES m ON p.RoundID = m.RoundID
GROUP BY m.Year, p.PlayerName
ORDER BY GoalsScored DESC
limit 1;

-- 4.Retrieve the names of countries participated (qualified) most number of times in 21st century.
SELECT
  Country,
  Year,
  COUNT(*) AS Participations
FROM WORLD_CUPS
WHERE Year >= 2000
GROUP BY Country, Year
ORDER BY Participations DESC
LIMIT 1;

-- 5.How many times (years) USA qualified to play world cups?
SELECT   
	Year,   COUNT(*) AS Appearances 
    FROM WORLD_CUPS 
    WHERE Country ='USA' 
    GROUP BY Year ORDER BY Year;
    
-- 6. How many times USA has played a game as away team?
SELECT   
	COUNT(*) AS AwayGames 
    FROM WORLD_CUP_MATCHES 
    WHERE AwayTeamName= 'USA';

-- 7.Who has scored maximum number of goals?
SELECT
  PlayerName,
  COUNT(*) AS GoalsScored
FROM WORLD_CUP_PLAYERS
GROUP BY PlayerName
ORDER BY GoalsScored DESC;

-- 8.Which city has hosted the game most number of times?
SELECT
  City,
  COUNT(*) AS GamesPlayed
FROM WORLD_CUP_MATCHES
GROUP BY City
ORDER BY GamesPlayed DESC;

-- 9.Find all the matches played with country ‘Brazil’.
SELECT *
FROM WORLD_CUP_MATCHES
WHERE HomeTeamName = 'Brazil' OR AwayTeamName = 'Brazil';

-- 10.Retrieve the names of the players who have scored at least one goal, the player’s country, and the number of goals each player scored. Order the result by number of goals scored in descending order.
SELECT
  PlayerName,
  COUNT(*) AS GoalsScored
FROM WORLD_CUP_PLAYERS
GROUP BY PlayerName
ORDER BY GoalsScored DESC;

-- 11.Repeat 10. But only for the players who have more than 2 goals.
SELECT
  PlayerName,
  COUNT(*) AS GoalsScored
FROM WORLD_CUP_PLAYERS
GROUP BY PlayerName
HAVING GoalsScored > 2
ORDER BY GoalsScored DESC;

-- 12.Make a list of participating countries and their population, ordered in descending order of population.
SELECT   
	HOMETeamInitials AS Country,   
    SUM(Attendance) AS Attendance FROM WORLD_CUP_MATCHES 
    GROUP BY HOMETeamInitials ORDER BY Attendance DESC;
