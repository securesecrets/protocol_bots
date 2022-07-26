# Functions that execute code on for the stkd_secret contract
import utils

SECURITY_BOT = ""

def unbond_batch():
    client, wallet = utils.bot_init()

    time = int(time.time())
    utils.log("stkd_log.csv", "\nCurrent time: " + str(time))

    query_msg = {"next_unbond_batch_time": {"time": time}}
    query_result = client.wasm.contract_query(SECURITY_BOT, query_msg)
    next_unbonding_batch_time = query_result['next_unbonding_batch_time']['time']
    utils.log("stkd_log.csv", "Next unbonding batch time " + str(next_unbonding_batch_time))

    if time > next_unbonding_batch_time:
        handle_msg = {"unbond_batch": {}}
        utils.log("stkd_log.csv", "Trying to batch unbond...")
        handle_result = wallet.execute_tx(SECURITY_BOT, handle_msg, gas=430000, gas_prices=0.125)
        if not handle_result.is_tx_error():
            utils.log("stkd_log.csv", "Batch successfully completed")
    else:
        utils.log("stkd_log.csv", "Time hasn't reached for executing batch, waiting for next round")

def compound_rewards():
    _, wallet = utils.bot_init()

    handle_msg = {"compound_rewards": {}}
    handle_result = wallet.execute_tx(SECURITY_BOT, handle_msg, gas=250000, gas_prices=0.125)

    if not handle_result.is_tx_error():
        utils.log("stkd_log.csv", "\nRewards compounded")

def rebalace():
    _, wallet = utils.bot_init()

    handle_msg = {"rebalance": {}}
    handle_result = wallet.execute_tx(SECURITY_BOT, handle_msg, gas=250000, gas_prices=0.125)

    if not handle_result.is_tx_error():
        utils.log("stkd_log.csv", "\nRedelegate Complete")

def save_staking_info():
    client, wallet = utils.bot_init()

    time = int(time.time())
    utils.log("stkd_log.csv", "\nCurrent time: " + str(time))

    query_msg = {"staking_info": {"time": time}}
    query_result = client.wasm.contract_query(SECURITY_BOT, query_msg)

    utils.log("stkd_log.csv", "Staking Info: " + str(query_result.to_json()))
