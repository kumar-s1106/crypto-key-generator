# crypto-key-generator

## Overview
A command line tool for generating cryptographically secure keys.
Supports both symmetric 256-bit hex keys and asymmetric RSA 2048-bit
public/private keypairs. Built in Python using the cryptography library.

## Features
- Generate 256-bit symmetric keys using Python secrets module
- Generate RSA 2048-bit public/private keypairs
- Save or discard keys after generation
- View saved keys from the menu
- Delete saved keys securely from the menu
- Timestamped filenames so keys never overwrite each other

## Tech Stack
- Python 3
- cryptography library (hazmat primitives)
- secrets module (cryptographically secure random)

## Installation
Install the required library:
pip install cryptography

## How To Run
python3 keygen.py

## Menu Options
1. Generate 256-bit symmetric key
2. Generate RSA public/private keypair
3. View saved keys
4. Delete saved keys
5. Exit

## Key Types Explained

### Symmetric Key
One key that does both encryption and decryption.
Like a password - whoever has it can encrypt and decrypt.
Good for encrypting files or databases.
NOT meant for public sharing - keep it secret.
Uses Python secrets module which draws from the OS
random number generator making it cryptographically secure.
secrets is used instead of random because random is
predictable and NOT safe for security applications.

### RSA Keypair
Two mathematically linked keys.
Public key  - share this freely. Others use it to encrypt
              messages to you or verify your signatures.
Private key - never share this. You use it to decrypt
              messages or sign things.
Uses RSA 2048-bit which is the industry standard for
asymmetric encryption used in HTTPS, SSH, and PGP.

## Saved Files
public.pem  - your RSA public key, safe to share
private.pem - your RSA private key, NEVER share this
key_TIMESTAMP.txt - saved symmetric keys

## Security Notes
- Private keys are saved without password encryption in
  this version. In production you would encrypt the
  private key with a passphrase.
- Symmetric keys saved to .txt files should be stored
  securely and never committed to GitHub.
- This tool uses secrets and cryptography hazmat
  primitives which are production grade libraries.
- Never use Python random module for security purposes
  as it is deterministic and predictable.

## Future Improvements
- Password protect private keys with a passphrase
- AES file encryption using the generated symmetric key
- Key expiry and rotation system
- Export keys in different formats (DER, SSH)
- GUI interface

## Author
Built as a cybersecurity project demonstrating
cryptographic key generation and management.
