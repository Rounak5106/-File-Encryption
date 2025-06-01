 # tests/test_encrypt_decrypt.py
import os
from encrypt_decrypt import encrypt_file, decrypt_file

def test_encrypt_decrypt():
    test_file = "test.txt"
    test_content = b"Hello, this is a test!"
    password = "testpassword"

    with open(test_file, 'wb') as f:
        f.write(test_content)

    assert encrypt_file(test_file, password) == True
    assert os.path.exists(test_file + '.enc')

    assert decrypt_file(test_file + '.enc', password) == True
    decrypted_file = test_file + '.decrypted'
    assert os.path.exists(decrypted_file)

    with open(decrypted_file, 'rb') as f:
        decrypted_content = f.read()
    assert decrypted_content == test_content

    os.remove(test_file)
    os.remove(test_file + '.enc')
    os.remove(decrypted_file)

if __name__ == "__main__":
    test_encrypt_decrypt()
    print("Tests passed!")
