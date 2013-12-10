class Observable:
    def __init__(self):
        pass

    def register_observer(self, observer):
        raise NotImplementedError

    def remove_observer(self, observer):
        raise NotImplementedError

    def notify_observers(self):
        raise NotImplementedError


class GameData(Observable):
    def __init__(self, home_team, visiting_team):
        Observable.__init__(self)
        self._observers = []
        self._home_team = home_team
        self._visiting_team = visiting_team
        self._home_team_socre = 0
        self._visiting_team_score = 0

    def register_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self, None)

    def update(self, home_team_socre, visiting_team_score):
        self._home_team_socre = home_team_socre
        self._visiting_team_score = visiting_team_score
        self.notify_observers()

    def home_team(self):
        return self._home_team

    def visiting_team(self):
        return self._visiting_team

    def home_team_socre(self):
        return self._home_team_socre

    def visiting_team_score(self):
        return self._visiting_team_score
