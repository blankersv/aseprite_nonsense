
with open('advent12.txt', 'r') as file:
    advent = file.read().split('\n')

practice = False
if practice:
    advent = ['0:',
              '###',
              '##.',
              '##.',
              '',
              '1:',
              '###',
              '##.',
              '.##',
              '',
              '2:',
              '.##',
              '###',
              '##.',
              '',
              '3:',
              '##.',
              '###',
              '##.',
              '4:',
              '###',
              '#..',
              '###',
              '',
              '5:',
              '###',
              '.#.',
              '###',
              '',
              '4x4: 0 0 0 0 2 0',
              '12x5: 1 0 1 0 2 2',
              '12x5: 1 0 1 0 3 2']


def part_one():
    print('Part one:')
    # just going to do the very dumb thing of trying to check if the total area can accommodate the area of the presents
    # EVERYTHING IS LIQUID
    

    shape_dict = {}
    for ll in range(len(advent)):
        if advent[ll] == '':
            shape_dict[int(advent[ll-4][:-1])] = advent[ll-3:ll]

    count_dict = {}
    for ind in shape_dict:
        count_dict[ind] = sum([x.count('#') for x in shape_dict[ind]])

    count = 0
    first_region_index = 0
    while first_region_index == 0:
        if advent[count].count('x') > 0:
            first_region_index = count
        count += 1

    good_regions = 0
    for ll in range(first_region_index, len(advent)):
        region_area = int(advent[ll][:advent[ll].find('x')]) * int(advent[ll][advent[ll].find('x')+1 : advent[ll].find(':')])
        region_list = [int(x) for x in advent[ll][advent[ll].find(':')+2:].split()]
        liquid_area = 0
        for ii in range(len(region_list)):
            liquid_area += region_list[ii] * count_dict[ii]
        if liquid_area <= region_area:
            good_regions += 1
        print(liquid_area)

    print(good_regions)




part_one()

