import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def fillDDYear(self):
        for i in self._model.getAllYears():
            self._view._ddAnno.options.append(ft.dropdown.Option(data=i, text=i, on_click=self.readYear))

    def readYear(self, e):
        if e.control.data:
            self._selectedYear = e.control.data
        else:
            self._selectedYear = None
        for i, item in enumerate(self._model.getAllTeams(self._selectedYear), start=1):
            self._view._txtOutSquadre.controls.append(ft.Text(f"{i}. {item}"))
        self._view.update_page()


    def handleCreaGrafo(self, e):
        self._view._txt_result.controls.clear()
        bool, Nnodes, Nedges = self._model.creaGrafo(self._selectedYear)
        self._view._txt_result.controls.append(ft.Text(f"Creazione grafo avvenuta con successo\nNumero nodi: {Nnodes}\nNumero archi: {Nedges}"))
        for i in self._model.getAllNodes():
            self._view._ddSquadra.options.append(ft.dropdown.Option(data=i, text=f"{i} ({i.name})", on_click=self.readSquadra))
        self._view.update_page()

    def handleDettagli(self, e):
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Eseguito lo studio dei dettagli"))
        for i, item in enumerate(self._model.calcolaDettagli(self._insertedTeam), start=1):
            self._view._txt_result.controls.append(ft.Text(f"{i}. {item[0]}: {item[1]}"))
        self._view.update_page()

    def handlePercorso(self, e):
        self._view._txt_result.controls.clear()
        sequenza, costo = self._model.calcolaPercorso(self._insertedTeam)
        self._view._txt_result.controls.append(ft.Text(f"Studio della ricorsione eseguita\nCosto: {costo}"))
        for i, item in enumerate(sequenza, start=1):
            self._view._txt_result.controls.append(ft.Text(f"{i}. {item}"))
        self._view.update_page()

    def readSquadra(self, e):
        if e.control.data:
            self._insertedTeam = e.control.data
        else:
            self._insertedTeam = None

