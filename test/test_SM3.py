from SM import SM3
SM3hash = SM3.SM3()
x = SM3hash.SM3(b'abc')
assert x == '66c7f0f462eeedd9d1f2d46bdc10e4e24167c4875cf2f7a2297da02b8f4ba8e0'
SM3hash = SM3.SM3()
x = SM3hash.SM3(b'abcd'*16)
assert x == 'debe9ff92275b8a138604889c18e5a4d6fdb70e5387e5765293dcba39c0c5732'