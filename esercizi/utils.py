from pathlib import Path

src = 'src.txt'
tgt = 'tgt.txt'
res = 'res.txt'

def read_lines(filename, remove_blanks=True, stripline=True):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines if len(line.strip()) > 0]
    
def test(folder):
    folder= Path(folder)
    src_lines = read_lines(folder / src)
    tgt_lines = read_lines(folder / tgt)
    res_lines = read_lines(folder / res)
    for i, (src_line, tgt_line, res_line) in enumerate(zip(src_lines, tgt_lines, res_lines)):
        if tgt_line != res_line:
            print(f'input={src_line}\n\natteso={tgt_line}\n\ntrovato={res_line}')
            break
    else:
        print('test superato!')