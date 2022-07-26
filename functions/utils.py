from secret_sdk.client.lcd.lcdclient import LCDClient
from secret_sdk.client.lcd.wallet import Wallet
from secret_sdk.key.mnemonic import MnemonicKey
from env import endpoint, bot_key

CHAIN_ID = 'secret-4'

def bot_init():
    client = LCDClient(endpoint, CHAIN_ID)
    wallet = Wallet(client, MnemonicKey(bot_key))
    return client, wallet