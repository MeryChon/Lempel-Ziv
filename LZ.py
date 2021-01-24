import sys
import os


def read_data_from_file(file_name):
    with open(file_name, "r") as f:
        data = f.read()
        return data


def write_to_file(file_path, data):
    with open(file_path, "w") as f:
        f.write(data)


def lz_compress(data):
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}

    compressed_list = []

    current_substr = data[0]
    for i in range(0, len(data) - 1):
        next_symbol = data[i + 1]
        if (current_substr + next_symbol) in dictionary:
            current_substr = current_substr + next_symbol
        else:
            current_substr_code = dictionary[current_substr]
            compressed_list.append(current_substr_code)

            dictionary[current_substr + next_symbol] = dict_size + 1
            dict_size += 1

            current_substr = next_symbol
    compressed_list.append(dictionary[current_substr])

    return compressed_list


def lz_decompress(compressed):
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))

    result = []
    old = compressed[0]
    result.append(dictionary[old])
    c = dictionary[old]

    for i in range(0, len(compressed) - 1):
        new = compressed[i + 1]
        if new not in dictionary:
            s = dictionary[old]
            s = s + c
        else:
            s = dictionary[new]
        result.append(s)
        c = s[0]
        dict_size += 1
        dictionary[dict_size] = dictionary[old] + c
        old = new
    return ''.join(result)


def main(argv):
    file_name = argv[0]
    dir_path = os.path.dirname(__file__)

    data = read_data_from_file(os.path.join(dir_path, file_name))

    compressed_data = lz_compress(data)

    decompressed_data = lz_decompress(compressed_data)
    print(data == decompressed_data)


if __name__ == "__main__":
    main(sys.argv[1:])
