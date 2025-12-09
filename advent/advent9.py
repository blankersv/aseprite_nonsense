
with open('advent9.txt', 'r') as file:
    advent = file.read().split('\n')

practice = True
if practice:
    advent = ['7,1',
              '11,1',
              '11,7',
              '9,7',
              '9,5',
              '2,5',
              '2,3',
              '7,3']

def parse_tuple(strang):
    return [int(x) for x in strang.split(',')]

advent = [parse_tuple(x) for x in advent]


def part_one():
    print('Part one:')

    largest_area = 0
    for corner1 in advent:
        for corner2 in advent:
            largest_area = max(largest_area, (abs(corner1[0] - corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1))

    print(largest_area)


def part_two():
    print('Part two:')

    largest_area = 0
    for cc1 in range(len(advent)-1):
        corner1 = advent[cc1]
        for cc2 in range(cc1+1, len(advent)):
            corner2 = advent[cc2]
            fail = False
            # only need to check along the edges of the rectangle
            while not fail:
                if corner1[0] == corner2[0] or corner1[1] == corner2[1]:
                    pass # actually pass, we assume a width-1 rectangle isn't the right option
                else:
                    if corner1[0] < corner2[0]:
                        if corner1[1] < corner2[1]:
                            corner3 = [corner1[0], corner2[1]]
                            corner4 = [corner2[0], corner1[1]]
                        else:
                            corner3 = [corner2[0], corner1[1]]
                            corner4 = [corner1[0], corner2[1]]
                    else:
                        if corner1[1] < corner2[1]:
                            corner3 = [corner2[0], corner1[1]]
                            corner4 = [corner1[0], corner2[1]]
                        else:
                            corner3 = [corner1[0], corner2[1]]
                            corner4 = [corner2[0], corner1[1]]

                if True:
                    largest_area = max(largest_area, (abs(corner1[0] - corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1))

    print(largest_area)


#part_one()
part_two()


