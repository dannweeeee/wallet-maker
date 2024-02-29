# EVM Wallet Maker

Python script to bulk-create wallets for Ethereum and other EVM-based blockchains. <br />
The script will generate a CSV file containing the wallet addresses and private keys.

## Usage

### Enter the number of wallets you would like to bulk-create

```bash
if __name__ == "__main__":
    num_wallets = 100 # number of wallets you would like to create
    wallets = create_eth_wallets(num_wallets)

    save_to_csv(wallets)
    print(f"{num_wallets} wallets saved to eth_wallets.csv.")
```

### Install Python Packages

```bash
python -m pip install web3
```

### Run Python Script

```bash
python walletmaker.py
```

## Precaution

ENSURE THAT THE CSV FILE IS STORED IN A SAFE LOCATION.<br />
THE PRIVATE KEYS SHOULD NOT BE LEAKED TO ANYONE.
