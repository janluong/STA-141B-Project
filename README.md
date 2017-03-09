<h2>Introduction</h2>

Janice Luong and Sierra Tevlin analyzed the Lahman 2015 baseball data. We analyzed data from 2006 to 2016 because 2006 was the year after any names changes had happened (last name change was in 2005). We will primarily focus on the player’s and a little bit on team statistics (number of hits, pitches, etc...) so we can get an idea of how well a player and teams performs throughout the years and what kind of strategies are popular or successful among different teams.

<h2>Analyzing the Data</h2>

Here are the World Series Winners from 2006 to 2015

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Team</th>
      <th>Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>St. Louis Cardinals</td>
      <td>2006</td>
    </tr>
    <tr>
      <td>Boston Red Sox</td>
      <td>2007</td>
    </tr>
    <tr>
      <td>Philadelphia Phillies</td>
      <td>2008</td>
    </tr>
    <tr>
      <td>New York Yankees</td>
      <td>2009</td>
    </tr>
    <tr>
      <td>San Francisco Giants</td>
      <td>2010</td>
    </tr>
    <tr>
      <td>St. Louis Cardinals</td>
      <td>2011</td>
    </tr>
    <tr>
      <td>San Francisco Giants</td>
      <td>2012</td>
    </tr>
    <tr>
      <td>Boston Red Sox</td>
      <td>2013</td>
    </tr>
    <tr>
      <td>San Francisco Giants</td>
      <td>2014</td>
    </tr>
    <tr>
      <td>Kansas City Royals</td>
      <td>2015</td>
    </tr>
  </tbody>
</table>

<h3>Who had the most hits in a given season?</h3>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Last Name</th>
      <th>First Name</th>
      <th>Year</th>
      <th>Number of Hits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Suzuki</td>
      <td>Ichiro</td>
      <td>2006</td>
      <td>224</td>
    </tr>
    <tr>
      <td>Suzuki</td>
      <td>Ichiro</td>
      <td>2007</td>
      <td>238</td>
    </tr>
    <tr>
      <td>Pedroia</td>
      <td>Dustin</td>
      <td>2008</td>
      <td>213</td>
    </tr>
    <tr>
      <td>Suzuki</td>
      <td>Ichiro</td>
      <td>2009</td>
      <td>225</td>
    </tr>
    <tr>
      <td>Suzuki</td>
      <td>Ichiro</td>
      <td>2010</td>
      <td>214</td>
    </tr>
    <tr>
      <td>Gonzalez</td>
      <td>Adrian</td>
      <td>2011</td>
      <td>213</td>
    </tr>
    <tr>
      <td>Jeter</td>
      <td>Derek</td>
      <td>2012</td>
      <td>216</td>
    </tr>
    <tr>
      <td>Beltre</td>
      <td>Adrian</td>
      <td>2013</td>
      <td>199</td>
    </tr>
    <tr>
      <td>Altuve</td>
      <td>Jose</td>
      <td>2014</td>
      <td>225</td>
    </tr>
    <tr>
      <td>Gordon</td>
      <td>Dee</td>
      <td>2015</td>
      <td>205</td>
    </tr>
  </tbody>
</table>

<h3>Which team had the most and least home runs in a given season?</h3>

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

<img src="img/Teams-most-homeruns.png">

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

<img src="img/teams-least-homeruns.png">

<h3>Who were the American League winners for each year?</h3>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Year</th>
      <th>Team</th>
      <th>Division</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2006</td>
      <td>Detroit Tigers</td>
      <td>C</td>
    </tr>
    <tr>
      <td>2007</td>
      <td>Boston Red Sox</td>
      <td>E</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Tampa Bay Rays</td>
      <td>E</td>
    </tr>
    <tr>
      <td>2009</td>
      <td>New York Yankees</td>
      <td>E</td>
    </tr>
    <tr>
      <td>2010</td>
      <td>Texas Rangers</td>
      <td>W</td>
    </tr>
    <tr>
      <td>2011</td>
      <td>Texas Rangers</td>
      <td>W</td>
    </tr>
    <tr>
      <td>2012</td>
      <td>Detroit Tigers</td>
      <td>C</td>
    </tr>
    <tr>
      <td>2013</td>
      <td>Boston Red Sox</td>
      <td>E</td>
    </tr>
    <tr>
      <td>2014</td>
      <td>Kansas City Royals</td>
      <td>C</td>
    </tr>
    <tr>
      <td>2015</td>
      <td>Kansas City Royals</td>
      <td>C</td>
    </tr>
  </tbody>
