import sqlite3
import pandas as pd

# Reads database
baseball_con = sqlite3.connect("data/lahman2015.sqlite")

# Who won the World Series for each year?
WSWinners = pd.read_sql_query("SELECT teamID, yearID, WSWin from Teams WHERE WSWin = 'Y' GROUP BY yearID"
                              , baseball_con)

# Who had the most hits in a given season?
player_most_hits =  pd.read_sql_query("SELECT playerID, yearID, MAX(H) from Batting GROUP BY yearID LIMIT 20"
                                      , baseball_con)

# Who were the AL and NL winners for each year?
division_win =  pd.read_sql_query("SELECT DivWin, yearID, teamID FROM Teams WHERE DivWin = 'Y'"
                                  , baseball_con)

# Which team had the most and least home runs in a given season?
max_HR = pd.read_sql_query("SELECT teamID, yearID, MAX(HR) as 'Home Runs' FROM Teams GROUP BY yearID LIMIT 10"
                           , baseball_con)
min_HR = pd.read_sql_query("SELECT teamID, yearID, MIN(HR) as 'Home Runs' FROM Teams GROUP BY yearID LIMIT 10"
                           , baseball_con)

# Find the 20 best hitters and 20 worst hitters in all of baseball.
best_20_hitters = pd.read_sql_query("SELECT playerID, teamID, SUM(H) as 'Number of Hits' FROM Batting GROUP BY playerID ORDER BY SUM(H) DESC LIMIT 20"
                                    , baseball_con)

#baseball_con.execute("DELETE FROM Batting WHERE H IS NULL OR H = '0'")

print pd.read_sql_query("SELECT playerID, teamID, SUM(H) as 'num_hits' FROM Batting GROUP BY playerID ORDER BY SUM(H) LIMIT 20"
                                   , baseball_con)
