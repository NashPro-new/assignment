import pandas as pd
from selenium import webdriver
import maxL

driver = webdriver.Chrome(executable_path = "D:\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(30)
url = "https://en.wikipedia.org/wiki/2022_Indian_Premier_League#Points_Table"
driver.get(url)

html = driver.page_source
tables = pd.read_html(html)
df = tables[4]
df2 = tables[5]

df.rename(columns = {'Team.mw-parser-output .navbar{display:inline;font-size:88%;font-weight:normal}.mw-parser-output .navbar-collapse{float:left;text-align:left}.mw-parser-output .navbar-boxtext{word-spacing:0}.mw-parser-output .navbar ul{display:inline-block;white-space:nowrap;line-height:inherit}.mw-parser-output .navbar-brackets::before{margin-right:-0.125em;content:"[ "}.mw-parser-output .navbar-brackets::after{margin-left:-0.125em;content:" ]"}.mw-parser-output .navbar li{word-spacing:-0.125em}.mw-parser-output .navbar a>span,.mw-parser-output .navbar a>abbr{text-decoration:inherit}.mw-parser-output .navbar-mini abbr{font-variant:small-caps;border-bottom:none;text-decoration:none;cursor:inherit}.mw-parser-output .navbar-ct-full{font-size:114%;margin:0 7em}.mw-parser-output .navbar-ct-mini{font-size:114%;margin:0 4em}vte':'Team', 'Pld':'Played'}, inplace = True)
df2.rename(columns = {'Team':'Team'})
df = df.reset_index()


mydict = {}
teamname = []
team2= []
pts= {}

for index,row in df.iterrows():
    pts[row['Team']]= row['Pts']

for index,row in df.iterrows():
    teamname.append(row['Team'])


del1 = ['(C)','(R)','(4th)','(3rd)']
for i1 in del1:
    for team in teamname[0:4]:
        if i1 in team:
            team1 = team.split()
            team1.remove(i1)
            team = ' '.join(team1)
            team2.append(team)

for team in teamname[4:14]:
    team2.append(team)



df2 = df2.reset_index()

summary1 = df2.values.tolist()
list1 = []

for summary in summary1:
    if summary[2] == 0:
        list1.append('l')
    else:
        list1.append('w')
    for i in range(2,15):
        if int(summary[i+1]) - int(summary[i]) == 2:
            list1.append('w')
        else:
            list1.append('l')





########## Mydict contains team names as keys and all match results as their values#######

myteams = []
mydict = {}
k=[]
x = 0
y =14
for index,row in df2.iterrows():
    myteams.append(row['Team'])
for team in myteams:
    mydict[str(team)] = []
    for k in list1[x:y]:
        mydict[str(team)].append(k)
    x=y
    y+=14
##### Dictionary named table containing team names as keys and points and last 5 matches result as it's values########
##### Report dictionary contains all match wins and total points with corrected team names #########

table = {}
report = {}
for team in team2:
    for i in mydict.keys():
        if team in i:
            for z in pts.keys():
                if team in z:
                    table[team] = []
                    table[team].append(pts[z])
                    table[team].append(mydict[i][9:14])
                    report[team] = []
                    report[team].append(pts[z])
                    report[team].append(mydict[i])


losses={}
tm = []
total_pts = 0
n = int(input('Enter consecutive losses or wins number:'))
rep = str(input('Enter win or loss (w or l):'))
for team_name, team_data in report.items():
    #print(team_data[1])
    losses[team_name] = maxL.max_losses_wins(team_data[1], rep)
for t_name,t_rep in losses.items():
    if t_rep >= n:
        tm.append(t_name)
        total_pts += table[t_name][0]
if len(tm) != 0:
    avg_pts = total_pts/int(len(tm))
    print('teams that won/lost: ', tm)
    print(' with avg points: ', avg_pts)
else:
    print('no team won/lost these many matches consecutively')
tm.clear()












    #     if ( str(value[1][l]) == 'l' and str(value[1][l+1]) == 'l'):
    #         #print(value[0])
    #         print(rep_keys[pos1])
    #         break
    # pos1 += 1

