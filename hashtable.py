class HashTable:

    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_bucket()


    def create_bucket(self):
        return [[] for _ in range(self.size)]


    def set_val(self, key, value):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))


    def get_val(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_value = record
            if record_key == key:
                found_key = True
                break
        if found_key:
            return record_value
        else:
            return "No record found with that key"

    def __str__(self):
        return "".join(str(item) for item in self.hash_table)

hash_table = HashTable(256)
hash_table.set_val('daniel7711potter', 'hello')
print(hash_table)
