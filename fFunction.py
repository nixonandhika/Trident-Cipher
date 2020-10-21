from helper import Helper as helper
from keyGenerator import KeyGenerator
import numpy as np

def fFunc(block, sKey, xKey):
    pBox = [16, 15, 13, 27, 21, 25, 14, 18, 2, 8, 7, 19, 3, 24, 28, 4, 10, 5, 12, 0, 6, 1, 29, 31]
    reducedBlock = []
    for idx in pBox:
        reducedBlock.append(block[idx])

    for i in range(8):
        reducedBlock[i*3+1] = sKey[i]
    
    for i in range(8, 16):
        reducedBlock.append(sKey[i])

    reducedBlock = ''.join(reducedBlock)
    xorResult = helper.xor(reducedBlock, xKey)
    
    
    if (xKey[0] == "1"):
        xorResult = helper.shiftLeft(xorResult, 1)
    
    return xorResult

if __name__ == "__main__":
    stringBlock = helper.convertStringToBinary64("abcdefgh")[0]
    left = stringBlock[:32]
    right = stringBlock[-32:]
    keyBlock = helper.convertStringToBinary64("qwertyui")[0]
    np.random.seed(helper.totalAsciiCode("qwertyui"))
    keygen = KeyGenerator(keyBlock, 1, 2)
    keygen.round()
    fFunc(right, keygen.subKey, keygen.crossKey)