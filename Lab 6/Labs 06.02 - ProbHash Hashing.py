class Student:
    def __init__(self, std_id, name, gpa):
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa

    def std_id_getter(self):
        return self.__std_id
    
    def name_getter(self):
        return self.__name

    def gpa_getter(self):
        return self.__gpa

    def print_details(self):
        print(f"ID: {self.__std_id}")
        print(f"Name: {self.__name}")
        print(f"GPA: {self.__gpa:.2f}")

class ProbHash:
    def __init__(self, size):
        self.__hash_table = [None] * size
        self.__size = size

    def hash_key(self, key):
        return key % self.__size

    def rehash(self, hash_key):
        original_key = hash_key
        while self.__hash_table[hash_key] is not None:
            hash_key = (hash_key + 1) % self.__size
            if hash_key == original_key:
                return None
        return hash_key

    def insert_data(self, student):
        if self.__hash_table.count(None) == 0:
            print(f"The list is full. {student.std_id_getter()} could not be inserted.")
            return

        hash_key = self.hash_key(student.std_id_getter())

        if self.__hash_table[hash_key] is None:
            self.__hash_table[hash_key] = student
            print(f"Insert {student.std_id_getter()} at index {hash_key}")
        else:
            rehash_key = self.rehash(hash_key)
            if rehash_key is not None:
                self.__hash_table[rehash_key] = student
                print(f"Insert {student.std_id_getter()} at index {rehash_key}")
            else:
                print(f"Could not insert {student.std_id_getter()}, table is full.")

    def search_data(self, std_id):
        for index, student in enumerate(self.__hash_table):
            if student is not None and student.std_id_getter() == std_id:
                print(f"Found {std_id} at index {index}")
                return student
        print(f"{std_id} does not exist.")
        return None

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()