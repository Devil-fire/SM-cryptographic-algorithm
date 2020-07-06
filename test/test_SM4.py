from SM import SM4
plain = b'123456'
key = b'0123456789abcdef'
SM4crypto = SM4.SM4()
IV = SM4crypto.IV_generate()
encrypto = SM4crypto.encrypt(plain,key,IV)
decrypto = SM4crypto.decrypt(encrypto,key,IV)
assert plain == decrypto
