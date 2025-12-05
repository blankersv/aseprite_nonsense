
with open('advent4.txt', 'r') as file:
    advent = file.read().split('\n')

practice = False
if practice:
    advent = ['..@@.@@@@.',
              '@@@.@.@.@@',
              '@@@@@.@.@@',
              '@.@@@@..@.',
              '@@.@@@@.@@',
              '.@@@@@@@.@',
              '.@.@.@.@@@',
              '@.@@@.@@@@',
              '.@@@@@@@@.',
              '@.@.@@@.@.']

advent = [list(line) for line in advent]


def part_one():
    reachable = 0
    configuration = advent

    for row_i in range(len(configuration)):
        for col_i in range(len(configuration[0])):
            if configuration[row_i][col_i] == '@':
                count = 0
                # if top edge
                if row_i == 0:
                    if col_i == 0 or col_i == len(configuration[0]) - 1:
                        pass  # keep this pass
                    else:
                        for yy in [-1, 0, 1]:
                            for xx in [0, 1]:
                                if configuration[row_i + xx][col_i + yy] == '@':
                                    count += 1
                # if bottom edge
                elif row_i == len(configuration) - 1:
                    if col_i == 0 or col_i == len(configuration[0]) - 1:
                        pass  # keep this pass
                    else:
                        for yy in [-1, 0, 1]:
                            for xx in [-1, 0]:
                                if configuration[row_i + xx][col_i + yy] == '@':
                                    count += 1
                # if left edge
                elif col_i == 0:
                    for yy in [0, 1]:
                        for xx in [-1, 0, 1]:
                            if configuration[row_i + xx][col_i + yy] == '@':
                                count += 1
                # if right edge
                elif col_i == len(configuration) - 1:
                    for yy in [-1, 0]:
                        for xx in [-1, 0, 1]:
                            if configuration[row_i + xx][col_i + yy] == '@':
                                count += 1
                else:
                    for yy in [-1, 0, 1]:
                        for xx in [-1, 0, 1]:
                            if configuration[row_i + xx][col_i + yy] == '@':
                                count += 1
                if count <= 4:
                    reachable += 1

    print(reachable)


def part_two():
    configuration = advent
    total_reached = 0
    reachable = 1
    indices_to_change = []
    while reachable > 0:

        reachable = 0
        for row_i in range(len(configuration)):
            for col_i in range(len(configuration[0])):
                if configuration[row_i][col_i] == '@':
                    count = 0
                    # if top edge
                    if row_i == 0:
                        if col_i == 0 or col_i == len(configuration[0]) - 1:
                            pass  # keep this pass
                        else:
                            for yy in [-1, 0, 1]:
                                for xx in [0, 1]:
                                    if configuration[row_i + xx][col_i + yy] == '@':
                                        count += 1
                    # if bottom edge
                    elif row_i == len(configuration) - 1:
                        if col_i == 0 or col_i == len(configuration[0]) - 1:
                            pass  # keep this pass
                        else:
                            for yy in [-1, 0, 1]:
                                for xx in [-1, 0]:
                                    if configuration[row_i + xx][col_i + yy] == '@':
                                        count += 1
                    # if left edge
                    elif col_i == 0:
                        for yy in [0, 1]:
                            for xx in [-1, 0, 1]:
                                if configuration[row_i + xx][col_i + yy] == '@':
                                    count += 1
                    # if right edge
                    elif col_i == len(configuration) - 1:
                        for yy in [-1, 0]:
                            for xx in [-1, 0, 1]:
                                if configuration[row_i + xx][col_i + yy] == '@':
                                    count += 1
                    else:
                        for yy in [-1, 0, 1]:
                            for xx in [-1, 0, 1]:
                                if configuration[row_i + xx][col_i + yy] == '@':
                                    count += 1
                    if count <= 4:
                        reachable += 1
                        indices_to_change.append([row_i, col_i])

        total_reached += reachable

        for pair_ind in range(len(indices_to_change)):
            first_ind = indices_to_change[pair_ind][0]
            second_ind = indices_to_change[pair_ind][1]
            configuration[first_ind][second_ind] = '.'

    print(total_reached)


#part_one()
part_two()






