import json
import base64
from algosdk import wallet
from algosdk import account, mnemonic, constants
from algosdk.v2client import algod
from algosdk.future import transaction
from algosdk import kmd
kmd_clt = kmd.KMDClient( )

def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))
    
seed = wallet.generate_mnemonic
w = wallet.create_wallet(network="USDT", seed=seed, children=1)
print(w)
if kmd_clt:
    kmd_wlt_mdk = None
    kmd_wlt_list = kmd_clt.list_wallets()
    for kmd_wlt in kmd_wlt_list:
        kmd_name = kmd_wlt['name']
        kmd_id = kmd_wlt['id']
        if kmd_name :
            kmd_wlt_hdl = kmd_clt.init_wallet_handle(kmd_id, )
            if kmd_wlt_hdl:
                kmd_wlt_mdk = kmd_clt.export_master_derivation_key(kmd_wlt_hdl, )
            break
    if kmd_wlt_mdk:
        wlt = wallet.Wallet(, , kmd_clt, mdk=kmd_wlt_mdk)
        if wlt:
            acc_addr_list = wlt.list_keys()
            for acc_addr in acc_addr_list:
                account_address = acc_addr
                print(account_address)
                account_key = wlt.export_key(acc_addr)
                print(account_key)
                account_mnemonic = mnemonic.from_private_key(account_key)
                print(account_mnemonic)
def create_wallet(self, name, pswd, driver_name="sqlite",
                  master_deriv_key=None):
    """
    Create a new wallet.
    Args:
        name (str): wallet name
        pswd (str): wallet password
        driver_name (str, optional): name of the driver
        master_deriv_key (str, optional): if recovering a wallet, include
    Returns:
        dict: dictionary containing wallet information
    """
    req = "/wallet"
    query = {
        "wallet_driver_name": driver_name,
        "wallet_name": name,
        "wallet_password": pswd
    }
    if master_deriv_key:
        query["master_derivation_key"] = master_deriv_key
    return self.kmd_request("POST", req, data=query)["wallet"]




# Write down the address, private key, and the passphrase for later usage
generate_algorand_keypair()

def first_transaction_example(private_key, my_address):
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    print("My address: {}".format(my_address))
    account_info = algod_client.account_info(my_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')))

    # build transaction
    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    params.flat_fee = constants.MIN_TXN_FEE 
    params.fee = 1000
    receiver = "HZ57J3K46JIJXILONBBZOHX6BKPXEM2VVXNRFSUED6DKFD5ZD24PMJ3MVA"
    amount = 100000
    note = "Hello World".encode()

    unsigned_txn = transaction.PaymentTxn(my_address, params, receiver, amount, None, note)

    # sign transaction
    signed_txn = unsigned_txn.sign(private_key)

    # submit transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Signed transaction with txID: {}".format(txid))

    # wait for confirmation 
    try:
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)  
    except Exception as err:
        print(err)
        return

    print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=4)))
    print("Decoded note: {}".format(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode()))

    print("Starting Account balance: {} microAlgos".format(account_info.get('amount')) )
    print("Amount transfered: {} microAlgos".format(amount) )    
    print("Fee: {} microAlgos".format(params.fee) ) 


    account_info = algod_client.account_info(my_address)
    print("Final Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")



# replace private_key and my_address with your private key and your address.
first_transaction_example(private_key, my_address)
#submit transaction
txid = algod_client.send_transaction(signed_txn)
print("Successfully sent transaction with txID: {}".format(txid))

    # wait for confirmation 
try:
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)  
except Exception as err:
        print(err)
        return

print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=4)))
print("Decoded note: {}".format(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode()))
print("Starting Account balance: {} microAlgos".format(account_info.get('amount')) )
print("Amount transfered: {} microAlgos".format(amount) )    
print("Fee: {} microAlgos".format(params.fee) ) 


account_info = algod_client.account_info(my_address)
print("Final Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")​
