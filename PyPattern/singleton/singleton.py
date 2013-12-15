def singleton(cls, *args, **kwargs):
    instance = {}
    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return _singleton
