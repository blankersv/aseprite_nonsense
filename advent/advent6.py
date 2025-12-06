
with open('advent6.txt', 'r') as file:
    advent = file.read().split('\n')

practice = False
if practice:
    advent = ['123 328  51 64 ',
              ' 45 64  387 23 ',
              '  6 98  215 314',
              '*   +   *   +  ']


def part_one():
    print('Part one:')

    for ln in range(len(advent)):
        advent[ln] = [x for x in advent[ln].split(' ') if x != '']
    numbers = advent[:-1]
    operations = advent[-1:][0]

    run_total = 0
    for col in range(len(numbers[0])):
        col_total = int(numbers[0][col])
        if operations[col] == '*':
            for num in range(1, len(numbers)):
                col_total *= int(numbers[num][col])
        elif operations[col] == '+':
            for num in range(1, len(numbers)):
                col_total += int(numbers[num][col])
        run_total += col_total
    print(run_total)


def part_two():
    print('Part two:')
    # I'm going to assume the operator is always on the far left of the column and hope that works
    run_total = 0
    current_nums = []
    for cc in range(len(advent[0])):
        col_num = ''
        for digg in range(len(advent) - 1):
            col_num += advent[digg][len(advent[0]) - cc - 1]
            col_num.replace(' ', '')
        current_nums.append(col_num.replace(' ', ''))
        current_nums = [int(x) for x in current_nums if x != '']

        if advent[-1][len(advent[0])-cc-1] == '+':
            col_total = sum(current_nums)
            run_total += col_total
            current_nums = []
        elif advent[-1][len(advent[0])-cc-1] == '*':
            col_total = 1
            for num in current_nums:
                col_total *= num
            run_total += col_total
            current_nums = []
        else:
            pass

    print(run_total)


#part_one()
part_two()


