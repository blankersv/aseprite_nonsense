
with open('advent5.txt', 'r') as file:
    advent = file.read().split('\n')

practice = False
if practice:
    advent = ['3-5',
              '10-14',
              '16-20',
              '12-18',
              '',
              '1',
              '5',
              '8',
              '11',
              '17',
              '32']

ranges = advent[:advent.index('')]
ingredients = advent[advent.index('')+1:]


def part_one():
    count_fresh = 0
    for ing in ingredients:
        fresh = False
        for ran in ranges:
            if int(ing) >= int(ran[:ran.find('-')]) and int(ing) <= int(ran[ran.find('-')+1:]):
                fresh = True
        if fresh:
            count_fresh += 1

    print(count_fresh)


def part_two():

    intervals = ranges[:]

    changes = True
    while changes:
        old_intervals = intervals[:]
        for ran in intervals:
            c = int(ran[:ran.find('-')])
            d = int(ran[ran.find('-') + 1:])
            all_new = True
            for inv in intervals:
                a = int(inv[:inv.find('-')])
                b = int(inv[inv.find('-') + 1:])
                if b < c or d < a:  # disjoint
                    pass
                elif a <= c and d <= b:  # second contained in first
                    all_new = False
                elif c < a and b < d:  # first contained in second
                    intervals.pop(intervals.index(inv))
                    intervals.append(str(c) + '-' + str(d))
                elif a <= c and b <= d:  # overlap with first on left
                    intervals.pop(intervals.index(inv))
                    intervals.append(str(a) + '-' + str(d))
                elif c <= a and d <= b:  # overlap with second on left
                    intervals.pop(intervals.index(inv))
                    intervals.append(str(c) + '-' + str(b))
            if all_new:
                keep_going = False
                intervals.append(str(c) + '-' + str(d))

        if intervals == old_intervals:
            changes = False

    intervals = list(set(intervals))
    print(intervals)
    run_sum = 0
    for inv in intervals:
        a = int(inv[:inv.find('-')])
        b = int(inv[inv.find('-') + 1:])
        run_sum += (b - a + 1)
    print(run_sum)

    #339668510830757


#part_one()
part_two()






