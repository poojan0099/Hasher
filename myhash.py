import random
import string
import hashlib

def hashify(size=8, password=None):

    if password is None:
        password_characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
        password = "".join(random.sample(password_characters, len(password_characters)))[:size]

    password_encoded = bytes(password, encoding='utf-8')

    return (
        password, {
            "blake2b": hashlib.blake2b(password_encoded).hexdigest(),
            "blake2s": hashlib.blake2s(password_encoded).hexdigest(),
            "md5": hashlib.md5(password_encoded).hexdigest(),
            "sha1": hashlib.sha1(password_encoded).hexdigest(),
            "sha224": hashlib.sha224(password_encoded).hexdigest(),
            "sha256": hashlib.sha256(password_encoded).hexdigest(),
            "sha384": hashlib.sha384(password_encoded).hexdigest(),
            "sha3_224": hashlib.sha3_224(password_encoded).hexdigest(),
            "sha3_256": hashlib.sha3_256(password_encoded).hexdigest(),
            "sha3_384": hashlib.sha3_384(password_encoded).hexdigest(),
            "sha3_512": hashlib.sha3_512(password_encoded).hexdigest(),
            "sha512": hashlib.sha512(password_encoded).hexdigest()
        }
    )


if __name__ == '__main__':
    globe = globals()
    state = hashify(password='kai')
    total = ["blake2b", "blake2s", "md5", "sha1", "sha224", "sha256",
             "sha384", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "sha512"]

    print(state)


