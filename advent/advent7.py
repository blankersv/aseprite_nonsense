
with open('advent7.txt', 'r') as file:
    advent = file.read().split('\n')


practice = False
if practice:
    advent = ['.......S.......',
              '...............',
              '.......^.......',
              '...............',
              '......^.^......',
              '...............',
              '.....^.^.^.....',
              '...............',
              '....^.^...^....',
              '...............',
              '...^.^...^.^...',
              '...............',
              '..^...^.....^..',
              '...............',
              '.^.^.^.^.^...^.',
              '...............'
]
advent.append('.'*len(advent[0]))

def part_one():
    print('Part one:')

    beams = [[0, advent[0].find('S')]]

    split_count = 0
    for rr in range(1, len(advent)):
        for cc in range(len(advent[0])):
            if [rr-1, cc] in beams:
                if advent[rr][cc] == '.':
                    beams.append([rr, cc])
                elif advent[rr][cc] == '^':
                    beams.append([rr, cc-1])
                    beams.append([rr, cc+1])
                    split_count += 1

    print(split_count)


def part_two():
    print('Part two:')
    # visualization of this solution: https://www.reddit.com/r/adventofcode/comments/1pgbg8a/2025_day_7_part_2_visualization_for_the_sample/

    beam_matrix = [[0 for x in range(len(advent[0]))] for x in range(len(advent))]
    beam_matrix[0][advent[0].find('S')] = 1

    for rr in range(1, len(beam_matrix)):
        for cc in range(len(beam_matrix[0])):
            if beam_matrix[rr-1][cc] > 0:
                if advent[rr][cc] == '.':
                    beam_matrix[rr][cc] += beam_matrix[rr-1][cc]
                elif advent[rr][cc] == '^':
                    beam_matrix[rr][cc-1] += beam_matrix[rr-1][cc]
                    beam_matrix[rr][cc+1] += beam_matrix[rr-1][cc]

    print(sum(beam_matrix[-1:][0]))


#part_one()
part_two()


