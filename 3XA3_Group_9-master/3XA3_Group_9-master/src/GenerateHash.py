import hashlib
## @file GenerateHash.py
#  @title GenerateHash
#  @author Illya Pilipenko
#  @date 2018-10-24


## @brief Hash Algorithm Retrival Function
#  @details Maps the user requested hash type to the corresponding hash encoding in the hashlib library
#  @param hash_type The string the user enters corresponding to a specific hash encoding
#  @return The hash encoding from the hashlib library that has the name hash_type, or if the requested
#   encoding is not found/ isn't supported in the running Python interpreter, a randomly selected
#   supported encoding
def _retrieve_hash_algorithm(hash_type):
    hash_list = {h: hashlib.new(h) for h in retrieve_available_hash_encodings()}
    if hash_type in hash_list:
        return hash_list[hash_type]
    return next(iter(hash_list.values()))


## @brief Set of Available Hash Algorithms
#  @details Returns a set of hash encodings available in the running Python interpreter
#  @return A set of available hashes
def retrieve_available_hash_encodings():
    return hashlib.algorithms_available


## @brief Hash Output Generation Function
#  @details Uses the selected hash encoding to produce a set of output bytes that will be further used to
#   generate colours
#  @param hash_input A string passed in by the user that will serve as input to the hash function
#  @param hash_type An string parameter corresponding to the name of the hash encoding. If omitted, sha256
#   encoding is assumed
#  @return A hex string representation of the output of the hash function
def generate_hash(hash_input, hash_type='sha256'):
    hash_algorithm = _retrieve_hash_algorithm(hash_type)

    input_bytes = bytes(hash_input, encoding='utf-8')
    hash_algorithm.update(input_bytes)

    return hash_algorithm.hexdigest()
