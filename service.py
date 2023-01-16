from bticoin.rpc import RawProxy

class BitcoindService:
    def __init__(self):
        # TODO determine whether
        # to set env info or take params
        # to configure a connection to Bitcoind Node.
        self._proxy = RawProxy()
    
    def get_chain_info(self) -> dict:
        """
            getblockchaininfo call
        """
        try:
            return self._proxy.getblockchaininfo()
        except Exception as e:
            # TODO handle
            print(str(e))
            raise e
    
    def get_tx_by_id(self, tx_id: int) -> dict:
        """
            getrawtransactionid call
            decoderawtransaction call
        """
        try:
            raw_tx = self._proxy.getrawtransaction(tx_id)
            # TODO should be its own helper method
            return self._proxy.decoderawtransaction(raw_tx)
        except Exception as e:
            # TODO handle
            print(str(e))
            raise e
    
    def tx_value_per_block(self, block: dict) -> int:
        """
            Iterates txns in a block and calculates the
            total value, denominated in BTC.
        """
        block_value = 0
        for tx_id in block.get("tx", []):
            tx_value = 0
            tx = self.get_tx_by_id(tx_id)
            for op in tx.get("vouts", []):
                tx_value += op.get("value", 0)
            block_value += tx_value

    def get_block_by_height(self, height: int) -> dict:
        """
            getblockhash call
        """
        try:
            block_hash = self._proxy.getblockhash(height)
            return self._proxy.getblock(block_hash)
        except Exception as e:
            # TODO handle
            print(str(e))
            raise e

