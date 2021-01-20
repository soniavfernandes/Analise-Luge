# Analise-Luge


<h3>INFORMAÇÃO GERAL</h3>
<br>Nome do dataset: Modalidade Luge (Men's singles) Jogos Olimpicos de Inverno;
<br>Identificação do evento:17;
<br>Número do grupo:11;
<br>Alunos:53417;55786;
<br>
<h3>RECOLHA DOS DADOS</h3>
<br>[ANO];LINK
<br>[2002];https://en.wikipedia.org/wiki/Luge_at_the_2002_Winter_Olympics_%E2%80%93_Men%27s_singles;
<br>[2006];https://en.wikipedia.org/wiki/Luge_at_the_2006_Winter_Olympics_%E2%80%93_Men%27s_singles;
<br>[2010];https://en.wikipedia.org/wiki/Luge_at_the_2010_Winter_Olympics_%E2%80%93_Men%27s_singles;
<br>[2014];https://en.wikipedia.org/wiki/Luge_at_the_2014_Winter_Olympics_%E2%80%93_Men%27s_singles;
<br>[2018];https://en.wikipedia.org/wiki/Luge_at_the_2018_Winter_Olympics_%E2%80%93_Men%27s_singles;
<br>[Relatórios oficiais][https://www.fil-luge.org/de/aktuell?event_season_id=19]
<br>
<h3>ESTRUTURA</h3>
<br>Número de ficheiros:2;
<br>Nome dos ficheiros:sport_events.csv;athletes.csv;
<br>
<h4>DESCRIÇÃO</h4>
<br>>>>athletes.csv
<br>
<br>Format: athlete_id,athlete_name,date_of_birth,country_sport_id
<br>
<br>Eg. 72,Felix Loch,24/07/1989,Germany
<br>
<br>Columns:              	Type:		Range:
<br>athlete_id            	Integer 	#where athlete_id is an athlete's identifier unique number
<br>athlete_name          	String		#where athlete_name is the athlete's name
<br>date_of_birth         	String		#where date_of_birth is the athlete's date of birth
<br>country_sport_id      	String		#where country_sport_id is the name of the team's country
<br>
<br>date_of_birth format is DD/MM/YYYY
<br>
<br>>>>sport_events.csv
<br>
<br>Format: year,athlete_id,round_id,finish_time_seconds,rank_id
<br>
<br>Eg. 2010,72,round 1,48.168,1
<br>
<br>Columns:              	Type:           Range:
<br>year                  	Integer         #where 'year' is the sport event's year (2002-2018)	
<br>athlete_id            	Integer	      	#where 'athlete_id'  is the athlete’s id (in the athletes.csv file)
<br>round_id              	String          #where 'round_id' is the round's number. There is four rounds (round 1, round 2, round 3, round 4)
<br>finish_time_seconds	Float		#where 'finish_time_seconds' is the total time spent per athlete on four rounds
<br>rank_id               	Integer         #where 'rank_id' is the number of athlete's rank in that year 
<br>
<br>
<br>Note:Missing values are represented by -1 values.

