import json

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

def binary_search(data, name):
    comparisons = 0
    begin = 0
    end = len(data) - 1

    while begin <= end:
        mid = begin + (end - begin) // 2
        comparisons += 1

        if data[mid].name_getter() == name:
            print(f"Found {name} at index {mid}")
            print(f"ID: {data[mid].std_id_getter()}")
            print(f"Name: {data[mid].name_getter()}")
            print(f"GPA: {data[mid].gpa_getter()}")
            print(f"Comparisons times: {comparisons}")
            return

        elif data[mid].name_getter() < name:
            begin = mid + 1

        else:
            end = mid - 1

    print(f"{name} does not exists.")
    print(f"Comparisons times: {comparisons}")

if __name__ == "__main__":
    data_input = input()
    name_input = input()

    data = json.loads(data_input)
    data_list = [Student(item["id"], item["name"], item["gpa"]) for item in data]

    binary_search(data_list, name_input)
