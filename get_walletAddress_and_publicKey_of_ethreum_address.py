from eth_account import Account
from eth_account.signers.local import (
    LocalAccount,
)

# Your private key (example key, do NOT use in production)

key = input("Your private key without '0x' in it: ")

private_key = key

# Create an account object from the private key
account: LocalAccount = Account.from_key(private_key)

# Get the public key
public_key = account._key_obj.public_key

# Get the wallet address
wallet_address = account.address

# Print the results
print(f"Public Key: {public_key}")
print(f"Wallet Address: {wallet_address}")
