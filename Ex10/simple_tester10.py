from ex10 import *
import time


def tester():
    start_time = time.time()
    records = parse_data('Data/big_data.txt')
    symptoms = ["cough", "fatigue", "headache", "nausea", "fever",
                "irritability", "rigidity", "sore_throat"]

    # Building Tree
    try:
        root = build_tree(records, symptoms)
        print('Built Tree in :', float(time.time()) - float(start_time),
              'seconds.')
    except:
        print("Could not build a tree. Sorry. :(")
        return

    # Tests:

    print('Test #1:')
    diagnoser = Diagnoser(root)
    diagnosis = diagnoser.diagnose(["cough"])
    if diagnosis == "healthy":
        print("Test passed -", diagnosis)
    else:
        print("Test failed. Should have printed healthy, printed: ", diagnosis)

    print('\n#2: Error_rate:')
    error_rate = diagnoser.calculate_error_rate(records)
    if round(error_rate, 6) == 0.097167:
        print("Test passed -", error_rate)
    else:
        print("Test failed. error rate should be 0.097167: ",
              round(error_rate, 6))
    # print(diagnoser.calculate_error_rate(records))

    print('\n#3: All Illnesses:')
    all_illnesses = diagnoser.all_illnesses()
    illnesses = ['cold', 'healthy', 'influenza', 'meningitis', 'mono', 'strep']
    if set(all_illnesses) == set(illnesses):
        print("Test passed -", all_illnesses)
    else:
        print("Test failed. Should have printed", illnesses, ", printed: ",
              all_illnesses)
    # print(diagnoser.all_illnesses())

    print('\n#4: Most Common:')
    most_common = diagnoser.most_common_illness(records)
    if most_common == "mono":
        print("Test passed -", most_common)
    else:
        print("Test failed. Should have printed mono, printed: ", most_common)

    illness = 'strep'
    print('\n#5: Path to illness:', illness)

    path_to_strep = [[False, False, False, True, True, False, False, True],
                     [False, False, False, True, True, False, False, False],
                     [False, False, False, True, False, False, False, True],
                     [False, False, False, True, False, False, False, False],
                     [False, False, False, False, True, False, False, True],
                     [False, False, False, False, True, False, False, False],
                     [False, False, False, False, False, False, False, True]]
    path = diagnoser.paths_to_illness(illness)
    if path.sort() == path_to_strep.sort():
        print("Test passed")
    else:
        print("Test failed. Should have printed", path_to_strep,
              "\n\n\nprinted: ", path)

    print('\n#7: Finding Optimal Trees')
    check_optimal(records, symptoms)
    print('Total Runtime:', float(time.time()) - float(start_time))


def check_optimal(records, symptoms):
    for depth in range(1, 8):
        root = optimal_tree(records, symptoms, depth)
        diagnoser = Diagnoser(root)
        error_rate = diagnoser.calculate_error_rate(records)
        print('for depth:', depth, 'error rate:', error_rate)


if __name__ == "__main__":
    tester()
