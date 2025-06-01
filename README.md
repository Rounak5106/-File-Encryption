# Security Considerations

Developed for my internship at **Micro IT**, this tool uses the following security measures.

## Encryption Algorithm
- **Fernet**: Symmetric encryption using AES-128 in CBC mode with PKCS7 padding.
- **Authentication**: HMAC-SHA256 ensures data integrity.
- **Key Derivation**: PBKDF2HMAC with SHA256, 100,000 iterations, and random salt.

## Security Features
- **Random Salt**: Unique per encryption, stored with the encrypted file.
- **Password Protection**: Keys derived from user passwords, not stored.
- **Error Handling**: Prevents data corruption from invalid inputs.

## Best Practices
- Use strong, unique passwords.
- Store passwords securely (e.g., password manager).
- Avoid sharing encrypted files publicly without secure channels.
- Check `logs/encryption.log` for unauthorized access attempts.

## Limitations
- Weak passwords reduce security.
- No brute-force protection; use complex passwords.
- Fernet is symmetric; consider asymmetric encryption for advanced use cases.
