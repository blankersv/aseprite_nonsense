
with open('advent3.txt', 'r') as file:
    advent = file.read().split('\n')

practice = False
if practice:
    advent = ['987654321111111',
              '811111111111119',
              '234234234234278',
              '818181911112111']


def part_one():
    litbats = []
    for line in advent:
        bat1 = 9
        while bat1 > 0:
            if str(bat1) in line[:-1]:
                bat2 = 9
                while bat2 > 0:
                    if str(bat2) in line[line.find(str(bat1))+1:]:
                        litbats.append(str(bat1)+str(bat2))
                        bat2 = 0
                        bat1 = 0
                    bat2 -= 1
            bat1 -= 1

    print(sum([int(x) for x in litbats]))


def part_two():

    numbats = 12
    litbats = []

    for line in advent:
        bats = [9 for x in range(0, numbats)]
        bank = line[:]
        for bb in range(len(bats)):
            while bats[bb] > 0:
                if str(bats[bb]) in bank[:len(bank) - (numbats - 1) + bb]:
                    bank = bank[bank.find(str(bats[bb])) + 1:]
                    bats[bb] = -bats[bb]
                else:
                    bats[bb] -= 1


        litbats.append(bats)


    run_total = 0
    for bank in litbats:
        bat_str = ''
        for bat in bank:
            bat_str += str(-bat)
        run_total += int(bat_str)

    print(run_total)




#part_one()
part_two()

