import hashlib
from ecdsa import SigningKey, SECP256k1
import base58
import sys

# Define the start and end values for the range
start_value = int("0000000000000000000000000000000000000000000000031FAF356A70ED600", 16)
end_value = int("000000000000000000000000000000000000000000000003B02291E89C062000", 16)

# Load addresses from address.txt
with open("address.txt", "r") as file:
    target_addresses = [line.strip() for line in file if line.strip()]

# Loop through the range
for value in range(start_value, end_value + 1):
    priv_key = SigningKey.from_secret_exponent(value, curve=SECP256k1)
    pub_key = priv_key.verifying_key

    address = {}
    for key_type in ['uncompressed', 'compressed']:
        hash1 = hashlib.sha256(pub_key.to_string(key_type))
        hash2 = hashlib.new('ripemd160')
        hash2.update(hash1.digest())
        network_hash = b'\x00' + hash2.digest()
        address[key_type] = base58.b58encode_check(network_hash)

    print("Private Key:                  ", priv_key.to_string().hex())
    print("Public Key Uncompressed:      ", pub_key.to_string("uncompressed").hex())
    print("Bitcoin Address Uncompressed: ", address['uncompressed'].decode())
    print("Public Key Compressed:        ", pub_key.to_string("compressed").hex())
    print("Bitcoin Address Compressed:   ", address['compressed'].decode())
    print("-----------------------------")

    # Check if generated address matches target addresses
    for target_address in target_addresses:
        if address['uncompressed'].decode() == target_address or address['compressed'].decode() == target_address:
            # Save the found address, private key, and public key to found.txt
            with open("found.txt", "a") as file:
                file.write("Private Key: {}\n".format(priv_key.to_string().hex()))
                file.write("Public Key: {}\n".format(pub_key.to_string("uncompressed").hex()))
                file.write("Bitcoin Address: {}\n".format(address['uncompressed'].decode()))
                file.write("-----------------------------\n")
            print("Match found! Address: {}".format(target_address))
            sys.exit()

print("Finished checking the range.")
