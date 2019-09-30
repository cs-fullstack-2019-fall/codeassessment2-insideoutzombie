# ### Problem 6
# Example Output:
# ```
# There are currently 4 club members in the list!

# Club President: Alfred
# Club Vice President: Troy
# Club Secretary: Albert
# Club Treasurer: Bob
# ```

# Create a class called ClubMember
# Each club member has a name and a role
class ClubMember:
    def __init__(self, name, role):
        self.name = name
        self.role = role

# Create ClubMember instances for the following people:
member1 = ClubMember("Alfred", "Club President")
member2 = ClubMember("Troy", "Club Vice President")
member3 = ClubMember("Albert", "Club Secretary")
member4 = ClubMember("Bob", "Club Treasurer")

# Add each member instance to a new club_members list that you create.
club_members = []

# Write the code needed to loop through the club member list and print
# the current number of members in the list, then the member’s name and
# club role, one per line using f strings.
for x in member1:
    x.append(club_members)

    print(x.name)










# TODO: research TypeError: 'ClubMember' object is not iterable
