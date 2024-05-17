from backend.blockchain.block import Block, GENESIS_DATA

def test_mine_block():
    last_block = Block.genesis()

    data = 'test-data'
    block = Block.mine_block(last_block,data)

    assert isinstance(block, Block)
    assert block.data == data
    assert block.last_hash == last_block.hash



def test_genesis():
    genesis = Block.genesis()

    assert isinstance(genesis, Block)
    for key, value in genesis.__dict__.items():
        assert getattr(genesis, key) == getattr(Block.genesis(), key)

    for key in GENESIS_DATA:
        assert getattr(genesis,key) == GENESIS_DATA[key]