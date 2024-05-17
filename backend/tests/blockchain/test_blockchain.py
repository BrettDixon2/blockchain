from backend.blockchain.blockchain import BlockChain
from backend.blockchain.block import GENESIS_DATA

def test_blockchain_instance():
    blockchain = BlockChain()
    assert blockchain.chain[0].hash == GENESIS_DATA['hash']

def test_add_block():
    blockchain = BlockChain()
    data = 'test-data'
    blockchain.add_block(data)
    assert blockchain.chain[-1].data == data
    assert blockchain.chain[-1].last_hash == blockchain.chain[-2].hash
    
