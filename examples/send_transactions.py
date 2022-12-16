"""
### How to send transaction with the BeezX client:

We simulate the creation of two wallets: the sender and the receiver of the transaction.
Wallets are created by the BeezX library through the RSA PublicKey algorithm, which is a well trusted public key algorithm,
which rely on the difficulty of factorizing large integers. 
RSA can be used for both:
1. Confidentality (encryption)
2. Digital Signature

The RSA algorithm provides a keys pair for each wallet: the secret and the public key.
From the public key, the BeezX library compute the wallet address (the nickname's wallet).

The sender wallet creates a transaction instance of type transaction type (exchange in this example).
The transaction is signed with the sender pub key. These steps are performed with the create_transaction wallet's method.


"""

from pathlib import Path
import sys
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from beez.wallet.wallet import Wallet

# create the wallets
sender_wallet = Wallet()
receiver_wallet = Wallet()
print(f'SENDER WALLET: {sender_wallet.address}')
print(f'RECEIVER WALLET: {receiver_wallet.address}')

# print(f'SENDER PubKey: {sender_wallet.public_key_string()}')

# the BeezX wallet has itw own method for creating and signing a transaction of type trasaction_type
transaction = sender_wallet.create_transaction(
    receiver=receiver_wallet.public_key_string(), 
    amount=1000, 
    transaction_type='exchange')

print(f'TRANSACTION:\n{transaction.to_json()}')