</table>

<img src="img/al-div-winners.png">

<h3>Who were the National League winners for each year?</h3>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Year</th>
      <th>Team</th>
      <th>Division</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2006</td>
      <td>St. Louis Cardinals</td>
      <td>C</td>
    </tr>
    <tr>
      <td>2007</td>
      <td>Colorado Rockies</td>
      <td>W</td>
    </tr>
    <tr>
      <td>2008</td>
      <td>Philadelphia Phillies</td>
      <td>E</td>
    </tr>
    <tr>
      <td>2009</td>
      <td>Philadelphia Phillies</td>
      <td>E</td>
    </tr>
    <tr>
      <td>2010</td>
      <td>San Francisco Giants</td>
      <td>W</td>
    </tr>
    <tr>
      <td>2011</td>
      <td>St. Louis Cardinals</td>
      <td>C</td>
    </tr>
    <tr>
      <td>2012</td>
      <td>San Francisco Giants</td>
      <td>W</td>
    </tr>
    <tr>
      <td>2013</td>
      <td>St. Louis Cardinals</td>
      <td>C</td>
    </tr>
    <tr>
      <td>2014</td>
      <td>San Francisco Giants</td>
      <td>W</td>
    </tr>
    <tr>
      <td>2015</td>
      <td>New York Mets</td>
      <td>E</td>
    </tr>
  </tbody>
</table>

<img src="img/nl-div-winners.png">

