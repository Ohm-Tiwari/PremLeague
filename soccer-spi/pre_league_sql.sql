SELECT * FROM premleague.prem_league_dataset;

select distinct season from premleague.prem_league_dataset order by season;

select distinct season, team1 from premleague.prem_league_dataset 
where season = 2022
order by team1;

select distinct season, team2 from premleague.prem_league_dataset 
where season = 2022
order by team2;

select distinct season, team1, team2, score1, score2 from premleague.prem_league_dataset 
where season = 2021
and ((team1 = 'Chelsea') or (team2 = 'Chelsea'))
and ((team2 = 'Everton') or (team2 = 'Everton')) 
;





