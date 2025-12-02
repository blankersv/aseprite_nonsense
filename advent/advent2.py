
with open('advent2.txt', 'r') as file:
    advent = file.read().split(',')

practice = False
if practice:
    advent = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'
    advent = advent.split(',')

def is_doubled(s):
    if len(s) % 2 == 0:
        if s[:len(s)//2] == s[len(s)//2:]:
            return True
    return False

def divisors(n):
    divs = [n]
    for ii in range(2, n // 2 + 1):
        if n % ii == 0:
            divs.append(ii)
    return divs

def is_noubled(s):
    divs = divisors(len(s))
    for div in divs:
        delta = len(s) // div
        subunits = []
        for ii in range(0, div):
            subunits.append(s[ii * delta : (ii+1) * delta])
        if len(set(subunits)) == 1:
            return True
    return False


def part_one():
    running_sum = 0
    for rang in advent:
        start_num = int(rang[:rang.find('-')])
        end_num = int(rang[rang.find('-')+1:])
        for ii in range(start_num, end_num+1):
            if is_doubled(str(ii)):
                running_sum += ii

    print(running_sum)


def part_two():
    running_sum = 0
    for rang in advent:
        start_num = int(rang[:rang.find('-')])
        end_num = int(rang[rang.find('-') + 1:])
        for ii in range(start_num, end_num + 1):
            if is_noubled(str(ii)) and ii > 9:
                running_sum += ii

    print(running_sum)


part_two()

