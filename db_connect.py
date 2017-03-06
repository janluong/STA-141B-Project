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
best_20_hitters = pd.read_sql_query("SELECT playerID, teamID, yearID, SUM(H) as 'Number of Hits' FROM Batting WHERE (yearID > 2005 AND yearID < 2016) GROUP BY playerID ORDER BY SUM(H) DESC LIMIT 20"
                                    , baseball_con)
worst_20_hitters = pd.read_sql_query("SELECT playerID, teamID, yearID, SUM(H) as 'num_hits' FROM Batting WHERE (H IS NOT NULL AND H > 0)  AND (yearID > 2005 AND yearID < 2016)GROUP BY playerID ORDER BY SUM(H) LIMIT 20"
                                     , baseball_con)

# For 20 best and 20 worst hitters, find the ball-strike count for each hitter.
# Find the percentage of fastballs for each player.
most_strike_out = pd.read_sql_query("SELECT playerID, teamID, yearID, MAX(SO), H, (MAX(SO) * 1.0) / (MAX(SO) + H) as 'Percentage of Strike Outs' FROM Batting WHERE (yearID > 2005 AND yearID < 2016) GROUP BY playerID ORDER BY SO DESC LIMIT 20"
                        , baseball_con)

least_strike_out = pd.read_sql_query("SELECT playerID, teamID, yearID, MIN(SO), H, (MAX(SO) * 1.0) / (MAX(SO) + H) as 'Percentage of Strike Outs' FROM Batting WHERE (yearID > 2005 AND yearID < 2016) GROUP BY playerID ORDER BY SO DESC LIMIT 20"
                                     , baseball_con)

# Which teams had the most amount of  stolen bases in a given season?
most_SB = pd.read_sql_query("SELECT MAX(SB), name, yearID FROM Teams WHERE (yearID > 2005 AND yearID < 2016) GROUP BY yearID"
                            , baseball_con)

# What team pitch the most strike outs for the season?
max_SOA = pd.read_sql_query("SELECT MAX(SOA), name, yearID FROM Teams WHERE (yearID > 2005 AND yearID < 2016) GROUP BY yearID"
                            , baseball_con)

# Who were the top players had the most home runs in the a given season?
top_player_HR = pd.read_sql_query("SELECT MAX(HR), teamID, playerID, yearID FROM Batting WHERE (yearID > 2005 AND yearID < 2016) GROUP BY yearID"
                                  , baseball_con)

# Which pitcher had the most and least stolen bases allowed each season? Are they left or right handed?
most_SB_given = pd.read_sql_query("SELECT t.playerID, m.throws, t.teamID, t.yearID, MAX(t.SB) FROM (SELECT playerID, teamID, SUM(SB) as SB, yearID FROM FieldingPost WHERE (yearID > 2005 AND yearID < 2016) AND SB IS NOT NULL GROUP BY playerID, yearID ORDER BY SUM(SB) DESC LIMIT 20) t LEFT JOIN Master m ON m.playerID = t.playerID GROUP BY yearID"
                                  , baseball_con)

print pd.read_sql_query("SELECT t.playerID, m.throws, t.teamID, t.yearID, MIN(t.SB) FROM (SELECT playerID, teamID, SUM(SB) as SB, yearID FROM FieldingPost WHERE (yearID > 2005 AND yearID < 2016) AND SB IS NOT NULL GROUP BY playerID, yearID ORDER BY SUM(SB) DESC LIMIT 20) t LEFT JOIN Master m ON m.playerID = t.playerID GROUP BY yearID"
                                  , baseball_con)
