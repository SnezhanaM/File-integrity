import sys
import hashlib
from collections import namedtuple

FileInfo = namedtuple('FileInfo', 'file, algo, hash')


def loader(file):
    file_list = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            if line:
                file_list.append(FileInfo._make(line.split()))
    return file_list


def hasher(file, algo):
    BLOCK_SIZE = 65536
    file_hash = None

    if algo == 'md5':
        file_hash = hashlib.md5()

    elif algo == 'sha1':
        file_hash = hashlib.sha1()

    elif algo == 'sha256':
        file_hash = hashlib.sha256()

    with open(file, 'rb') as f:
        if file_hash:
            fb = f.read(BLOCK_SIZE)
            while len(fb) > 0:
                file_hash.update(fb)
                fb = f.read(BLOCK_SIZE)

            file_hash = file_hash.hexdigest()

    return file_hash


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
