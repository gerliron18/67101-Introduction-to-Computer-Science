import ex11_sudoku as sudoku
import ex11_map_coloring as map_colors
import ex11_improve_backtrack as improved
import time

COLORS = ['red', 'blue', 'green', 'magenta', 'yellow', 'cyan']

IMPROVED_METHODS = [improved.back_track_degree_heuristic,
                    improved.back_track_MRV,
                    improved.back_track_FC,
                    improved.back_track_LCV,
                    improved.fast_back_track]

ADJ_FILES = ['adjacency_files/adj_usa_ex11.txt',
             'adjacency_files/adj_world_ex11.txt']
ADJ_US = map_colors.read_adj_file(ADJ_FILES[0])
ADJ_WORLD = map_colors.read_adj_file(ADJ_FILES[1])

ADJ_DICTS = [ADJ_US, ADJ_WORLD]
SUDOKU_BOARDS = ['sudoku_tables/sudoku_table1.txt',
                 'sudoku_tables/sudoku_table2.txt',
                 'sudoku_tables/sudoku_table3.txt']
NUM_OF_TESTS = 20
NUM_COLORS = 4
MAP_TYPE = 0


def timer(start):
    return float(time.clock()) - float(start)


def tester(sudoku_test=False, maps_test=False):
    print('Starting Speed Tests: \n(***This does not check results, only '
          'checks speed). Use another tester for accuracy check.***')

    start_time = time.clock()
    if sudoku_test:
        sudoku_tests()
    if maps_test:
        maps_tester(NUM_COLORS, MAP_TYPE)
        # maps_tester()

    print('\n\nTotal Runtime:', float(time.clock()) - float(start_time))


def sudoku_tests():
    print('\nSudoku test:')
    for i in SUDOKU_BOARDS:
        total_time = 0
        for test in range(NUM_OF_TESTS):
            start_time = time.clock()
            sudoku.run_game(i, False)
            total_time += timer(start_time)

        print('Average Runtime for Sudoku', i, ':', total_time / NUM_OF_TESTS)


def maps_tester(num_colors, map_type, algorithms='123456'):
    print('\nMaps test:')

    total_time_general = 0
    for test in range(NUM_OF_TESTS):
        start_time = time.clock()
        map_colors.run_map_coloring(ADJ_FILES[map_type], num_colors)
        total_time_general += timer(start_time)
    average_general = total_time_general / NUM_OF_TESTS
    print('Avg runtime for General BT:', average_general)

    for i in IMPROVED_METHODS:
        total_time = 0
        for test in range(NUM_OF_TESTS):
            start_time = time.clock()
            i(ADJ_DICTS[map_type], COLORS[:num_colors])
            total_time += timer(start_time)
        average = total_time / NUM_OF_TESTS
        print('\nAvg Runtime for', i, average)
        speed = average_general / average
        if speed > 1:
            print(speed, 'times faster than General Backtracking')
        else:
            print(speed, 'times SLOWER than General Backtracking')


if __name__ == "__main__":
    tester(True, True)
