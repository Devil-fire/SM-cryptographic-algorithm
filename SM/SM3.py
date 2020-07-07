import math
class SM3:
    def __init__(self):
        self.IV = [0x7380166f,0x4914b2b9,0x172442d7,0xda8a0600,0xa96f30bc,0x163138aa,0xe38dee4d,0xb0fb0e4e]
        self.clshift = lambda x, n:((x << n) & 0xffffffff) | ((x >> (32 - n)) & 0xffffffff)
        self.bytes_to_list = lambda data: [i for i in data]
    def T(self,j):
        if j <=15 :
            return 0x79cc4519
        else:
            return 0x7a879d8a
    def P_0(self,X):
        return X^self.clshift(X,9)^self.clshift(X,17)
    def P_1(self,X):
        return X^self.clshift(X,15)^self.clshift(X,23)
    def FF(self,j,X,Y,Z):
        if j <=15 :
            return X^Y^Z
        else:
            return (X&Y)|(X&Z)|(Y&Z)
    def GG(self,j,X,Y,Z):
        if j <=15 :
            return X^Y^Z
        else:
            return (X&Y)|(~X&Z)
    def padding(self,plain):
        plainlen = len(plain)*8
        plain.append(0x80)
        paddinglen = (512*math.ceil((plainlen-440)/512)-plainlen+440)//8
        plain.extend([0x00]*paddinglen)
        paddinglen = 16-(len(hex(plainlen))-2)
        padding_str = "0"*paddinglen+hex(plainlen)[2:]
        for i in range(0,8):
            plain.append(int(padding_str[i*2:(i+1)*2],16))
        return plain
    def SM3(self,plain):
        assert type(plain) is bytes
        plain = self.bytes_to_list(plain)
        plain = self.padding(plain)
        blocknum = (len(plain)*8)//512
        for i in range(blocknum):
            W = []
            B_i = plain[i*64:(i+1)*64]
            for j in range(16):
                tmp = B_i[j*4:(j+1)*4]
                W.append(tmp[0]*0x1000000+tmp[1]*0x10000+tmp[2]*0x100+tmp[3]*0x1)
            for j in range(16,68):
                W.append(self.P_1(W[j-16]^W[j-9]^self.clshift(W[j-3],15))^self.clshift(W[j-13],7)^W[j-6])
            for j in range(0,64):
                W.append(W[j]^W[j+4])
            V = list(self.IV)
            for j in range(0,64):
                SS1 = self.clshift((self.clshift(self.IV[0],12)+self.IV[4]+self.clshift(self.T(j),(j%32)))&0xffffffff,7)
                SS2 = SS1^self.clshift(self.IV[0],12)
                TT1 = (self.FF(j,self.IV[0],self.IV[1],self.IV[2])+self.IV[3]+SS2+W[j+68])&0xffffffff
                TT2 = (self.GG(j,self.IV[4],self.IV[5],self.IV[6])+self.IV[7]+SS1+W[j])&0xffffffff
                self.IV[3] = self.IV[2]
                self.IV[2] = self.clshift(self.IV[1],9)
                self.IV[1] = self.IV[0]
                self.IV[0] = TT1
                self.IV[7] = self.IV[6]
                self.IV[6] = self.clshift(self.IV[5],19)
                self.IV[5] = self.IV[4]
                self.IV[4] = self.P_0(TT2)
            for j in range(0,8):
                self.IV[j] = self.IV[j]^V[j]
        return ''.join(["0"*(10-len(hex(i)))+hex(i)[2:] for i in self.IV])
