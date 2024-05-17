from backend.blockchain.block import Block

class BlockChain:
    """
    blockchain is a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1],data))

    def __repr__(self):
        return f'blockchain: {self.chain}'
    
def main():

    blockchain = BlockChain()
    blockchain.add_block('one')
    blockchain.add_block('two')
    print(f'blockchain.py __name__: {__name__}')

    print(blockchain)

if __name__ == "__main__":
    main()