from pyhmy import contract,transaction,account
from pyhmy.util import convert_one_to_hex
from web3 import Web3,providers
import json

#define wallet address
test_wallet_address = 'one18t4yj4fuutj83uwqckkvxp9gfa0568uc48ggj7' #example wallet

#get all contracts (manually created via https://explorer.harmony.one/hrc20 - have not found any subgraphs yet)
with open("contracts.json", "r") as contract_file:
    contract_dict = json.load(contract_file)
    
#get metamask abi (application binary interface)
with open("metamask_abi.txt", "r") as abi_file:
    contract_abi = abi_file.read()

#connect to web3 via testnet or mainnet
test_net = 'https://api.s0.b.hmny.io' #get an error when I try to read HRC20 Tokens on test server!
main_net = 'https://rpc.s0.t.hmny.io'
w3 = Web3(providers.HTTPProvider(main_net))

#get ONE balance
one_balance = account.get_balance(test_wallet_address, endpoint=main_net)

#haven't figured out how to get the ONE decimal via pyhmy library.
asset_dict={}
asset_dict['ONE'] = one_balance*10**(-18)

#loop through HRC20 contracts listed in JSON file
for symbol,contract_addr in contract_dict['tokens'].items():

    #compile metamask abi and get token balances
    contract_data = w3.eth.contract(abi=contract_abi, address=convert_one_to_hex(contract_addr))
    balance_bytes = contract_data.functions.balanceOf(convert_one_to_hex(test_wallet_address)).call()
    contract_decimals = contract_data.functions.decimals().call()
    
    if balance_bytes > 0:
        #convert balance to decimal number
        balance = balance_bytes*10**(-1*contract_decimals)
        
        #store in dictionary
        asset_dict[symbol] = balance
        
        #print(balance,symbol)

#print all assets in wallet
print(asset_dict)