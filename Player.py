from collections import OrderedDict

class Player:

    def __init__(self, name):
       self.name = name
       self.results = {}

    def __eq__(self, other) -> bool:
        if isinstance(self, other.__class__):
            return self.name == other.name and self.results == other.results
        else:
            return NotImplemented

    def __hash__(self) -> int:
        return hash(self.name + self.results)

    def __str__(self) -> str:
        return str(self.results)

    def __repr__(self) -> str:
        return self.results

    def getresults(self):
        return self.results

    def getsortedresult(self):
        return sorted(self.results.items(), key = lambda kv:(kv[0], kv[1]))

    def getbestresult(self):
        return self.getsortedresult()[0]

    def addresult(self, timeresult, round):
        self.results[timeresult] = round

    def getname(self):
        return self.name

    def __iter__(self):
        return self.results

    def next(self):
        for result in self.results:
            yield result
        else:
            StopIteration


player = Player("Karol")
player.addresult(1.189, 3)
player.addresult(2.189, 1)
player.addresult(3.289, 2)

print(player.getname())
print(player.getsortedresult())
print(player.getsortedresult()[0])
