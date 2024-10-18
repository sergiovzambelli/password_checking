import math
import mmh3
from bitarray import bitarray
import os
from decimal import Decimal, getcontext
import time

'''
Initialize a BloomFilter with the following parameters:
- `storage`: The estimated maximum number of elements the filter is expected to store.
- `error_rate`: The desired maximum false positive rate (the probability of a false positive result).

The Bloom filter uses a bit array, a highly memory-efficient structure, to store elements and ensure optimal space usage while maintaining the specified error rate.
'''

class BloomFilter:

    def __init__(self, storage, error_rate):
        self.storage = storage
        self.error_rate = error_rate
        self.bits = self.get_bits(storage, error_rate)
        self.hashes = self.get_hashes(self.bits, storage)
        self.bit_array = bitarray(self.bits)
        
    # Derivative hash functions
    def add(self, element):
        h1 = mmh3.hash(element, 0)
        h2 = mmh3.hash(element, 1)
        
        for i in range(self.hashes):
            hash_val = (h1 + i * h2) % self.bits
            self.bit_array[hash_val] = 1
      
    # Overridden the __contains__ method to support lookup using in operator
    def __contains__(self, element):
        h1 = mmh3.hash(element, 0)
        h2 = mmh3.hash(element, 1)
        
        for i in range(self.hashes):
            hash_val = (h1 + i * h2) % self.bits
            if self.bit_array[hash_val] == 0:
                return False
        return True
    
    # Decimal help the accuracy of division and logarithm operations
    def get_bits(self, storage, error_rate):
        getcontext().prec = 10
        bits = Decimal(-storage) * Decimal(math.log(error_rate)) / (Decimal(math.log(2)) ** 2)
        return int(bits)
    
    def get_hashes(self, bits, storage):
        getcontext().prec = 10
        hashes = (Decimal(bits) / Decimal(storage)) * Decimal(math.log(2))
        return int(hashes)


dict_directory = "dict"

print("Reading dictionary files...")
start_time_total = time.time()

max_bloom_size = 0
max_error_rate = 0.01

start_time_read = time.time()

for filename in os.listdir("dict"):
    file_path = os.path.join(dict_directory, filename)
    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r') as f:
                max_bloom_size += sum(1 for line in f)
        except Exception as e:
            print("Error reading file: ", file_path, e)
            
end_time_read = time.time()
print(f"Time taken to read files and count lines: {end_time_read - start_time_read:.2f} seconds")
print()

print("Max Bloom Size: ", max_bloom_size)
print("Error rate: ", max_error_rate)

bloom_filter = BloomFilter(max_bloom_size, max_error_rate)

start_time_populate = time.time()

for filename in os.listdir(dict_directory):
    file_path = os.path.join(dict_directory, filename)
    if os.path.isfile(file_path):
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    bloom_filter.add(line.strip())
        except Exception as e:
            print("Error reading file: ", file_path)
            
end_time_populate = time.time()
print(f"Time taken to populate Bloom filter: {end_time_populate - start_time_populate:.2f} seconds")
print()
            
print("Bloom Filter ready!")
print(f"Total time taken: {end_time_populate - start_time_total:.2f} seconds")
print("Enter 'q' to quit.")
print()

password = input('Enter a possible password: ')
while password != "q":
    print("The password is weak? ", (password in bloom_filter))
    print()
    password = input('Enter a word: ')
    