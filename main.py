import hashlib
import json
import itertools

blockchain = []
def generateBlock(previousHash,data):
        dic = {'data':data,'previousHash':previousHash}
        dic_package = json.dumps(dic).encode()
        Hash = hashlib.sha256(dic_package).hexdigest()
        block = {'Hash':Hash,'data':data,'previousHash':previousHash}
        return block

genesisBlock = generateBlock(0,'GENESIS')
blockchain.append(genesisBlock)
secondBlock = generateBlock(genesisBlock.get('Hash'),'TEST') 
blockchain.append(secondBlock)

for i in itertools.count():
    data = "qwretyuikgfdvbn347487584378fjdsufidufieuriewriew"
    thirdBlock = generateBlock(secondBlock.get('Hash'),data)
    blockchain.append(thirdBlock)
    print(blockchain)

