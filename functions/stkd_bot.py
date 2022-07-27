# Functions that execute code on for the stkd_secret contract
import utils, time

SECURITY_BOT = ""

def unbond_batch():
    client, wallet = utils.bot_init()

    cur_time = int(time.time())
    utils.log("stkd_log.csv", "\nCurrent time: " + str(cur_time))

    query_msg = {"next_unbonding_batch_time": {"time": cur_time}}
    query_result = client.wasm.contract_query(SECURITY_BOT, query_msg)
    next_unbonding_batch_time = query_result['next_unbonding_batch_time']['time']
    utils.log("stkd_log.csv", "Next unbonding batch time " + str(next_unbonding_batch_time))

    if cur_time > next_unbonding_batch_time:
        handle_msg = {"unbond_batch": {}}
        utils.log("stkd_log.csv", "Trying to batch unbond...")
        handle_result = wallet.execute_tx(SECURITY_BOT, handle_msg, gas=430000, gas_prices="125uscrt", gas_adjustment=0.001)
        if not handle_result.is_tx_error():
            utils.log("stkd_log.csv", "Batch successfully completed")
        else:
            utils.log("stkd_log.csv", "Something went wrong with unbond_batch!")
    else:
        utils.log("stkd_log.csv", "Time hasn't reached for executing batch unbond, waiting for next round")

def compound_rewards():
    _, wallet = utils.bot_init()
    
    cur_time = int(time.time())
    utils.log("stkd_log.csv", "\nCurrent time: " + str(cur_time))

    utils.log("stkd_log.csv", "Trying to compound rewards...")
    handle_msg = {"compound_rewards": {}}
    handle_result = wallet.execute_tx(SECURITY_BOT, handle_msg, gas=250000, gas_prices="125uscrt", gas_adjustment=0.001)

    if not handle_result.is_tx_error():
        utils.log("stkd_log.csv", "Compound Rewards Complete")
    else:
        utils.log("stkd_log.csv", "Something went wrong with compound rewards!")

def rebalance():
    client, wallet = utils.bot_init()
    
    cur_time = int(time.time())
    utils.log("stkd_log.csv", "\nCurrent time: " + str(cur_time))

    query_msg = {"next_rebalance_time": {"time": cur_time}}
    query_result = client.wasm.contract_query(SECURITY_BOT, query_msg)
    next_rebalance_time = query_result['next_rebalance_time']['time']
    utils.log("stkd_log.csv", "Next rebalance time " + str(next_rebalance_time))

    if cur_time > next_rebalance_time:
        handle_msg = {"rebalance": {}}
        utils.log("stkd_log.csv", "Trying to rebalance...")
        handle_result = wallet.execute_tx(SECURITY_BOT, handle_msg, gas=250000, gas_prices="125uscrt", gas_adjustment=0.001)
        if not handle_result.is_tx_error():
            utils.log("stkd_log.csv", "Rebalance Complete")
        else:
            utils.log("stkd_log.csv", "Something went wrong with rebalance!")
    else:
        utils.log("stkd_log.csv", "Time hasn't reached for rebalancing, waiting for next round")

def save_staking_info():
    client, _ = utils.bot_init()

    cur_time = int(time.time())
    utils.log("stkd_log.csv", "\nCurrent time: " + str(cur_time))

    query_msg = {"staking_info": {"time": cur_time}}
    query_result = client.wasm.contract_query(SECURITY_BOT, query_msg)

    utils.log("stkd_log.csv", "Current state: " + str(query_result))
