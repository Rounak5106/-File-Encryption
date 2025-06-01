 ```python
   # src/encrypt_decrypt.py
   from cryptography.fernet import Fernet
   from cryptography.hazmat.primitives import hashes
   from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
   import base64
   import os
   import logging

   # Configure logging
   logging.basicConfig(filename='logs/encryption.log', level=logging.INFO,
                       format='%(asctime)s - %(levelname)s - %(message)s')

   def derive_key(password: str, salt: bytes = None) -> tuple:
       """Derive a Fernet key from a password using PBKDF2HMAC."""
       if not salt:
           salt = os.urandom(16)
       kdf = PBKDF2HMAC(
           algorithm=hashes.SHA256(),
           length=32,
           salt=salt,
           iterations=100000,
       )
       key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
       return key, salt

   def encrypt_file(input_file: str, password: str) -> bool:
       """Encrypt a file using a password-derived key."""
       try:
           if not os.path.exists(input_file):
               logging.error(f"Input file {input_file} does not exist")
               return False

           # Derive key
           key, salt = derive_key(password)
           fernet = Fernet(key)

           # Read input file
           with open(input_file, 'rb') as f:
               data = f.read()

           # Encrypt data
           encrypted_data = fernet.encrypt(data)

           # Save encrypted file with salt prepended
           output_file = input_file + '.enc'
           with open(output_file, 'wb') as f:
               f.write(salt + encrypted_data)

           logging.info(f"Encrypted {input_file} to {output_file}")
           return True
       except Exception as e:
           logging.error(f"Encryption failed for {input_file}: {str(e)}")
           return False

   def decrypt_file(input_file: str, password: str) -> bool:
       """Decrypt an encrypted file using a password-derived key."""
       try:
           if not input_file.endswith('.enc'):
               logging.error(f"Input file {input_file} is not an encrypted file (.enc)")
               return False
           if not os.path.exists(input_file):
               logging.error(f"Input file {input_file} does not exist")
               return False

           # Read encrypted file
           with open(input_file, 'rb') as f:
               file_data = f.read()

           # Extract salt and encrypted data
           salt, encrypted_data = file_data[:16], file_data[16:]

           # Derive key
           key, _ = derive_key(password, salt)
           fernet = Fernet(key)

           # Decrypt data
           decrypted_data = fernet.decrypt(encrypted_data)

           # Save decrypted file
           output_file = input_file[:-4] + '.decrypted'
           with open(output_file, 'wb') as f:
               f.write(decrypted_data)

           logging.info(f"Decrypted {input_file} to {output_file}")
           return True
       except Exception as e:
           logging.error(f"Decryption failed for {input_file}: {str(e)}")
           return False
   ```
