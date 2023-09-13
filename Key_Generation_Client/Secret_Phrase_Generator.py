import hashlib


def generate_int_from_random(random_value, client_id):
    value = client_id
    if value == 1:
        print("Use SHA-256")
        random_bytes = str(random_value).encode('utf-8')
        hash_object = hashlib.sha256()
        hash_object.update(random_bytes)
        hash_hex = hash_object.hexdigest()
        generated_int = int(hash_hex, 16)
        return generated_int
    elif value == 2:
        print("Use SHA-512")
        random_bytes = str(random_value).encode('utf-8')
        hash_object = hashlib.sha512()
        hash_object.update(random_bytes)
        hash_hex = hash_object.hexdigest()
        generated_int = int(hash_hex, 16)
        return generated_int
    elif value == 3:
        print("Use SHA-384")
        random_bytes = str(random_value).encode('utf-8')
        hash_object = hashlib.sha384()
        hash_object.update(random_bytes)
        hash_hex = hash_object.hexdigest()
        generated_int = int(hash_hex, 16)
        return generated_int
    elif value == 4:
        print("Use SHA-512")
        random_bytes = str(random_value).encode('utf-8')
        hash_object = hashlib.sha512()
        hash_object.update(random_bytes)
        hash_hex = hash_object.hexdigest()
        generated_int = int(hash_hex, 16)
        return generated_int
