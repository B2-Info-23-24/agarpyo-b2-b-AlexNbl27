class Settings :
    def __init__(self) :
        self.allmodes = {"mouse": 1, "keyboard": 2}
        self.alllevels = {"easy": 2, "medium": 3, "hard": 4}
        
    def get_key_from_value(self, dictionary, value):
        for key, val in dictionary.items():
            if val == value:
                return key
        return None