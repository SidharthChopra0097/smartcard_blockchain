# main.py

from blockchain_smartcard import SmartCardBlockchain
from smartcard import read_smartcard_data

def main():
    # Instantiate the blockchain
    blockchain = SmartCardBlockchain()

    # Read data from the smartcard
    smartcard_data = read_smartcard_data()

    # Register the smartcard on the blockchain
    print("Registering smartcard on the blockchain...")
    blockchain.register_smartcard(smartcard_data)
    print("Smartcard registered successfully.")

    # Authenticate the smartcard
    print("Authenticating smartcard...")
    if blockchain.authenticate_smartcard(smartcard_data):
        print("Smartcard authenticated successfully.")
    else:
        print("Smartcard authentication failed.")

if __name__ == "__main__":
    main()