<h3>Find the 20 best hitters in all of baseball.</h3>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Divison</th>
      <th>League</th>
      <th>Last Name</th>
      <th>First Name</th>
      <th>Team</th>
      <th>Number of Hits</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>W</td>
      <td>NL</td>
      <td>Phillips</td>
      <td>Brandon</td>
      <td>Cincinnati Reds</td>
      <td>203364</td>
    </tr>
    <tr>
      <td>W</td>
      <td>NL</td>
      <td>Rollins</td>
      <td>Jimmy</td>
      <td>Los Angeles Dodgers</td>
      <td>193194</td>
    </tr>
    <tr>
      <td>W</td>
      <td>AL</td>
      <td>Cano</td>
      <td>Robinson</td>
      <td>Seattle Mariners</td>
      <td>183096</td>
    </tr>
    <tr>
      <td>W</td>
      <td>NL</td>
      <td>Utley</td>
      <td>Chase</td>
      <td>Los Angeles Dodgers</td>
      <td>182596</td>
    </tr>
    <tr>
      <td>E</td>
      <td>AL</td>
      <td>Cabrera</td>
      <td>Miguel</td>
      <td>Detroit Tigers</td>
      <td>178512</td>
    </tr>
    <tr>
      <td>E</td>
      <td>NL</td>
      <td>Howard</td>
      <td>Ryan</td>
      <td>Philadelphia Phillies</td>
      <td>174097</td>
    </tr>
    <tr>
      <td>E</td>
      <td>AL</td>
      <td>Jeter</td>
      <td>Derek</td>
      <td>New York Yankees</td>
      <td>172777</td>
    </tr>
    <tr>
      <td>E</td>
      <td>NL</td>
      <td>Peralta</td>
      <td>Jhonny</td>
      <td>St. Louis Cardinals</td>
      <td>171459</td>
    </tr>
    <tr>
      <td>E</td>
      <td>AL</td>
      <td>Pedroia</td>
      <td>Dustin</td>
      <td>Boston Red Sox</td>
      <td>170430</td>
    </tr>
    <tr>
      <td>E</td>
      <td>AL</td>
      <td>Ortiz</td>
      <td>David</td>
      <td>Boston Red Sox</td>
      <td>163990</td>
    </tr>
    <tr>
      <td>E</td>
      <td>AL</td>
      <td>Martinez</td>
      <td>Victor</td>
      <td>Detroit Tigers</td>
      <td>161805</td>
    </tr>
    <tr>
      <td>E</td>
      <td>NL</td>
      <td>Molina</td>
      <td>Yadier</td>
      <td>St. Louis Cardinals</td>
      <td>160704</td>
    </tr>
    <tr>
      <td>W</td>
      <td>AL</td>
      <td>Victorino</td>
      <td>Shane</td>
      <td>Los Angeles Angels of Anaheim</td>
      <td>157837</td>
    </tr>
    <tr>
      <td>W</td>
      <td>NL</td>
      <td>Votto</td>
      <td>Joey</td>
      <td>Cincinnati Reds</td>
      <td>154476</td>
    </tr>
    <tr>
      <td>E</td>
      <td>NL</td>
      <td>McCutchen</td>
      <td>Andrew</td>
      <td>Pittsburgh Pirates</td>
      <td>148479</td>
    </tr>
    <tr>
      <td>W</td>
      <td>AL</td>
      <td>Ramirez</td>
      <td>Alexei</td>
      <td>Chicago White Sox</td>
      <td>146280</td>
    </tr>
    <tr>
      <td>W</td>
      <td>AL</td>
      <td>Pujols</td>
      <td>Albert</td>
      <td>Los Angeles Angels of Anaheim</td>
      <td>144179</td>
    </tr>
    <tr>
      <td>E</td>
      <td>NL</td>
      <td>Granderson</td>
      <td>Curtis</td>
      <td>New York Mets</td>
      <td>141407</td>
    </tr>
    <tr>
      <td>E</td>
      <td>AL</td>
      <td>Soriano</td>
      <td>Alfonso</td>
      <td>New York Yankees</td>
      <td>141099</td>
    </tr>
    <tr>
      <td>W</td>
      <td>AL</td>
      <td>Konerko</td>
      <td>Paul</td>
      <td>Chicago White Sox</td>
      <td>140875</td>
    </tr>
  </tbody>
</table>

<h3>What team pitched the most shutouts for a given season?</h3>
​
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Team</th>
      <th>Year</th>
      <th>Shutouts</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Detroit Tigers</td>
      <td>2006</td>
      <td>16</td>
    </tr>
    <tr>
      <td>San Diego Padres</td>
      <td>2007</td>
      <td>20</td>
    </tr>
    <tr>
      <td>Boston Red Sox</td>
      <td>2008</td>
      <td>16</td>
    </tr>
    <tr>
      <td>San Francisco Giants</td>
      <td>2009</td>
      <td>18</td>
    </tr>
    <tr>
      <td>Philadelphia Phillies</td>
      <td>2010</td>
      <td>21</td>
    </tr>
    <tr>
      <td>Philadelphia Phillies</td>
      <td>2011</td>
      <td>21</td>
    </tr>
    <tr>
      <td>Los Angeles Angels of Anaheim</td>
      <td>2012</td>
      <td>16</td>
    </tr>
    <tr>
      <td>Los Angeles Dodgers</td>
      <td>2013</td>
      <td>22</td>
    </tr>
    <tr>
      <td>St. Louis Cardinals</td>
      <td>2014</td>
      <td>23</td>
    </tr>
    <tr>
      <td>Chicago Cubs</td>
      <td>2015</td>
      <td>21</td>
    </tr>
  </tbody>
</table>

<img src="img/teams-most-shoutout.png">

Database downloaded from [jknecht baseball archive](https://github.com/jknecht/baseball-archive-sqlite/blob/master/lahman2015.sqlite)