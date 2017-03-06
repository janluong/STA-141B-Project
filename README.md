## STA 141B Project

Janice Luong and Sierra Tevlin analyzed the Lahman 2015 baseball data. We analyzed data from 2006 to 2016 because 2006 was the year after any names changes had happened (last name change was in 2005). We will primarily focus on the player’s and a little bit on team statistics (number of hits, pitches, etc...) so we can get an idea of how well a player and teams performs throughout the years and what kind of strategies are popular or successful among different teams.

Here are the World Series Winners from 2006 to 2015

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>teamID</th>
      <th>yearID</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>SLN</td>
      <td>2006</td>
    </tr>
    <tr>
      <td>BOS</td>
      <td>2007</td>
    </tr>
    <tr>
      <td>PHI</td>
      <td>2008</td>
    </tr>
    <tr>
      <td>NYA</td>
      <td>2009</td>
    </tr>
    <tr>
      <td>SFN</td>
      <td>2010</td>
    </tr>
    <tr>
      <td>SLN</td>
      <td>2011</td>
    </tr>
    <tr>
      <td>SFN</td>
      <td>2012</td>
    </tr>
    <tr>
      <td>BOS</td>
      <td>2013</td>
    </tr>
    <tr>
      <td>SFN</td>
      <td>2014</td>
    </tr>
    <tr>
      <td>KCA</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>

Who had the most hits in a given season?

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Last Name</th>
      <th>First Name</th>
      <th>Team</th>
      <th>Year</th>
      <th>Number of Hits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Suzuki</td>
      <td>Ichiro</td>
      <td>Baltimore Orioles</td>
      <td>2006</td>
      <td>224</td>
    </tr>
    <tr>
      <td>Suzuki</td>
      <td>Ichiro</td>
      <td>Baltimore Orioles</td>
      <td>2007</td>
      <td>238</td>
    </tr>
    <tr>
      <td>Pedroia</td>
      <td>Dustin</td>
      <td>Baltimore Orioles</td>
      <td>2008</td>
      <td>213</td>
    </tr>
    <tr>
      <td>Suzuki</td>
      <td>Ichiro</td>
      <td>Baltimore Orioles</td>
      <td>2009</td>
      <td>225</td>
    </tr>
    <tr>
      <td>Suzuki</td>
      <td>Ichiro</td>
      <td>Baltimore Orioles</td>
      <td>2010</td>
      <td>214</td>
    </tr>
    <tr>
      <td>Gonzalez</td>
      <td>Adrian</td>
      <td>Baltimore Orioles</td>
      <td>2011</td>
      <td>213</td>
    </tr>
    <tr>
      <td>Jeter</td>
      <td>Derek</td>
      <td>Baltimore Orioles</td>
      <td>2012</td>
      <td>216</td>
    </tr>
    <tr>
      <td>Beltre</td>
      <td>Adrian</td>
      <td>Baltimore Orioles</td>
      <td>2013</td>
      <td>199</td>
    </tr>
    <tr>
      <td>Altuve</td>
      <td>Jose</td>
      <td>Baltimore Orioles</td>
      <td>2014</td>
      <td>225</td>
    </tr>
    <tr>
      <td>Gordon</td>
      <td>Dee</td>
      <td>Baltimore Orioles</td>
      <td>2015</td>
      <td>205</td>
    </tr>
  </tbody>
</table>

Which team had the most and least home runs in a given season?

Teams who had the most homeruns:

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Team</th>
      <th>Year</th>
      <th>Home Runs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Chicago White Sox</td>
      <td>2006</td>
      <td>236</td>
    </tr>
    <tr>
      <td>Milwaukee Brewers</td>
      <td>2007</td>
      <td>231</td>
    </tr>
    <tr>
      <td>Chicago White Sox</td>
      <td>2008</td>
      <td>235</td>
    </tr>
    <tr>
      <td>New York Yankees</td>
      <td>2009</td>
      <td>244</td>
    </tr>
    <tr>
      <td>Toronto Blue Jays</td>
      <td>2010</td>
      <td>257</td>
    </tr>
    <tr>
      <td>New York Yankees</td>
      <td>2011</td>
      <td>222</td>
    </tr>
    <tr>
      <td>New York Yankees</td>
      <td>2012</td>
      <td>245</td>
    </tr>
    <tr>
      <td>Baltimore Orioles</td>
      <td>2013</td>
      <td>212</td>
    </tr>
    <tr>
      <td>Baltimore Orioles</td>
      <td>2014</td>
      <td>211</td>
    </tr>
    <tr>
      <td>Toronto Blue Jays</td>
      <td>2015</td>
      <td>232</td>
    </tr>
  </tbody>
</table>

Teams who had the least homeruns:

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Team</th>
      <th>Year</th>
      <th>Home Runs</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Kansas City Royals</td>
      <td>2006</td>
      <td>124</td>
    </tr>
    <tr>
      <td>Kansas City Royals</td>
      <td>2007</td>
      <td>102</td>
    </tr>
    <tr>
      <td>San Francisco Giants</td>
      <td>2008</td>
      <td>94</td>
    </tr>
    <tr>
      <td>New York Mets</td>
      <td>2009</td>
      <td>95</td>
    </tr>
    <tr>
      <td>Seattle Mariners</td>
      <td>2010</td>
      <td>101</td>
    </tr>
    <tr>
      <td>San Diego Padres</td>
      <td>2011</td>
      <td>91</td>
    </tr>
    <tr>
      <td>San Francisco Giants</td>
      <td>2012</td>
      <td>103</td>
    </tr>
    <tr>
      <td>Miami Marlins</td>
      <td>2013</td>
      <td>95</td>
    </tr>
    <tr>
      <td>Kansas City Royals</td>
      <td>2014</td>
      <td>95</td>
    </tr>
    <tr>
      <td>Atlanta Braves</td>
      <td>2015</td>
      <td>100</td>
    </tr>
  </tbody>
</table>




Database downloaded from [jknecht baseball archive](https://github.com/jknecht/baseball-archive-sqlite/blob/master/lahman2015.sqlite)