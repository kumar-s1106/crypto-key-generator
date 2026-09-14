import secrets
import datetime
import os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

def generate_symmetric():
    return secrets.token_hex(32)

def generate_keypair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key

def save_symmetric(key):
    filename = "key_" + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
    with open(filename, "w") as f:
        f.write("SYMMETRIC KEY\n")
        f.write("Generated: " + str(datetime.datetime.now()) + "\n")
        f.write("Bits: 256\n")
        f.write("Key: " + key + "\n")
    print("Saved to " + filename)

def save_keypair(private_key, public_key, private=True):
    pub_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open("public.pem", "wb") as f:
        f.write(pub_pem)
    print("Public key saved to public.pem")

    if private:
        priv_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open("private.pem", "wb") as f:
            f.write(priv_pem)
        print("Private key saved to private.pem")
        print("WARNING: Keep private.pem secret. Never share it.")
    else:
        print("Private key discarded.")

print("=" * 60)
print("SECURE KEY GENERATOR")
print("=" * 60)

while True:
    print("\n1. Generate 256-bit symmetric key")
    print("2. Generate RSA public/private keypair")
    print("3. View saved keys")
    print("4. Delete saved keys")
    print("5. Exit")

    choice = input("\nChoice: ")

    if choice == "1":
        key = generate_symmetric()
        print("\nGenerated key:")
        print(key)
        print("Bits: 256")

        action = input("\nSave or discard? (s/d): ")
        if action == "s":
            use = input("Public or private use? (pub/priv): ")
            save_symmetric(key)
            if use == "pub":
                print("Note: symmetric keys are not meant for public sharing.")
                print("Consider using RSA keypair for public/private use instead.")
            else:
                print("Key saved for private use. Keep it secret.")
        else:
            print("Key discarded.")

    elif choice == "2":
        print("\nGenerating RSA 2048-bit keypair...")
        private_key, public_key = generate_keypair()

        print("\nPublic key preview:")
        pub_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        print(pub_pem.decode())

        action = input("Save or discard? (s/d): ")
        if action == "s":
            save_priv = input("Save private key too? (y/n): ")
            save_keypair(private_key, public_key, private=(save_priv == "y"))
        else:
            print("Keypair discarded.")
    elif choice == "3":
        print("\n--- Saved Keys ---")
        if os.path.exists("public.pem"):
            print("\nPUBLIC KEY:")
            print(open("public.pem").read())
        else:
            print("No public key found.")
        if os.path.exists("private.pem"):
            print("PRIVATE KEY EXISTS - saved in private.pem")
        else:
            print("No private key found.")

    elif choice == "4":
        confirm = input("Are you sure? This deletes all saved keys (y/n): ")
        if confirm == "y":
            if os.path.exists("public.pem"):
                os.remove("public.pem")
                print("public.pem deleted.")
            if os.path.exists("private.pem"):
                os.remove("private.pem")
                print("private.pem deleted.")
        else:
            print("Cancelled.") 
    elif choice == "5":
        print("Exiting.")
        break
    else:
        print("Invalid choice.")
