import networkx as nx
from database.DAO import DAO
from itertools import combinations
import copy

class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def getAllYears(self):
        return DAO.getAllYears()

    def getAllTeams(self, y):
        return DAO.getAllTeams(y)

    def creaGrafo(self, y):
        self._grafo.clear()
        self._idMap.clear()
        self._grafo.add_nodes_from(self.getAllTeams(y))
        for i, j in combinations(self._grafo.nodes(), 2):
            weight = self.calcolaWeight(i, j, y)
            self._grafo.add_edge(i, j, weight=weight)
        return True, self._grafo.number_of_nodes(), self._grafo.number_of_edges()

    def calcolaWeight(self, i, j, y):
        if DAO.getSalari(i.teamCode, y) is not None:
            peso1 = int(DAO.getSalari(i.teamCode, y))
        else:
            peso1 = 0
        if DAO.getSalari(j.teamCode, y) is not None:
            peso2 = int(DAO.getSalari(j.teamCode, y))
        else:
            peso2 = 0
        weight = peso1+peso2
        return weight

    def getAllNodes(self):
        return self._grafo.nodes()

    def calcolaDettagli(self, n):
        vicini = self._grafo.neighbors(n)
        lista = []
        for i in vicini:
            lista.append((i, self._grafo[n][i]['weight']))
        return sorted(lista, key=lambda x: x[1], reverse=True)

    def calcolaPercorso(self, n):
        self._sequenzaOttima = []
        self._costoMax = -1
        lista = sorted(self._grafo.neighbors(n), key=lambda x: self._grafo[n][x]['weight'], reverse=True)
        self.ricorsione([n], list(lista))
        return self._sequenzaOttima, self._costoMax

    def ricorsione(self, parziale, sequenza):
        costo = self.costo(parziale)
        if costo > self._costoMax:
            self._costoMax = costo
            self._sequenzaOttima = copy.deepcopy(parziale)
            print(f"aggiornamento ({len(self._sequenzaOttima)}): {self._costoMax} - {self._sequenzaOttima}")
        for i in sequenza:
            if self.vincoli(parziale, i):
                parziale.append(i)
                lista = sorted(self._grafo.neighbors(parziale[-1]), key=lambda x: self._grafo[parziale[-1]][x]['weight'], reverse=True)
                self.ricorsione(parziale, list(lista))
                parziale.pop()

    def vincoli(self, parziale, i):
        if i in parziale:
            return False
        if len(parziale) >= 2:
            if self._grafo[parziale[-2]][parziale[-1]]['weight'] < self._grafo[parziale[-1]][i]['weight']:
                return False
        return True

    def costo(self, parziale):
        costoMax = 0
        for i in range(0, len(parziale)-1):
            costoMax += self._grafo[parziale[i]][parziale[i+1]]['weight']
        return costoMax










