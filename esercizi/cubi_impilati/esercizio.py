from esercizi.cubi_impilati.create_data import create_postive
from esercizi.utils import test

def is_valid(l):
    pass

def create_results_file():
    pass

folder = r'F:\Documenti\Python NLP\esercizi\cubi_impilati'


from pathlib import Path
import random
with open(Path(folder) / 'tgt.txt', 'r') as tgt:
    with open(Path(folder) / 'res.txt', 'w') as res:
        for line in tgt:
            if random.random() < 1e-9:
                line = line + str(3)
            res.write(line + '\n')

if __name__ == '__main__':
    create_results_file()
    test(folder)