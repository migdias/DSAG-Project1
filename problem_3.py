import sys
import heapq
import typing as t

class Node:
    def __init__(self, character: str, frequency: int):
        self.character: str = character
        self.frequency: int = frequency
        self._left: 'Node' = None
        self._right: 'Node' = None

    def __repr__(self) -> str:
        return f'Character: {self.character}, Frequency: {self.frequency}, Children: ({self._left},  {self._right})'
    
    def __lt__(self, other: 'Node'):
        return self.frequency < other.frequency

    
class PriorityQueue:
    def __init__(self, init_sentence = None):
        self.heap: t.List[Node] = []

        self._init_sentence_as_queue(init_sentence)

    def _init_sentence_as_queue(self, sentence):
        if sentence:
            d = {}
            for c in sentence:
                if c in d.keys():
                    d[c] += 1
                else:
                    d[c] = 1
            for character, frequency in d.items():
                node = Node(character, frequency)
                self.push(node)


    def push(self, node: Node) -> None:
        heapq.heappush(self.heap, (node.frequency, node))

    def pop(self) -> Node:
        if len(self.heap) > 0:
            return heapq.heappop(self.heap)[1]
        else:
            raise Exception('Priority Queue is empty.')
        
    def build_tree(self) -> Node:
        while len(self.heap) > 1:
            n1 = self.pop()
            n2 = self.pop()

            new_node = Node(None, n1.frequency + n2.frequency)
            if n1 < n2:
                new_node._left = n1
                new_node._right = n2
            else:
                new_node._left = n2
                new_node._right = n1

            self.push(new_node)

        tree = self.pop()
        return tree
        
    def __repr__(self):
        return f"PriorityQueue({self.heap})"


def huffman_encoding(sentence) -> t.Tuple[str, Node]:
    codes = {}
    pqueue = PriorityQueue(init_sentence=sentence)
    tree = pqueue.build_tree()

    def traverse(root: Node, code="", result={}):

        if root:
        
            traverse(root._left, code + "0", result)

            if root.character:
                #print(f'{root.character}: {code}')
                result[root.character] = code

            traverse(root._right, code + "1", result)

    if tree.character: # if root aready has chr
        codes[tree.character] = "0"
    else:
        traverse(tree, "", codes)

    encoded_str = ""
    for c in sentence:
        encoded_str += codes[c]

    return (encoded_str, tree)


def huffman_decoding(data:str , tree: Node) -> str:
    decoded_str = ""
    root = tree

    node = root

    for bit in data:
        if not node.character:
            if bit == "0":
                #print(f'Went left: {node._left.character} for bit {bit}')
                node = node._left
            elif bit == "1":
                #print(f'Went right: {node._right.character} for bit {bit}')
                node = node._right
            else:
                raise Exception('Not a 1 or a 0')
        
        # if reaches a leaf, set the character and reset the node
        if node.character:
            decoded_str += node.character
            node = root

    return decoded_str

if __name__ == "__main__":

    a_great_sentence = "The bird is the word"


    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    ## Add your own test cases: include at least three test cases
    ## and two of them must include edge cases, such as null, empty or very large values

    ## Test Case 1 - check one unique character over and over
    encoded_data, tree = huffman_encoding('AAAA') # Same character
    decoded_data = huffman_decoding(encoded_data, tree)
    print(f'Test1 -> Size encoded data: {sys.getsizeof(int(encoded_data, base=2))}, Size after decoding: {sys.getsizeof(decoded_data)}')
    assert sys.getsizeof(int(encoded_data, base=2)) < sys.getsizeof(decoded_data), 'Decoded is bigger than encoded'
    assert decoded_data == 'AAAA', 'Wrong decoding'

    ## Test Case 2 - check a huge text
    with open('resources/problem_3_big_text.txt') as f:
        txt = f.readlines()
        big_text = ''.join(txt)

    encoded_data, tree = huffman_encoding(big_text)
    decoded_data = huffman_decoding(encoded_data, tree)
    print(f'Test2 -> Size encoded data: {sys.getsizeof(int(encoded_data, base=2))}, Size after decoding: {sys.getsizeof(decoded_data)}')
    assert sys.getsizeof(int(encoded_data, base=2)) < sys.getsizeof(decoded_data), 'Decoded is bigger than encoded'
    assert decoded_data == big_text, 'Wrong decoding'
    
    ## Test Case 3 -- Check one character
    encoded_data, tree = huffman_encoding(',') # Same character
    decoded_data = huffman_decoding(encoded_data, tree)
    print(f'Test3 -> Size encoded data: {sys.getsizeof(int(encoded_data, base=2))}, Size after decoding: {sys.getsizeof(decoded_data)}')
    assert sys.getsizeof(int(encoded_data, base=2)) < sys.getsizeof(decoded_data), 'Decoded is bigger than encoded'
    assert decoded_data == ',', 'Wrong decoding'