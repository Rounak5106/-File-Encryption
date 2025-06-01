 # src/main.py
from encrypt_decrypt import encrypt_file, decrypt_file
from getpass import getpass
import os
import logging

logging.basicConfig(filename='logs/encryption.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    print("File Encryption/Decryption Tool")
    while True:
        print("\nOptions:")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
        choice = input("Enter choice (1-3): ")

        if choice == '3':
            print("Exiting...")
            break

        if choice not in ['1', '2']:
            print("Invalid choice. Try again.")
            continue

        file_path = input("Enter file path: ")
        if not os.path.exists(file_path):
            print("File does not exist.")
            logging.error(f"File {file_path} not found")
            continue

        password = getpass("Enter password: ")

        if choice == '1':
            if encrypt_file(file_path, password):
                print(f"File encrypted successfully as {file_path}.enc")
            else:
                print("Encryption failed. Check logs for details.")
        elif choice == '2':
            if decrypt_file(file_path, password):
                print(f"File decrypted successfully as {file_path[:-4]}.decrypted")
            else:
                print("Decryption failed. Check logs or password.")

if __name__ == "__main__":
    main()
