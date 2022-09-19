class Group:
    def __init__(self,team):
        self.team=team

    def __str__(self):
        return str(self.team)

    def __add__(self,group):
        self.team.extend(group.team)
        return self.team

team1=Group(['Raj','Naveen','Jack'])
team2=Group(['Joseph','Rohan','Manish'])

print(team1)
print(team2)
team3=team1+team2
print(team3)