import networkx as nx

def find_connected_components_networkx(edges):
    G = nx.Graph()
    G.add_edges_from(edges)
    return list(nx.connected_components(G))


def parse_tuple(strang):
    return [int(x) for x in strang.split(',')]


with open('advent8.txt', 'r') as file:
    advent = file.read().split('\n')

num_connections = 1000

practice = False
if practice:
    advent = ['162,817,812',
              '57,618,57',
              '906,360,560',
              '592,479,940',
              '352,342,300',
              '466,668,158',
              '542,29,236',
              '431,825,988',
              '739,650,466',
              '52,470,668',
              '216,146,977',
              '819,987,18',
              '117,168,530',
              '805,96,715',
              '346,949,466',
              '970,615,88',
              '941,993,340',
              '862,61,35',
              '984,92,344',
              '425,690,689']
    num_connections = 10


def part_one():
    print('Part one:')
    # used the networkx library for this so I don't have to do a depth-first search by hand

    distances = [[0 for ii in range(len(advent))] for jj in range(len(advent))]
    distances_ls = []
    for ii in range(len(advent)):
        for jj in range(ii+1, len(advent)):
            pi = parse_tuple(advent[ii])
            pj = parse_tuple(advent[jj])
            distances[ii][jj] = sum([(pi[kk] - pj[kk])**2 for kk in range(3)])
            distances_ls.append([distances[ii][jj],ii,jj])

    sorted_dists = sorted(distances_ls, key=lambda x: x[0])[:num_connections]
    print(sorted_dists)

    edges = []
    for box in sorted_dists:
        edges.append([box[1],box[2]])
    prod = 1
    for ll in sorted([len(x) for x in find_connected_components_networkx(edges)],reverse=True)[:3]:
        prod *= ll
    print(prod)


def part_two():
    print('Part two:')
    # the subreddit is mentioning "heaps of heaps" and "min heap" and such. I don't know how to do this,
    # so I'm just reusing the code from part 1

    num_conn = num_connections
    newest_comps = [[0]]

    distances = [[0 for ii in range(len(advent))] for jj in range(len(advent))]
    distances_ls = []
    for ii in range(len(advent)):
        for jj in range(ii + 1, len(advent)):
            pi = parse_tuple(advent[ii])
            pj = parse_tuple(advent[jj])
            distances[ii][jj] = sum([(pi[kk] - pj[kk]) ** 2 for kk in range(3)])
            distances_ls.append([distances[ii][jj], ii, jj])
    base_sorted_dists = sorted(distances_ls, key=lambda x: x[0])

    while len(newest_comps[0]) != len(advent):
        sorted_dists = base_sorted_dists[:num_conn]

        newest_i = sorted_dists[-1][1]
        penult_i = sorted_dists[-1][2]

        edges = []
        for box in sorted_dists:
            edges.append([box[1], box[2]])
        newest_comps = find_connected_components_networkx(edges)
        print(len(newest_comps[0]))
        num_conn += 1

    # print(sorted_dists)
    # print(newest_comps)
    print(parse_tuple(advent[newest_i])[0] * parse_tuple(advent[penult_i])[0])


#part_one()
part_two()


