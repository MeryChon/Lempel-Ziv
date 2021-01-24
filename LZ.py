import sys
import os


def read_data_from_file(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        return data


def write_to_file(file_path, data):
    with open(file_path, "w") as f:
        f.write(data)


# Initialize table with single character strings
#     P = first input character
#     WHILE not end of input stream
#         C = next input character
#         IF P + C is in the string table
#             P = P + C
#         ELSE
#             output the code for P
#             add P + C to the string table
#             P = C
#     END WHILE
#     output code for P
def lz_compress(data):
    dictionary = {
        "0": 1,
        "1": 2
    }
    dict_counter = 2

    compressed_list = []

    current_substr = data[0]
    for i in range(0, len(data) - 1):
        next_symbol = data[i + 1]
        print("current_substr: " + current_substr + "; next_symbol: " + next_symbol)
        if (current_substr + next_symbol) in dictionary:
            current_substr = current_substr + next_symbol
        else:
            current_substr_code = dictionary[current_substr]
            print("current_substr_code: " + str(current_substr_code))
            compressed_list.append(current_substr_code)

            dictionary[current_substr + next_symbol] = dict_counter + 1
            dict_counter += 1

            current_substr = next_symbol
    compressed_list.append(dictionary[current_substr])
    print(dictionary)

    return compressed_list


# Initialize table with single character strings
#  OLD = first input code
#  output translation of OLD
#  WHILE not end of input stream
#      NEW = next input code
#      IF NEW is not in the string table
#             S = translation of OLD
#             S = S + C
#     ELSE
#            S = translation of NEW
#     output S
#     C = first character of S
#     OLD + C to the string table
#     OLD = NEW
# END WHILE
def lz_decompress(compressed):
    print(compressed)

    dictionary = {
        1: "0",
        2: "1"
    }
    dict_count = 2

    result = []
    old = compressed[0]
    result.append(dictionary[old])
    c = ''

    for i in range(0, len(compressed) - 1):
        new = compressed[i + 1]
        print("old: " + str(old) + "; new: " + str(new) + "; c: " + c)
        if new not in dictionary:
            s = dictionary[old]
            s = s + c
        else:
            s = dictionary[new]
        print("s: " + s)
        result.append(s)
        c = s[0]
        print("c: " + c)
        dict_count += 1
        dictionary[dict_count] = dictionary[old] + c
        old = new
    print(result)
    return result


def main(argv):
    file_name = argv[0]
    dir_path = os.path.dirname(__file__)

    data = read_data_from_file(os.path.join(dir_path, file_name))
    print(data)

    compressed_data = lz_compress(data)
    print(compressed_data)

    # write_to_file(os.path.join(dir_path, "compressed.txt"), compressed_data)

    decompressed_data = lz_decompress(compressed_data)

    # write_to_file(os.path.join(dir_path, "decompressed.txt"), decompressed_data)


if __name__ == "__main__":
    main(sys.argv[1:])
