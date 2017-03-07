import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reads database
baseball_con = sqlite3.connect("data/lahman2015.sqlite")

# Who won the World Series for each year?
WSWinners = pd.read_sql_query("SELECT name as 'Team', yearID as 'Year', WSWin from Teams WHERE (yearID > 2005 AND yearID < 2016) AND WSWin = 'Y' GROUP BY yearID"
                              , baseball_con)
WSWinners_dropped = WSWinners.drop('WSWin', 1)
#print WSWinners_dropped.to_html(index = False)

# Who had the most hits in a given season?
player_most_hits =  pd.read_sql_query("SELECT m.nameLast as 'Last Name', m.nameFirst as 'First Name', b.yearID as 'Year', MAX(b.H) as 'Number of Hits' from Batting b LEFT JOIN Master m ON b.playerID = m.playerID LEFT JOIN Teams t ON b.yearID = t.yearID WHERE (b.yearID > 2005 AND b.yearID < 2016) GROUP BY b.yearID"
                                      , baseball_con)
#print player_most_hits.to_html(index = False)

# Who were the AL and NL winners for each year?
division_win_AL =  pd.read_sql_query("SELECT yearID as 'Year', name as 'Team', lgID as 'League' FROM Teams WHERE LgWin = 'Y' AND (yearID > 2005 AND yearID < 2016) AND lgID = 'AL' GROUP BY yearID"
                                  , baseball_con)
division_win_NL =  pd.read_sql_query("SELECT yearID as 'Year', name as 'Team', lgID as 'League' FROM Teams WHERE LgWin = 'Y' AND (yearID > 2005 AND yearID < 2016) AND lgID = 'NL' GROUP BY yearID"
                                  , baseball_con)
#print division_win_AL.to_html(index = False)
print division_win_NL.to_html(index = False)


# Which team had the most and least home runs in a given season?
max_HR = pd.read_sql_query("SELECT name as 'Team', yearID as 'Year', MAX(HR) as 'Homeruns' FROM Teams WHERE (yearID > 2005 AND yearID < 2016) GROUP BY yearID LIMIT 10"
                           , baseball_con)
#print max_HR.to_html(index = False)

#plt.rcParams['figure.figsize'] = (10, 10)
#sns.set(font_scale = 1.5)

#most_HR_plot = sns.FacetGrid(max_HR, hue = "Team", size = 8.5)
#most_HR_plot.map(plt.scatter, "Year", "Homeruns").add_legend()
#sns.plt.title('Teams with most Homeruns from 2006 to 2015')
#plt.show()

min_HR = pd.read_sql_query("SELECT name as 'Team', yearID as 'Year', MIN(HR) as 'Homeruns' FROM Teams WHERE (yearID > 2005 AND yearID < 2016) GROUP BY yearID LIMIT 10"
                           , baseball_con)
#print min_HR.to_html(index = False)

#min_HR_plot = sns.FacetGrid(min_HR, hue = "Team", size = 8.5)
#min_HR_plot.map(plt.scatter, "Year", "Homeruns").add_legend()
#sns.plt.title('Teams with least Homeruns from 2006 to 2015')
#plt.show()

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

least_SB_given = pd.read_sql_query("SELECT t.playerID, m.throws, t.teamID, t.yearID, MIN(t.SB) FROM (SELECT playerID, teamID, SUM(SB) as SB, yearID FROM FieldingPost WHERE (yearID > 2005 AND yearID < 2016) AND SB IS NOT NULL GROUP BY playerID, yearID ORDER BY SUM(SB) DESC LIMIT 20) t LEFT JOIN Master m ON m.playerID = t.playerID GROUP BY yearID"
                                  , baseball_con)
