def is_right(l):
    top_elem = float('inf')
    while len(l) > 0:
        first, last = l[0], l[-1]
        if max(first, last) > top_elem:
            return False
        if first > last:
            l = l[1:]
            top_elem = first
        else:
            l = l[:-1]
            top_elem = last
    return True

def line_to_list(line):
    return [int(elem) for elem in line.split(' ')]

def print_res(scr, target):
    with open(scr, 'r') as src_file:
        with open(target, 'w') as tgt_file:
            for line in src_file:
                if len(line.strip()) > 0:
                    l = line_to_list(line)
                    tgt_file.write(f'{is_right(l)}\n')
                else:
                    break
                
scr = r'F:\Documenti\Python NLP\esercizi\cubi_impilati\src.txt'
tgt = r'F:\Documenti\Python NLP\esercizi\cubi_impilati\tgt.txt'
print_res(scr, tgt)