# ### Problem 5
# Example Output:
# ```
# The Grizzlies are from Memphis and are 2 in the standings.
# # Update the rating from 2 to 8 from your code
# The Grizzlies are from Memphis and are 8 in the standings.
# ```

# Create a SportsTeam Class for tracking sports teams.
# The class should have the properties team_name_p, team_city, and team_ranking_p.
class SportsTeam:
    def __init__(self, team_name_p, team_city, team_ranking_p):
        self.team_name_p = team_name_p
        self.team_city = team_city
        self.team_ranking_p = team_ranking_p

    # The class should have a method to change a Team’s ranking.
    def changeRank(self, newRank):
        self.team_ranking_p = newRank

    # The class should implement the ```__str__``` method so that when an instance
    # of the SportsTeam is printed it will output a string containing the team name, team city,
    # and team rank (use f strings to format the output).
    def __str__(self):
        return f'The {self.team_name_p} are from {self.team_city} and are {self.team_ranking_p} in the standings'

# Your program should create a SportsTeam instance with an initial ranking of 2.
team1 = SportsTeam('Tigers', 'Memphis', 22)

# Print out the class
print(team1)


# Your program should change the ranking of the team to 8 using only the class method.
# Print out the class (should use your ```__str__``` method).
# print(team1)




# TODO: figure out how to call function from outside of class
