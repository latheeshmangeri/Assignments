-- 4.1
INSERT INTO WORLD_CUPS (Year, Country, Winner, Runners_Up, Third)  VALUES (1930, 'Qatar', 'Argentina', 'France', 'Croatia');
-- 4.2
INSERT INTO WORLD_CUP_PLAYERS (RoundID, MatchID, TeamInitials, CoachName, Line_up, ShirtNumber, PlayerName, Position, Event) VALUES (4, 1, 'BRA', 'CoachA', 'Starting XI', 10, 'Player X', 'Midfielder', 'Goal');
-- 4.3
INSERT INTO WORLD_CUP_MATCHES (Year, Datetime, Stage, Stadium, City, HomeTeamName, HomeTeamGoals, AwayTeamGoals, AwayTeamName, WinConditions, Attendance, Half_timeHomeGoals, Half_timeAwayGoals, Referee, Assistant1, Assistant2, RoundID, MatchID, HomeTeamInitials, AwayTeamInitials)
VALUES (2023, '2023-10-12 15:00:00', 'Group Stage', 'StadiumY', 'CityY', 'TeamA', -1, 0, 'TeamB', 'Normal Time', 45000, 0, 0, 'RefY', 'Asst1', 'Asst2', 4, 11, 'HXA', 'AYB');