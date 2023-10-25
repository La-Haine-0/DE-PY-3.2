# Задание 1
def square_properties(side_length):
    area = side_length ** 2
    perimeter = 4 * side_length
    print(f"Площадь квадрата: {area}")
    print(f"Периметр квадрата: {perimeter}")

# Задание 2
def sum_of_squares(num1, num2):
    squared = num1**2 + num2**2
    print(f"Сумма квадратов: {squared}")

# Задание 3
def reverse_list(input_list):
    new_list = input_list[::-1]
    print(f"Новый список: {new_list}")
    return new_list  # добавлен оператор return

# Задание 4
def count_genders(input_list, gender):
    if gender.lower() == 'male':
        count = input_list.count('male')
        print(f"Количество мужчин: {count}")
    elif gender.lower() == 'female':
        count = input_list.count('female')
        print(f"Количество женщин: {count}")
    else:
        print("Укажите 'male' или 'female' в качестве параметра")

# Задание 5
def count_characters(input_string):
    char_dict = {}
    for char in input_string:
        char_dict[char] = input_string.count(char)
    return char_dict

# Пример использования функций:
# Задание 1
square_properties(5)

# Задание 2
squared_result = sum_of_squares(3, 4)

# Задание 3
input_list = ["male", "male", "female", "male", "male", "female", "female"]
new_list = reverse_list(input_list)

# Задание 4
count_genders(new_list, 'male')

# Задание 5
input_string = "female"
character_count_dict = count_characters(input_string)
print(character_count_dict)
