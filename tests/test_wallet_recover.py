from stubs.ExplorerClientStub import TFChainExplorerGetClientStub

import tfchain

def test():
    # create a tfchain client for devnet
    c = tfchain.TFChainClient.TFChainClient(network_type="devnet")

    # (we replace internal client logic with custom logic as to ensure we can test without requiring an active network)
    explorer_client = TFChainExplorerGetClientStub()
    c.explorer_get = explorer_client.explorer_get

    # the devnet genesis seed is the seed of the wallet,
    # which receives all block stakes and coins in the genesis block of the tfchain devnet
    DEVNET_GENESIS_SEED="carbon boss inject cover mountain fetch fiber fit tornado cloth wing dinosaur proof joy intact fabric thumb rebel borrow poet chair network expire else"

    # create a new devnet wallet
    w = tfchain.TFChainWallet.TFChainWallet(seed=DEVNET_GENESIS_SEED, client=c)
    # we create a new wallet using an existing seed,
    # such that our seed is used and not a new randomly generated seed

    # a tfchain wallet uses the underlying tfchain client for all its
    # interaction with the tfchain network
    assert w.network_type == tfchain.TFChainClient.NetworkType.DEVNET

    # by default we still have 1 address only,
    # you can change this however by creating a new wallet with the `key_count` parameter
    # set to a value higher than 1
    assert w.key_count == 1
    # the first address is known for the genesis devnet wallet
    assert w.address == '015df22a2e82a3323bc6ffbd1730450ed844feca711c8fe0c15e218c171962fd17b206263220ee'

    # the next 2 addresses are known as well
    assert w.address_new() == '01095d1811ae152aad0a5dd40588d8414e3bc3132ce8bd2405df13df164635646e3afe5e3af280'
    assert w.address_new() == '0183ccf250c5a13b0b0bbe452eb65afdb551bd8c572bf45714a2f8cf37239afa3aaa114cdc8b57'
    # our wallet now has 3 addresses
    assert w.key_count == 3
