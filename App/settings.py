class Settings :
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BACKGROUND = (194, 161, 236)
    FOOD_COLOR = (154, 93, 202)
    TRAP_COLOR = (109, 120, 200)
    PLAYER_COLOR = (231, 65, 36)
    
    def __init__(self) :
        self.allmodes = {"mouse": 1, "keyboard": 2}
        self.alllevels = {"easy": 2, "medium": 3, "hard": 4}
        
    def get_key_from_value(self, dictionary, value):
        for key, val in dictionary.items():
            if val == value:
                return key
        return None