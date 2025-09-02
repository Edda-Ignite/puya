import os
from algosdk.v2client.algod import AlgodClient
from algosdk import account, mnemonic
from beaker import client
from contract import GitHubBoxContract

# === Configuration Section ===
#
# Replace the placeholders below with your actual information.
# DO NOT use your main account mnemonic. Use a Testnet account.
# You can get a free Testnet account and Algos from a faucet.

# Your Testnet account's 25-word mnemonic phrase.
mnemonic_phrase = "your 25-word mnemonic goes here"

# Your GitHub username.
github_handle = "your-github-username"

# --- Algorand Client Setup ---
algod_address = "https://testnet-api.algosandbox.io"
algod_token = ""

# Create a client to connect to the Algorand network.
algod_client = AlgodClient(algod_token, algod_address)

# === Script Logic ===
def call_deposit_method():
    """
    Calls the `deposit` ABI method on the deployed smart contract.
    """
    # Load the smart contract from the contract.py file.
    app = GitHubBoxContract()

    # Get the private key and address from your mnemonic.
    try:
        private_key = mnemonic.to_private_key(mnemonic_phrase)
        sender_address = account.address_from_private_key(private_key)
    except Exception as e:
        print(f"Error: Invalid mnemonic phrase. Please check your mnemonic.")
        return

    print(f"Calling deposit method from account: {sender_address}")
    
    # Get the application ID from the workshop-submission.txt file.
    try:
        with open("workshop-submission.txt", "r") as f:
            app_id = int(f.read().strip())
    except FileNotFoundError:
        print("Error: workshop-submission.txt not found. Please run deploy.py first to get the Application ID.")
        return
    except ValueError:
        print("Error: Invalid Application ID in workshop-submission.txt. The file should only contain the ID number.")
        return

    # Create the application client instance.
    app_client = client.ApplicationClient(
        client=algod_client,
        app=app,
        sender=private_key,
        app_id=app_id
    )

    print(f"Calling deposit method on App ID: {app_id}...")

    # Execute the ABI method call with the GitHub handle as an argument.
    # The `box_refs` parameter tells the client which boxes to include in the transaction.
    try:
        # We pass the method name and the argument name/value.
        app_client.call(app.deposit, github_handle=github_handle.encode('utf-8'))
        print("🎉 Successfully called the deposit method and stored your GitHub handle!")
    except Exception as e:
        print(f"Failed to call deposit method: {e}")

# Run the function.
if __name__ == "__main__":
    call_deposit_method()
