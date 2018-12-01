# coding: utf-8

from crypto import HDPrivateKey, HDKey

from itertools import permutations

def findkey(word, address):

    #bip 39: 将 seed 用方便记忆和书写的单字表示。一般由 12 个单字组成，称为 mnemonic code(phrase)，中文称为助记词或助记码
    master_key = HDPrivateKey.master_key_from_mnemonic(word)

    #bit 44: 基于 BIP32 的系统，赋予树状结构中的各层特殊的意义。让同一个 seed 可以支援多币种、多帐户等
    root_keys = HDKey.from_path(master_key, "m/44'/60'/0'")
    acct_priv_key = root_keys[-1]

    #bit 32: 定义 Hierarchical Deterministic wallet (简称 “HD Wallet”)，是一个系统可以从单一个 seed 产生一树状结构储存多组 keypairs（私钥和公钥）
    keys = HDKey.from_path(acct_priv_key, '{change}/{index}'.format(change=0, index=0))
    private_key = keys[-1]
    public_key = private_key.public_key

    # print("Private key (hex, compressed): " + private_key._key.to_hex())
    # print("Address: " + private_key.public_key.address())
    add = private_key.public_key.address()
    if add == address:
        return 'true'

    return 'false'



master_key, mnemonic = HDPrivateKey.master_key_from_entropy()
print('BIP32 Wallet Generated.')
print('Mnemonic Secret: ' + mnemonic)

from crypto import HDPrivateKey, HDKey
master_key = HDPrivateKey.master_key_from_mnemonic('laundry snap patient survey sleep strategy finger bone real west arch protect')
root_keys = HDKey.from_path(master_key,"m/44'/60'/0'")
acct_priv_key = root_keys[-1]
for i in range(6):
    keys = HDKey.from_path(acct_priv_key,'{change}/{index}'.format(change=0, index=i))
    private_key = keys[-1]
    public_key = private_key.public_key
    print("Index %s:" % i)
    print("  Private key (hex, compressed): " + private_key._key.to_hex())
    print("  Address: " + private_key.public_key.address())

# res = findkey('stay involve clerk code orient gloom session organ hip ship place trim', '0x86d5329fbe3556b1f8e16f95c45c18bf314d2efb')
# res = findkey('stomach relief holiday limb learn seat culture sort deer push brick wrong', '0x78b9fc862209272bd216baaea9bbeecf4117546c')
#
#
# print(res)
# #L = ['wrong']
# L = ['holiday', 'relief', 'seat', 'stomach', 'limb', 'sort', 'learn', 'culture', 'push', 'deer', 'brick', 'wrong']
#
# i = 0
# for l in permutations(L):
#     #print(l)
#     i = i + 1
#     print("i: ", i)
#     words = ''
#     for w in l:
#         if len(words) == 0:
#             words = w
#         else:
#             words = words + ' ' + w
#     print("word: ", words)
#     res = findkey(words, '0x78b9fc862209272bd216baaea9bbeecf4117546c')
#     if res == 'true':
#         print (l)
#         break
