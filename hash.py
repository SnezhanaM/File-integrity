import hashlib


def hasher(file, algo):
    BLOCK_SIZE = 65536
    hash_sum = None

    if algo == 'md5':
        hash_sum = hashlib.md5()

    elif algo == 'sha1':
        hash_sum = hashlib.sha1()

    elif algo == 'sha256':
        hash_sum = hashlib.sha256()

    with open(file, 'rb') as f:
        if hash_sum:
            fb = f.read(BLOCK_SIZE)
            while len(fb) > 0:
                hash_sum.update(fb)
                fb = f.read(BLOCK_SIZE)

            return hash_sum.hexdigest()

    return None
