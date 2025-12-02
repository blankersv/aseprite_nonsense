
with open('advent1.txt', 'r') as file:
    advent = file.read().splitlines()

practice = False
if practice:
    advent = ['L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']

def part_one():

    position = 50
    zero_counter = 0

    for rot in advent:
        direction = 1 if rot[0]=='R' else -1
        position = (position + (direction * int(rot[1:]))) % 100
        #print(position)
        if position == 0:
            zero_counter += 1

    print(zero_counter)

def part_two():

    position = 50
    zero_counter = 0

    for rot in advent:

        #print('Position', position)

        # figure out the direction
        direction = 1 if rot[0]=='R' else -1

        # figure out the minimum number of zero the rotation hits for any rotation
        # the actual number will sometimes be one more
        amount = int(rot[1:])
        zero_counter += (amount // 100)
        remainder = amount % 100
        #print('Moving', direction * remainder)

        # if we're going to the right, we check to see if we passed zero by seeing if
        # position + remainder >= 100; if it is, we've hit zero
        if direction == 1:
            if position + remainder >= 100:
                zero_counter += 1
                #print('Hit zero here!')

        # if we're going to the left, we check to see if we passed zero by seeing if
        # position - remainder <= 0:
        if direction == -1:
            # problems double counting when we start at 0 and then move left;
            # we just subtract off to cancel this
            if position == 0:
                zero_counter -= 1
            if position - remainder <= 0:
                zero_counter += 1
                #print('Hit zero here!')

        position = ((position + (direction * remainder)) % 100)

    print('Zero counter', zero_counter, '\n')

part_two()


