from algosdk.v2client import algod
from algosdk.transaction import ApplicationCreateTxn, StateSchema, OnComplete, wait_for_confirmation
from algosdk import account, mnemonic

# === CONFIG ===
ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"
ALGOD_TOKEN = ""  # No token needed for Algonode
MNEMONIC = "junk frame cram pattern midnight include rice morning spoil family bright detect immune absent ugly acid seek busy hazard gift choice enrich camp absorb duty"

# === SETUP ===
client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)
private_key = mnemonic.to_private_key(MNEMONIC)
sender = account.address_from_private_key(private_key)

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
