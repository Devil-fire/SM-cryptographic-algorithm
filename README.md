使用Python构建了国密算法中的SM3杂凑密码算法和SM4对称密码算法

SM3：杂凑密码算法，将任意长度（小于$2^{64}$的消息压缩为256位消息摘要）

```Python
from SM import SM3
SM3hash = SM3.SM3()
x = SM3hash.SM3(b'abc')
```

SM4：对称密码算法，使用分组加密，每组长度位128位（只支持cbc）

初始化：

```python
SM4crypto = SM4.SM4()
IV = SM4crypto.IV_generate() #生成初始向量
```

加密：

```python
encrypto = SM4crypto.encrypt(plain,key,IV)
```

解密：

```python
decrypto = SM4crypto.decrypt(encrypto,key,IV)
```

