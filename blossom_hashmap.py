# 0.0) Import linked lists and node to be able to make use of linked lists:
from linked_list import Node, LinkedList

# 0.1) Import flower definitions:
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(size)]
#Step1: This method produces a hashcode to be used in the hash map:
  
  def hash(self, key):
    return sum(key.encode())

#Step2: This method compresses the hash code produced by .hash() so that it will fit into the range of the array.

  def compress(self, hash_code):
    return hash_code % self.array_size

#Step3: Assign method
  
  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    payload = Node([key,value])
    list_at_array = self.array[array_index]
    for i in list_at_array:
      if i[0] == key:
        i[1] = value
        return
    list_at_array.insert(payload)
         
    

#Step4: Retrieval method

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]

    for i in list_at_index:
      if i[0] == key:
        return i[1]
    return None
blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])
print(blossom.retrieve('daisy'))
