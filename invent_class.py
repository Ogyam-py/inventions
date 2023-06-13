from random import choice

class invent():
    def __init__(self, user_name, level = 100, score = 0):
        self.username = user_name
        self.level = level
        self.score = score
        self.inventB = None
    
    @classmethod
    def game_data(cls):
        """
        Loads inventions data from the file dict_inventions.txt
        """
        with open("dict_inventions.txt", "r") as fh_game:  
            cls.patent_dict = eval(fh_game.read())
    
    def user_data(self, action = None):
            """
            Loads, updates, clears or saves user's data.
            save is temporal.
            """
            if action == "load":
                with open("user_data.txt", "r") as fh_load:
                    self.users_scores = eval(fh_load.read())
    
            elif action == "update":
                with open("user_data.txt", "w+") as fh_save:
                    txt = str(self.users_scores)
                    fh_save.write(txt)

            elif action == "clear":
                with open("user_data.txt", "w") as fh_clear:
                    fh_clear.write("{'defaut': 0}")
            
            else:
                self.users_scores[self.username] = self.users_scores.get(self.username, 0)
                if self.users_scores[self.username] < self.score:
                    self.users_scores[self.username] = self.score

    def collector(self):
        """
        Generates a tuple of invention A and B, respectively.
        Invention A is the previous invention B.
        """
        if self.inventB == None:
            inventA = choice(range(1800, 2022))
        else:
            inventA = inventB
        while True:
            inventB = choice(range(inventA-self.level, inventA+self.level+1))
            if 1800 <= inventB <= 2021:
                self.inventA, self.inventB = inventA, inventB
                break
                

    def validate(self, ans):
        """
        Checks the validity of the answer provided by the user.
        """
        if (ans == "a" and self.inventA < self.inventB) or (ans == "b" and self.inventA > self.inventB):
            if self.level == 100: self.score += 10
            elif self.level == 50: self.score += 15
            elif self.level == 25: self.score += 20
            return True
        elif ans == "c":
            return "clue"
        elif ans not in ("a", "b", "c"):
            return None
        else:
            return False