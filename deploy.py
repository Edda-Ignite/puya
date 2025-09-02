import os
from algosdk.v2client.algod import AlgodClient
from algosdk import account, mnemonic, transaction
from beaker import client

# This is a sample mnemonic, DO NOT use this for real assets.
# Replace this with your own Testnet mnemonic.
mnemonic_phrase = "your 25-word mnemonic goes here"

# Connect to the Algorand Testnet
algod_address = "https://testnet-api.algosandbox.io"
algod_token = ""  # For public sandbox, token is often empty

algod_client = AlgodClient(algod_token, algod_address)

def deploy_app():
    # Load the smart contract from the contract.py file
    from contract import GitHubBoxContract
    app = GitHubBoxContract()

    # Get the private key and address from your mnemonic
    private_key = mnemonic.to_private_key(mnemonic_phrase)
    sender_address = account.address_from_private_key(private_key)

    print(f"Deploying from account: {sender_address}")

    # Create the application client
    app_client = client.ApplicationClient(
        client=algod_client,
        app=app,
        sender=private_key,
    )

    print("Creating application...")
    
    # Deploy the application
    app_id, app_address, tx_id = app_client.create()

    # Call the method to create the box initially
    app_client.call(app.create_github_box)

    print(f"Application deployed with ID: {app_id}")
    print(f"Transaction ID: {tx_id}")

    # Return the deployed application ID for later use
    return app_id

if __name__ == "__main__":
    app_id = deploy_app()
    print(f"\nYour deployed Application ID is: {app_id}")
    
    # Optional: Save the Application ID to workshop-submission.txt
    with open("workshop-submission.txt", "w") as f:
        f.write(str(app_id))
    print("Application ID saved to workshop-submission.txt.")
