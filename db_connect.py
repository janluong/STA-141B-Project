import sqlite3
import pandas as pd

# Reads database
baseball_con = sqlite3.connect("data/lahman2015.sqlite")

# Who won the World Series for each year?
WSWinners = pd.read_sql_query("SELECT teamID, yearID, WSWin from Teams WHERE (yearID > 2005 AND yearID < 2016) AND WSWin = 'Y' GROUP BY yearID"
                              , baseball_con)

# Who had the most hits in a given season?
player_most_hits =  pd.read_sql_query("SELECT playerID, yearID, MAX(H) from Batting WHERE (yearID > 2005 AND yearID < 2016) GROUP BY yearID LIMIT 20"
                                      , baseball_con)

# Who were the AL and NL winners for each year?
division_win =  pd.read_sql_query("SELECT DivWin, yearID, teamID FROM Teams WHERE DivWin = 'Y' AND (yearID > 2005 AND yearID < 2016)"
                                  , baseball_con)

# Which team had the most and least home runs in a given season?
max_HR = pd.read_sql_query("SELECT teamID, yearID, MAX(HR) as 'Home Runs' FROM Teams WHERE (yearID > 2005 AND yearID < 2016) GROUP BY yearID LIMIT 10"
                           , baseball_con)
min_HR = pd.read_sql_query("SELECT teamID, yearID, MIN(HR) as 'Home Runs' FROM Teams WHERE (yearID > 2005 AND yearID < 2016) GROUP BY yearID LIMIT 10"
                           , baseball_con)

# Find the 20 best hitters and 20 worst hitters in all of baseball.
print pd.read_sql_query("SELECT playerID, teamID, yearID, SUM(H) as 'Number of Hits' FROM Batting WHERE (yearID > 2005 AND yearID < 2016) GROUP BY playerID ORDER BY SUM(H) DESC LIMIT 20"
                                    , baseball_con)
worst_20_hitters = pd.read_sql_query("SELECT playerID, teamID, yearID, SUM(H) as 'num_hits' FROM Batting WHERE H IS NOT NULL  AND (yearID > 2005 AND yearID < 2016)GROUP BY playerID ORDER BY SUM(H) LIMIT 20"
                                     , baseball_con)

# Test Change