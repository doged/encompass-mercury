import imp, os, pkgutil

import chains

blockchains = []
active_chain = None

def init_chains():
    global blockchains

    chain_names = [name for a, name, b in pkgutil.iter_modules(chains.__path__)]
    chain_modules = [__import__('encompassmercury.chains.'+name, fromlist=['encompassmercury.chains']) for name in chain_names]

    # skip these non-coins
    non_coins = ['cryptocur', 'hashes']
    for name, c in zip(chain_names, chain_modules):
        if name in non_coins:
            continue
        try:
            blockchains.append( c.Currency() )
        except Exception:
            print('Cannot initialize coin {}!'.format(name))

def get_active_chain():
    if len(blockchains) == 0:
        init_chains()
    return active_chain

def set_active_chain(chaincode):
    if len(blockchains) == 0:
        init_chains()
    global active_chain
    active_chain = get_chain_instance(chaincode)

def get_chain_instance(chaincode):
    for c in blockchains:
        if chaincode.upper() == c.code.upper():
            return c
