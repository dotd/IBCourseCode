# -*- coding: utf-8 -*-
"""
IBAPI - Getting Contract info

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
import time


class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString, advancedOrderRejectJson):
        print("Error {} {} {}".format(reqId, errorCode, errorString))

    def contractDetails(self, reqId, contractDetails):
        print("redID: {}\ncontract:{}\n".format(reqId, contractDetails))


def websocket_con():
    print("Before app.run()")
    app.run()
    print("Before event.wait()")
    event.wait()
    print("Before if")
    if event.is_set():
        app.close()


event = threading.Event()
app = TradingApp()
app.connect("127.0.0.1", 7497, clientId=1)

# starting a separate daemon thread to execute the websocket connection
con_thread = threading.Thread(target=websocket_con)
con_thread.start()
time.sleep(1)  # some latency added to ensure that the connection is established

# creating object of the Contract class - will be used as a parameter for other function calls
contract = Contract()
contract.symbol = "AAPL"
contract.secType = "STK"
contract.currency = "USD"
contract.exchange = "SMART"

app.reqContractDetails(100, contract)  # EClient function to request contract details
print("Before sleep")
time.sleep(5)  # some latency added to ensure that the contract details request has been processed
print("after sleep")
event.set()
print("after set")
