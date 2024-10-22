import csv
from web3 import Web3

def create_eth_wallets(num_wallets):
    w3 = Web3()

    wallets = []
    for _ in range(num_wallets):
        acc = w3.eth.account.create()
        private_key = w3.to_hex(acc._private_key)
        address = acc.address
        wallet = {
            'address': address,
            'private_key': private_key,
        }
        wallets.append(wallet)

    return wallets

def save_to_csv(wallets, csv_filename='eth_wallets.csv'):
    with open(csv_filename, mode='w', newline='') as file:
        fieldnames = ['Address', 'Private Key']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for wallet in wallets:
            writer.writerow({
                'Address': wallet['address'],
                'Private Key': wallet['private_key'],
            })

if __name__ == "__main__":
    num_wallets = 100
    wallets = create_eth_wallets(num_wallets)

    save_to_csv(wallets)
    print(f"{num_wallets} wallets saved to eth_wallets.csv.")
