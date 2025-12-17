from networkx.linalg.graphmatrix import adjacency_matrix

with open('advent11.txt', 'r') as file:
    advent = file.read().split('\n')

practice = True
if practice:
    advent = ['aaa: you hhh',
              'you: bbb ccc',
              'bbb: ddd eee',
              'ccc: ddd eee fff',
              'ddd: ggg',
              'eee: out',
              'fff: out',
              'ggg: out',
              'hhh: ccc fff iii',
              'iii: out']



def part_one():
    print('Part one:')

    davent = {lin[:3] : lin[5:].split(' ') for lin in advent}
    davent['out'] = []
    print(davent)

    amat = [[0 for x in range(len(davent))] for y in range(len(davent))]
    for row in range(len(davent)):
        for col in range(len(davent)):
            devicein = list(davent.keys())[row]
            deviceout = list(davent.keys())[col]
            if deviceout in davent[devicein]:
                amat[row][col] = 1

    for row in range(len(davent)):
        for col in range(len(davent)):
            amat[row][col] = min(amat[row][col] + amat[col][row], 1)

    for lin in amat:
        print(lin)














def part_two():
    print('Part two:')


part_one()
#part_two()


