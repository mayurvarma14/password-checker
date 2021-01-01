import requests
import hashlib
import sys


def get_password_hashes(hash):
    url = 'https://api.pwnedpasswords.com/range/'+hash
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching:{response.status_code}')
    return response


def hash_password(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1_password


def password_leak_count(hashes, current_hash):
    hashes = (line.split(':') for line in hashes)
    for hash, count in hashes:
        if hash == current_hash:
            return count
    return 0


def check_password(password):
    hashed_password = hash_password(password)
    first5_char, remaining_char = hashed_password[:5], hashed_password[5:]
    response = get_password_hashes(first5_char)
    hashes = response.text.splitlines()
    count = password_leak_count(hashes, remaining_char)
    return count
