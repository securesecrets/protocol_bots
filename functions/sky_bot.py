# functions that execute actions for the sky contract
from utils import bot_init

SWAP_AMOUNT = "1000000" # .01 SHD

SKY_ADDR = ''
SKY_HASH = ''
SKY_QUERY = {"is_any_cycle_profitable":{"amount":SWAP_AMOUNT}}
SKY_HANDLE = {"arb_cycle":{"amount":SWAP_AMOUNT, "index":"0"}}

def execute_arb():
    client, wallet = bot_init()
    res = client.wasm.contract_query(SKY_ADDR, SKY_QUERY)
    for (i, cycles) in enumerate(res['is_any_cycle_profitable']["is_profitable"]):
        if cycles:
            SKY_HANDLE["arb_cycle"]["index"] = str(i)
            wallet.execute_tx(SKY_ADDR, SKY_HANDLE)
