import csv

from django.db import models

class Match(models.Model):
    match_id = models.IntegerField()
    innings_id = models.IntegerField()
    over_id = models.IntegerField()
    ball_id = models.IntegerField()
    team_batting_id = models.IntegerField()
    team_bowling_id = models.IntegerField()
    striker_id = models.IntegerField()
    striker_batting_position = models.IntegerField()
    non_striker_id = models.IntegerField()
    bowler_id = models.IntegerField()
    batsman_scored = models.IntegerField()
    extra_type = models.CharField(max_length=30)
    extra_runs = models.IntegerField()
    player_dissimal_id = models.IntegerField()
    dissimal_type = models.CharField(max_length=30)
    fielder_id = models.IntegerField()

    class Meta:
        unique_together = ('match_id', 'innings_id', 'over_id', 'ball_id')

    @classmethod
    def load_from_csv( league.csv):
        with open('league.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
            for row in csvreader:
                match = cls(
                match_id=int(row[0]),
                innings_id=int(row[1]),
                over_id=int(row[2]),
                ball_id=int(row[3]),
                team_batting_id=int(row[4]),
                team_bowling_id=int(row[5]),
                striker_id=int(row[6]),
                striker_batting_position=int(row[7]),
                non_striker_id=int(row[8]),
                bowler_id=int(row[9]),
                batsman_scored=int(row[10]),
                extra_type=row[11],
                extra_runs=int(row[12]),
                player_dissimal_id=int(row[13])
                )
                yield match

#  example:
matches = Match.load_from_csv('league.csv')
Match.objects.bulk_create(matches)
                
data = [
    ['Match_Id', 'Innings_Id', 'Over_Id', 'Ball_Id', 'Team_Batting_Id','Team_Bowling_Id', 'Striker_Id', 'Striker_Batting_Position', 'Non_Striker_Id', 'Bowler_Id', 'Batsman_Scored', 'Extra_Type',' Extra_Runs', 'Player_dissimal_Id', 'Dissimal_Type', 'Fielder_Id'],
    [335987,4,5,4,1,2,2,2,3,17,0,'legbyes',1, , , ,],
    [335934,1,2,3,4,2,2,2,3,19,0, ,1,2, , , ,],
    [336788,1,2,4,6,4,3,6,7,23,0,'league',1,  , , ,]
]

filename = 'league.csv'

with open(filename, 'w' , newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    cvswriter.writerows(data)

print(f"Data has been added to {filename}")

#djando read and write