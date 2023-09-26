# This is a sample Python script.
from dataclasses import dataclass


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

@dataclass
class Contender:
    description: str
    wins = 0
    loses = 0


def generate_contenders(file_name: str) -> list[Contender]:
    contenders = []
    with open(file_name, 'r') as file:
        for line in file:
            if line.strip():  # skip empty lines
                if line.strip()[0].isdigit():  # check if line starts with a digit
                    description = line.split(".")[1].strip()
                    contender = Contender(description)
                    contenders.append(contender)
    return contenders

def creer_appairements(contenders: list[Contender]):
    to_return = []
    haut = [contender for contender in contenders if contender.loses == 0]
    moyen = [contender for contender in contenders if contender.loses == 1]
    bas = [contender for contender in contenders if contender.loses == 2]

    for tableau in [haut, moyen, bas]:
        if len(tableau) % 2 == 1:
            tableau.append(None)
        while len(tableau):
            to_return.append([tableau.pop(), tableau.pop()])



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Test with an example file name.
    contenders = generate_contenders("source.txt")
    for contender in contenders:
        print(contender)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
