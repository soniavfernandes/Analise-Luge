# Analise-Luge
Python language
INFORMAÇÃO GERAL
Nome do dataset: Modalidade Luge (Men's singles) Jogos Olimpicos de Inverno;
Identificação do evento:17;
Número do grupo:11;
Alunos:53417;55786;

RECOLHA DOS DADOS
[ANO];LINK
[2002];https://en.wikipedia.org/wiki/Luge_at_the_2002_Winter_Olympics_%E2%80%93_Men%27s_singles;
[2006];https://en.wikipedia.org/wiki/Luge_at_the_2006_Winter_Olympics_%E2%80%93_Men%27s_singles;
[2010];https://en.wikipedia.org/wiki/Luge_at_the_2010_Winter_Olympics_%E2%80%93_Men%27s_singles;
[2014];https://en.wikipedia.org/wiki/Luge_at_the_2014_Winter_Olympics_%E2%80%93_Men%27s_singles;
[2018];https://en.wikipedia.org/wiki/Luge_at_the_2018_Winter_Olympics_%E2%80%93_Men%27s_singles;
[Relatórios oficiais][https://www.fil-luge.org/de/aktuell?event_season_id=19]

ESTRUTURA
Número de ficheiros:2;
Nome dos ficheiros:sport_events.csv;athletes.csv;

DESCRIÇÃO

>>>athletes.csv

Format: athlete_id,athlete_name,date_of_birth,country_sport_id

Eg. 72,Felix Loch,24/07/1989,Germany

Columns:              	Type:		Range:
athlete_id            	Integer 	#where athlete_id is an athlete's identifier unique number
athlete_name          	String		#where athlete_name is the athlete's name
date_of_birth         	String		#where date_of_birth is the athlete's date of birth
country_sport_id      	String		#where country_sport_id is the name of the team's country

date_of_birth format is DD/MM/YYYY

>>>sport_events.csv

Format: year,athlete_id,round_id,finish_time_seconds,rank_id

Eg. 2010,72,round 1,48.168,1

Columns:              	Type:           Range:
year                  	Integer         #where 'year' is the sport event's year (2002-2018)	
athlete_id            	Integer	      	#where 'athlete_id'  is the athlete’s id (in the athletes.csv file)
round_id              	String          #where 'round_id' is the round's number. There is four rounds (round 1, round 2, round 3, round 4)
finish_time_seconds	Float		#where 'finish_time_seconds' is the total time spent per athlete on four rounds
rank_id               	Integer         #where 'rank_id' is the number of athlete's rank in that year 


Note:Missing values are represented by -1 values.

