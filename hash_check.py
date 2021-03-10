import sys
from load_file import loader
from hash import hasher


def main(file, dir):
    data_list = loader(file)

    for el in data_list:
        try:
            file_hash = hasher(dir + '/' + el.file, el.algo)
            if el.hash == file_hash:
                print(el.file, 'OK')

            elif el.hash != file_hash:
                if file_hash is None:
                    print(el.file, 'Unsupported hash algorithm')
                else:
                    print(el.file, 'FAIL')

        except FileNotFoundError:
            print(el.file, 'NOT FOUND')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Invalid call data')

    else:
        input_file = sys.argv[1]
        directory = sys.argv[2]
        if directory[-1] == '/':
            directory = directory[:-1]

        main(input_file, directory)

