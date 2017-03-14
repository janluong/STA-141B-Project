import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Reads database
baseball_con = sqlite3.connect("data/lahman2015.sqlite")

# Who won the World Series for each year?
WSWinners = pd.read_sql_query("SELECT name as 'Team', R as 'Runs', HR as 'Homeruns', yearID as 'Year', WSWin from Teams WHERE (yearID > 2005 AND yearID < 2016) AND WSWin = 'Y' GROUP BY yearID"
                              , baseball_con)

WSWinners_dropped = WSWinners.drop('WSWin', 1)
print WSWinners_dropped.to_html(index = False)

# Who were the AL and NL winners for each year?
division_win_AL =  pd.read_sql_query("SELECT yearID as 'Year', name as 'Team', divID as 'Division' FROM Teams WHERE LgWin = 'Y' AND (yearID > 2005 AND yearID < 2016) AND lgID = 'AL' GROUP BY yearID"
                                     , baseball_con)
division_win_NL =  pd.read_sql_query("SELECT yearID as 'Year', name as 'Team', divID as 'Division' FROM Teams WHERE LgWin = 'Y' AND (yearID > 2005 AND yearID < 2016) AND lgID = 'NL' GROUP BY yearID"
                                     , baseball_con)

print division_win_AL.to_html(index = False)

count_AL = sns.countplot(x = "Division", data = division_win_AL)
count_AL.set(xlabel='Divison', ylabel='Counts')
sns.plt.title('AL Division Winners 2006 - 2015')
plt.show()

print division_win_NL.to_html(index = False)

count_NL = sns.countplot(x = "Division", data = division_win_NL)
count_NL.set(xlabel='Divison', ylabel='Counts')
sns.plt.title('NL Division Winners 2006 - 2015')
plt.show()

# Which team had the most and least home runs in a given season?
max_HR = pd.read_sql_query("SELECT name as 'Team', yearID as 'Year', R as 'Runs', MAX(HR) as 'Homeruns' FROM Teams WHERE (yearID > 2005 AND yearID < 2016) GROUP BY yearID LIMIT 10"
                           , baseball_con)
print max_HR.to_html(index = False)

plt.rcParams['figure.figsize'] = (10, 10)
sns.set(font_scale = 1.5)

most_HR_plot = sns.FacetGrid(max_HR, hue = "Team", size = 8.5)
most_HR_plot.map(plt.scatter, "Year", "Homeruns").add_legend()
sns.plt.title('Teams with most Homeruns from 2006 to 2015')
plt.show()

min_HR = pd.read_sql_query("SELECT name as 'Team', yearID as 'Year', R as 'Runs', MIN(HR) as 'Homeruns' FROM Teams WHERE (yearID > 2005 AND yearID < 2016) GROUP BY yearID LIMIT 10"
                           , baseball_con)
#print min_HR.to_html(index = False)

min_HR_plot = sns.FacetGrid(min_HR, hue = "Team", size = 8.5)
min_HR_plot.map(plt.scatter, "Year", "Homeruns").add_legend()
sns.plt.title('Teams with least Homeruns from 2006 to 2015')
plt.show()

# Find the 20 best hitters in all of baseball.
best_20_hitters = pd.read_sql_query("SELECT t.divID as 'Divison', t.lgID as 'League', m.nameLast as 'Last Name', m.nameFirst as 'First Name', t.name as 'Team', SUM(b.H) as 'Number of Hits', m.birthcountry as 'Home Country' FROM Batting b LEFT JOIN Teams t ON b.teamID = t.teamID LEFT JOIN Master m ON b.playerID = m.playerID WHERE (b.yearID > 2005 AND b.yearID < 2016) GROUP BY b.playerID ORDER BY SUM(b.H) DESC LIMIT 20"
                                    , baseball_con)

print best_20_hitters.to_html(index = False)

sns.countplot(x = "Home Country", data = best_20_hitters)
plt.show()

# Which teams had the most amount of stolen bases for each season?
most_SB = pd.read_sql_query("SELECT yearID as 'Year', name as 'Team', MAX(SB) as '# of Stolen Bases' FROM Teams WHERE (yearID > 2005 AND yearID < 2016) GROUP BY yearID"
                            , baseball_con)

print most_SB.to_html(index = False)

# What team pitched the most strik outs for each season?
max_SOA = pd.read_sql_query("SELECT yearID as'Year', name as 'Team', MAX(SOA) '# of Strike Outs' FROM Teams WHERE (yearID > 2005 AND yearID < 2016) GROUP BY yearID"
                            , baseball_con)

print max_SOA.to_html(index = False)

# Who were the top players who had the most homeruns each season?
top_player_HR = pd.read_sql_query("SELECT b.yearID as 'Year', t.name as 'Team', m.nameLast as 'Last Name', m.nameFirst as 'First Name', MAX(b.HR) as '# of Homeruns' FROM Batting b LEFT JOIN Teams t ON b.teamID = t.teamID LEFT JOIN Master m ON b.playerID = m.playerID WHERE (b.yearID > 2005 AND b.yearID < 2016) GROUP BY b.yearID"
                                  , baseball_con)

print top_player_HR.to_html(index = False)

# Which pitcher had the most and least stolen bases allowed each season? Are they left or right handed?
most_SB_given = pd.read_sql_query("SELECT t.playerID, m.throws, t.teamID, t.yearID, MAX(t.SB) FROM (SELECT playerID, teamID, SUM(SB) as SB, yearID FROM FieldingPost WHERE (yearID > 2005 AND yearID < 2016) AND SB IS NOT NULL GROUP BY playerID, yearID ORDER BY SUM(SB) DESC LIMIT 20) t LEFT JOIN Master m ON m.playerID = t.playerID GROUP BY yearID"
                                  , baseball_con)

least_SB_given = pd.read_sql_query("SELECT t.playerID, m.throws, t.teamID, t.yearID, MIN(t.SB) FROM (SELECT playerID, teamID, SUM(SB) as SB, yearID FROM FieldingPost WHERE (yearID > 2005 AND yearID < 2016) AND SB IS NOT NULL GROUP BY playerID, yearID ORDER BY SUM(SB) DESC LIMIT 20) t LEFT JOIN Master m ON m.playerID = t.playerID GROUP BY yearID"
                                  , baseball_con)

#What team pitched the most shutouts for a given season?
most_shutouts = pd.read_sql_query("SELECT name as 'Team', yearID as 'Year', MAX(sho) as 'Shutouts' FROM Teams WHERE (yearID > 2005 AND yearID < 2016) GROUP BY yearID"
                                  , baseball_con)

print most_shutouts

plt.rcParams['figure.figsize'] = (10, 10)
sns.set(font_scale = 1.5)

most_sho_plot = sns.FacetGrid(most_shutouts, hue = "Team", size = 8.5)
most_sho_plot.map(plt.scatter, "Year", "Shutouts").add_legend()
sns.plt.title('Teams with most Shutouts from 2006 to 2015')
plt.show()