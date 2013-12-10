from observable import GameData
from observer import GameBoard

gameboard = GameBoard()
gamedata = GameData('New York', 'Indiana Pacers')
gamedata.register_observer(gameboard)
gamedata.update(0, 0)
gamedata.update(10, 15)
gamedata.update(30, 28)
