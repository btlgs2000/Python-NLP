import random
from tqdm import tqdm

def write(l, f, last_line=False):
    *elems, last = l
    for elem in elems:
        f.write(f'{elem} ')
    f.write(str(last))
    if not last_line:
        f.write('\n')

def create_postive(length, max_num):
    ret = []
    l = sorted([random.randint(1, max_num) for _ in range(length)])
    for elem in l:
        if random.choice([True, False]):
            # in coda
            ret.append(elem)
        else:
            # all'inizio
            ret = [elem] + ret
    return ret

def create_random(length, max_num):
    return [random.randint(1, max_num) for _ in range(length)]

def create_test_file(n, max_length, max_num):
    with open(r'F:\Documenti\Python NLP\esercizi\cubi_impilati\test_file.txt', 'w') as f:
        for i in tqdm(range(n)):
            length = random.randint(1, max_length)
            is_postive = random.choice([True, False])
            if is_postive:
                # lista con un esempio positivo
                l = create_postive(length, max_num)
            else:
                l = create_random(length, max_num)
            
            last_line = False if i < n-1 else True
            write(l, f, last_line)
                
            
if __name__ == "__main__":
    create_test_file(10_000, 1000, 100)