# This is a sample Python script.
from dataclasses import dataclass


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class tournoi:
    def __init__(self, txt):
        self.contenders = self._generate_contenders(txt)

    @dataclass
    class Contender:
        description: str
        wins = 0
        loses = 0



    def _generate_contenders(self, file_name: str) -> list[Contender]:
        to_return = []
        with open(file_name, 'r') as file:
            for line in file:
                if line.strip() and line.strip()[0].isdigit():
                    description = line.split(".")[1].strip()
                    contender = self.Contender(description)
                    to_return.append(contender)
        return to_return

    def creer_appaieiments(self, contenders: list[Contender]):
        to_return = []
        haut = [contender for contender in contenders if contender.loses == 0]
        moyen = [contender for contender in contenders if contender.loses == 1]
        bas = [contender for contender in contenders if contender.loses == 2]

        for tableau in [haut, moyen, bas]:
            if len(tableau) % 2 == 1:
                tableau.append(None)
            while len(tableau):
                to_return.append([tableau.pop(), tableau.pop()])

        return to_return

    def ronde_en_cours(self, table_appariements):
        if len(table_appariements):
            return table_appariements[0][0].wins + table_appariements[0][0].loses

        return -1

    # Press the green button in the gutter to run the script.
    def demander_vote_a_utilisateur(self, contender_1, contender_2):
        pass


if __name__ == '__main__':
    #lancement du programme : demander si fichier de sauvegarde ou nouveau projet (saisie)

    # Test with an example file name.
    contenders = tournoi("source.txt")
    for contender in contenders:
        print(contender)

    appariements = creer_appaieiments(contenders)

    while len(appariements):
        contender_1, contender_2 = appariements.pop()
        demander_vote_a_utilisateur(contender_1, contender_2)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
