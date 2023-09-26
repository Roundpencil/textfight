# This is a sample Python script.
import pickle
import random
import re
from dataclasses import dataclass
from typing import List


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Tournoi:
    def __init__(self, txt):
        self.contenders = self._generate_contenders(txt)
        self.appariements = []

    @dataclass
    class Contender:
        description: str
        wins = 0
        loses = 0

    def save(self, filename='me.tour'):
        """Sauvegarde l'état du tournoi dans un fichier pickle."""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @staticmethod
    def load(filename='me.tour'):
        """Charge l'état du tournoi à partir d'un fichier pickle."""
        with open(filename, 'rb') as f:
            return pickle.load(f)


    def _generate_contenders(self, file_name: str) -> List['Tournoi.Contender']:
        to_return = []
        with open(file_name, 'r') as file:
            description_lines = []  # Pour stocker les lignes de la description en cours de construction
            for line in file:
                # Utiliser une regex pour vérifier si la ligne commence par un nombre suivi d'un point
                if re.match(r"^\d+\.", line):
                    if description_lines:  # si description_lines n'est pas vide
                        # Joindre toutes les lignes pour créer la description complète
                        description = "\n".join(description_lines).strip()
                        contender = self.Contender(description)
                        to_return.append(contender)
                    # Commencer une nouvelle description
                    description_lines = [line.split(".")[1].strip()]  # conservez uniquement la partie après le numéro et le point
                else:
                    # Ajouter la ligne à description_lines
                    description_lines.append(line.strip())

            # Pour ajouter le dernier contender
            if description_lines:
                description = " ".join(description_lines)
                contender = self.Contender(description)
                to_return.append(contender)

        return to_return

    def _creer_appariements(self):
        to_return = []
        haut = [contender for contender in self.contenders if contender.loses == 0]
        moyen = [contender for contender in self.contenders if contender.loses == 1]
        bas = [contender for contender in self.contenders if contender.loses == 2]

        if len(moyen)==1 and len(bas)==1:
            return [[bas[0], moyen[0]]]

        if len(moyen)==1 and len(haut)==1:
            return [[haut[0], moyen[0]]]

        if len(haut)==1 and len(bas)==1:
            return [[bas[0], haut[0]]]


        for tableau in [haut, moyen, bas]:
            random.shuffle(tableau)
            if len(tableau) % 2 == 1:
                tableau.append(None)
            while len(tableau):
                to_return.append([tableau.pop(), tableau.pop()])

        print(f"\n\nappariements pour la ronde {self._ronde_en_cours(to_return)} : {to_return}")

        return to_return


    def _ronde_en_cours(self, table_appariements):
        if len(table_appariements):
            if table_appariements[0][0]:
                return table_appariements[0][0].wins + table_appariements[0][0].loses
            else:
                return table_appariements[0][1].wins + table_appariements[0][1].loses

        return -1

    # Press the green button in the gutter to run the script.
    def _demander_vote_a_utilisateur(self, contender_1: Contender, contender_2: Contender):

        """
        Demande à l'utilisateur de voter entre deux contenders ou de quitter.

        Affiche les descriptions des deux contenders passés en paramètres et demande
        à l'utilisateur de faire un choix parmi eux, ou de quitter. Si l'utilisateur
        choisit un des contenders, les attributs wins et loses sont mis à jour en conséquence.

        Parameters:
            contender_1 (Contender): Le premier contender parmi lesquels l'utilisateur doit choisir.
            contender_2 (Contender): Le deuxième contender parmi lesquels l'utilisateur doit choisir.

        Returns:
            bool: Retourne True si un vote a été effectué, False si l'utilisateur choisit de quitter.
        """
        if contender_1 is None:
            contender_2.wins+=1
            return True

        if contender_2 is None:
            contender_1.wins+=1
            return True

        print("\n\n")
        print(f"1. {contender_1.description}\n\n")
        print(f"2. {contender_2.description}")
        print("3. Quitter et sauvegarder")

        choix = input("Faites votre choix (1/2/3): ")

        while choix not in ['1', '2', '3']:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
            choix = input("Faites votre choix (1/2/3): ")

        if choix == '1':
            contender_1.wins += 1
            contender_2.loses += 1
            return True
        elif choix == '2':
            contender_2.wins += 1
            contender_1.loses += 1
            return True
        elif choix == '3':
            return False

    def start(self):
        for contender in self.contenders:
            print(contender)

        appariements = self._creer_appariements()
        ronde = self._ronde_en_cours(appariements)
        print(f"rond : {ronde} : appariements en cours : {appariements}")
        print()
        while len(appariements) > 1 or (appariements[0][0] is not None and appariements[0][1] is not None):
            while len(appariements):
                contender_1, contender_2 = appariements.pop()
                yeah = self._demander_vote_a_utilisateur(contender_1, contender_2)
                if not yeah:
                    self.save()
                    exit()
            appariements = self._creer_appariements()
            random.shuffle(appariements)

        sorted_contenders = sorted(self.contenders, key=lambda x: x.wins, reverse=True)

        print("\n\n\n affichage des résulats")
        # Afficher les contenders triés
        for index, contender in enumerate(sorted_contenders, 1):
            print(f"{index}. {contender.description}: {contender.wins} wins / {contender.loses} loses ")

if __name__ == '__main__':
    # lancement du programme : demander si fichier de sauvegarde ou nouveau projet (saisie)

    # Test with an example file name.
    tournoi = Tournoi("source.txt")
    tournoi.start()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
