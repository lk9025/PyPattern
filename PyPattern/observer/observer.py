class Observer:
    def __init__(self):
        pass

    def update(self, observable, data):
        raise NotImplementedError


class GameBoard(Observer):
    def __init__(self):
        Observer.__init__(self)

    def update(self, observable, data):
        print observable.home_team(), observable.home_team_socre()
        print observable.visiting_team(), observable.visiting_team_score()
