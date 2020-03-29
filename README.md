Change your root accordingly while using the data_preparation notebook

In The Mongo_Data Folder,we have a List of .json Files which are the Data that we have scraped for
out project

These Include Things like the match odds,League Tables,Manager Stats for Per Team Per Season and 
a list of all matches that the team has played throughout the season in different competitions

In the Following Section,we briefly Explain the different JSON files in detail in the type of data
that they contain.


Description of the Data

Competition_Table.json

In this table,we get the data for per club per season per competition for the years 2014-2019

It contains the List of Following columns

competition_name:This contains the competition name in which the corresponding match took place(EFL,FA Cup,Permier League etc)

club_name:Name of the Club(Primary Club for which this record is scraped)

Season:Year of the Season
club_id:Id of the club(Acc to the transfermarket website)

match_type:The type of the match(Semi Final,Quarter Final,Third Round etc)

match_date:The date on which the match took place

match_time:The time at which the match took place(9 AM,12 PM,5 PM etc)

home_team:The team in whose home ground this match took place

away_team:The Visiting team for which this match is an away match.

play_style:Formation employed in this match

coach:Name of the coach

result:Home:Away Result

home_score:Home Team Score

away_score:Away Score

match_result_link:Link in which more detailed data for the match is given

collection_name:Internal Key to be used

LeagueTable.JSON

In this table,we store the team standing in a given season for the Premier League Competition.

league_standing:Position in the league after the end of the season.

team_name:Name of the Team

team_link:Internal Link to be used to get more detailed data for the matches played by this team in this season.

total_matches:The no of matches played by this team

wins:No of Wins

loss:No of Losses

draw:no of Draws

goals_scored:Goals scored by the team

goals_conceded:no of goals conceded.

plus_minus:Goal Difference

Points:Points at the end of the league

club_id:Internal Key to get more data about this particualr team

season:The season in which this data was taken.

collection_name:Internal key


Manager_Table

In this table we store the data for the manager for a given club in a given season.

matches_played:No of matches managed by this manager.

manager_name:Name of the Manager

matches_won:No of matches won by this manager

club_nanem:Name of the club for this particular manager.

matches_draw:No of matches drawn

matches_lost:No of matches lost

goals_for:Goals in Favour of the Manger

goals_against:Goals against this manager

goal_difference:Difference between for and against

win_percentage:Success rate for the manager.

total_points:Total points won by this manager

points_match:Points Per Match

collection_name:Internal Key


Comment_data

In this table,we gather the comments for premier league matches fromm different subs

sub_id:Id of the comment from which the data is gathered.

title:Title of the post

address:Link of the Post

author:Name of the author

score:Score for the post

created:Date of creation of the post.

num_comments:No of comments made on this post

permalink:linf of the post

flair:Flair attached to this post.

Odds_data

In this table,we gather the odds for per match per season per team.

Div = League Division

Date = Match Date (dd/mm/yy)

Time = Time of match kick off

HomeTeam = Home Team

AwayTeam = Away Team

FTHG and HG = Full Time Home Team Goals

FTAG and AG = Full Time Away Team Goals

FTR and Res = Full Time Result (H=Home Win, D=Draw, A=Away Win)

HTHG = Half Time Home Team Goals

HTAG = Half Time Away Team Goals

HTR = Half Time Result (H=Home Win, D=Draw, A=Away Win)

Referee = Match Referee

HS = Home Team Shots

AS = Away Team Shots

HST = Home Team Shots on Target

AST = Away Team Shots on Target

HF = Home Team Fouls Committed

AF = Away Team Fouls Committed

HC = Home Team Corners

AC = Away Team Corners

HY = Home Team Yellow Cards

AY = Away Team Yellow Cards

HR = Home Team Red Cards

AR = Away Team Red Cards

B365H = Bet365 home win odds

B365D = Bet365 draw odds

B365A = Bet365 away win odds

BWH = Bet&Win home win odds

BWD = Bet&Win draw odds

BWA = Bet&Win away win odds

IWH = Interwetten home win odds

IWD = Interwetten draw odds

PSH and PH = Pinnacle home win odds

PSD and PD = Pinnacle draw odds

PSA and PA = Pinnacle away win odds

WHH = William Hill home win odds

WHD = William Hill draw odds

WHA = William Hill away win odds

VCH = VC Bet home win odds

VCD = VC Bet draw odds

VCA = VC Bet away win odds

MaxH = Market maximum home win odds

MaxD = Market maximum draw win odds

MaxA = Market maximum away win odds

AvgH = Market average home win odds

AvgD = Market average draw win odds

AvgA = Market average away win odds

B365>2.5 = Bet365 over 2.5 goals

B365<2.5 = Bet365 under 2.5 goals

P>2.5 = Pinnacle over 2.5 goals

P<2.5 = Pinnacle under 2.5 goals

Max>2.5 = Market maximum over 2.5 goals

Max<2.5 = Market maximum under 2.5 goals

Avg>2.5 = Market average over 2.5 goals

Avg<2.5 = Market average under 2.5 goals

AHh = Market size of handicap (home team) (since 2019/2020)

B365AHH = Bet365 Asian handicap home team odds

B365AHA = Bet365 Asian handicap away team odds

PAHH = Pinnacle Asian handicap home team odds

PAHA = Pinnacle Asian handicap away team odds

MaxAHH = Market maximum Asian handicap home team odds

MaxAHA = Market maximum Asian handicap away team odds	

AvgAHH = Market average Asian handicap home team odds

AvgAHA = Market average Asian handicap away team odds

IWA = Interwetten away win odds