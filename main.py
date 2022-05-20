import math
import datetime
import os.path
import sys


def load_file(file_name):
    arr = []
    with open(file_name, "r", encoding="cp1250") as f:
        for line in f:
            for word in line.split():
                arr.append(word.lower())
    return arr


def edit_distance(str1, str2, m, n):
    mat = [[0 for i in range(n + 1)] for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):

            if j == 0:
                mat[i][j] = i

            elif i == 0:
                mat[i][j] = j

            elif str1[i - 1] != str2[j - 1]:
                mat[i][j] = 1 + min(mat[i][j - 1],
                                    mat[i - 1][j],
                                    mat[i - 1][j - 1])

            else:
                mat[i][j] = mat[i - 1][j - 1]
    return mat[m][n]


def longest_common_subseq(str1, str2, m, n):
    mat = [[0 for i in range(n + 1)] for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                mat[i][j] = mat[i - 1][j - 1] + 1
            else:
                mat[i][j] = max(mat[i - 1][j], mat[i][j - 1])

    return mat[m][n]


def check_fixed(word, fixed_dict):
    fixed = ""
    if word in fixed_dict.keys():
        fixed = fixed_dict[word]
    return fixed


def get_fixed_words(dict, words, type, fixed_dict):
    for idx, j in enumerate(words):
        if j in dict:
            words[idx] = j
            continue

        sht = math.inf
        lng = 0
        word = check_fixed(j, fixed_dict)

        if word != "":
            words[idx] = word
            continue

        for i in dict:
            n = len(i)
            m = len(j)

            if n < (m - 2) or n > (m + 2):
                continue

            if type == 1:
                count = edit_distance(j, i, m, n)
                if count < sht:
                    sht = count
                    word = i
            else:
                count = longest_common_subseq(j, i, m, n)
                if count > lng:
                    lng = count
                    word = i

        if word != "":
            fixed_dict[j] = word
            words[idx] = word

    return words


def compare(vystup, pvstup):
    right = 0
    for i in range(len(vystup)):
        if vystup[i] == pvstup[i]:
            right += 1

    perc = (right * 100) / len(vystup)
    print(f'Number of all words: {len(vystup)}\n'
          f'Number of correct words: {right}\n'
          f'Number of incorrect words: {len(vystup) - right}\n'
          f'Success Rate: {perc:5.2f}%')


def write_fixed(fixed, file_name):
    f = open(file_name, 'w', encoding="cp1250")
    for ele in fixed:
        f.write(ele + ' ')
    f.close()


def init(dictionary_file, input_file, fixed_input_file, output_file, type):
    fixed_dict = {}
    dict = load_file(dictionary_file)
    input = load_file(input_file)
    g_v = load_file(fixed_input_file)

    start = datetime.datetime.now()
    fixed = get_fixed_words(dict, input, type, fixed_dict)
    write_fixed(fixed, output_file)
    end = datetime.datetime.now()

    if type == 1:
        print('\nType: Edit distance')
    else:
        print('\nType: Longest common subseq')

    p_v = load_file(output_file)
    compare(p_v, g_v)
    dif = end - start
    print(f'Length of repair: {dif.total_seconds():5.2f} s')


def get_files(type):
    dictionary = ""
    inpt = ""
    if type == "R":
        dictionary = input("Write name of dictionary file: ")
        inpt = input("Write name of file with incorrect words: ")
    fixed = input("Write name of file with correct words: ")
    output0 = input("Write name of first output file: ")
    output1 = input("Write name of second output file: ")

    return dictionary, inpt, fixed, output0, output1


def check_file(list):
    for x in list:
        if os.path.isfile(x):
            continue
        else:
            print(f"File {x} not exist")
            exit()


def load_input(type, dictionary, inpt, fixed, output1, output0):
    if type == "R":
        check_file([dictionary, inpt, fixed])
        init(dictionary, inpt, fixed, output1, 1)
        init(dictionary, inpt, fixed, output0, 0)

    elif type == "C":
        check_file([output1, output0])
        g_v = load_file(fixed)
        p_v1 = load_file(output1)
        p_v0 = load_file(output0)

        print('\nFirst file:')
        compare(p_v0, g_v)

        print('\nSecond file:')
        compare(p_v1, g_v)

    else:
        exit()


def main():
    if len(sys.argv) == 6:
        type = "R"
        dictionary, inpt, fixed, output0, output1 = str(sys.argv[1]), str(
            sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]), str(sys.argv[5])
        load_input(type, dictionary, inpt, fixed, output1, output0)

    else:
        while True:
            type = input("\nType R/C to repair or compare files: ")
            dictionary, inpt, fixed, output0, output1 = get_files(type)
            load_input(type, dictionary, inpt, fixed, output1, output0)


main()
