from collections import namedtuple

FileInfo = namedtuple('FileInfo', 'file, algo, hash')


def loader(file):
    file_list = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            if line:
                file_list.append(FileInfo._make(line.split()))
    return file_list
