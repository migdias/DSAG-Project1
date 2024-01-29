import hashlib
from datetime import datetime, timezone

class Block:

    def __init__(self, data: str, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.timestamp: datetime = datetime.now(timezone.utc)
        self.hash = self.calc_hash()
        self._prev = None

    def calc_hash(self):
        sha = hashlib.sha256()

        st = self.timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%Z") + self.data + self.previous_hash
        hash_str = st.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()
    
    def __repr__(self) -> str:
        return f'Hash: {self.hash}, Timestamp: {self.timestamp.strftime("%Y-%m-%dT%H:%M:%S.%f%Z"),}, Data: {self.data}'
    
class BlockChain:
    
    def __init__(self):
        self.head = None
        self.size = 0
        

    def add(self, data):
        if data:
            if not self.head:
                self.head = Block(data, previous_hash="0")
            else:
                new_block =  Block(data, previous_hash=self.head.hash)
                new_block._prev = self.head
                self.head = new_block

            self.size += 1
        return 

    def print_chain(self):
        current_block = self.head
        while current_block:
            print(f"Timestamp: {current_block.timestamp}")
            print(f"Data: {current_block.data}")
            print(f"Previous Hash: {current_block.previous_hash}")
            print(f"Hash: {current_block.hash}")
            print("\n")
            current_block = current_block._prev


if __name__ == '__main__':

    bc = BlockChain()

    bc.add('My Data 1')

    # Test 1 -- check head data should be the same and previous hash = "0"
    assert bc.head.data == 'My Data 1', 'Wrong data'
    assert bc.head.previous_hash == "0", "Wrong hash"

    # Test 2
    bc.add('Another Data')
    bc.add('And yet another data')
    assert bc.size == 3, 'Wrong size'
    assert bc.head._prev._prev.previous_hash == "0", "Going two times back and checking prev hash should be 0"
    assert bc.head.previous_hash == bc.head._prev.hash, 'Prev Curr Hash and previous hash should be the same'

    # Test 3 adding no data should not do anything
    bc.add(None)
    assert bc.size == 3, 'Wrong size'
    assert bc.head.data == 'And yet another data', 'Wrong data'


    # Test 4 - Checking the chain as print
    bc.print_chain()
