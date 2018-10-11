# coding: utf-8

from crypto import HDPrivateKey, HDKey

from itertools import permutations

def findkey(word, address):
    master_key = HDPrivateKey.master_key_from_mnemonic(word)

    root_keys = HDKey.from_path(master_key, "m/44'/60'/0'")
    acct_priv_key = root_keys[-1]

    keys = HDKey.from_path(acct_priv_key, '{change}/{index}'.format(change=0, index=0))
    private_key = keys[-1]
    public_key = private_key.public_key

    print("Private key (hex, compressed): " + private_key._key.to_hex())
    print("Address: " + private_key.public_key.address())
    add = private_key.public_key.address()
    if add == address:
        return 'true'

    return 'false'

def permutations(L):
    if len(L) == 1:
        yield L
    else:
        a = [L.pop(0)]
        for p in permutations(L):
            for i in range(len(p) + 1):
                yield p[:i] + a + p[i:]

res = findkey('stay involve clerk code orient gloom session organ hip ship place trim', '0x86d5329fbe3556b1f8e16f95c45c18bf314d2efb')
res = findkey('stomach relief holiday limb learn seat culture sort deer push brick wrong', '0x78b9fc862209272bd216baaea9bbeecf4117546c')


print(res)
L = ['wrong']
#L = ['holiday', 'relief', 'seat', 'stomach', 'limb', 'sort', 'learn', 'culture', 'push', 'deer', 'brick', 'wrong']


i = 0
for l in permutations(L):
    #print(l)
    i = i + 1
    print("i: ", i)
    words = ''
    for w in l:
        if len(words) == 0:
            words = w
        else:
            words = words + ' ' + w
    print("word: ", words)
    res = findkey(words, '0x78b9fc862209272bd216baaea9bbeecf4117546c')
    if res == 'true':
        print (l)
        break
