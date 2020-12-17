from magic_list import MagicList
from dataclasses import dataclass

@dataclass
class Person:
    age: int = 1


def main():
    first_instance = MagicList()
    # Works with wanted usage
    first_instance[0] = 5
    first_instance[1] = 10
    print(first_instance)
    # Won't work without continuity
    try:
        first_instance[5] = 6
    except IndexError:
        print("Please maintain index continuity.")

    second_instance = MagicList(cls_type=Person)

    second_instance[0] = 5
    print(second_instance[0])

    second_instance[1].age = 7
    print(second_instance[1])

if __name__ == "__main__":
    main()