from dataclasses import dataclass

@dataclass
class Team:
    ID: int
    year: int
    teamCode: str
    divID: str
    div_ID: int
    teamRank: int
    games: int
    gamesHome: int
    wins: int
    losses: int
    divisionWinnner: str
    leagueWinner: str
    worldSeriesWinnner: str
    runs: int
    hits: int
    homeruns: int
    stolenBases: int
    hitsAllowed: int
    homerunsAllowed: int
    name: str
    park: str

    def __str__(self):
        return self.teamCode

    def __eq__(self, other):
        if isinstance(other, Team):
            return self.teamCode == other.teamCode

    def __hash__(self):
        return hash(self.teamCode)