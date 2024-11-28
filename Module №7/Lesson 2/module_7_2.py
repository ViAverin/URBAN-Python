def custom_write(file_name, strings):
    strings_positions = {}
    f = open(file_name, 'w', encoding='utf-8')  # Открываем файл
    try:
        for index, string in enumerate(strings):
            byte_position = f.tell()  # Получаем текущую позицию в байтах
            strings_positions[(index + 1, byte_position)] = string  # Обновляем словарь
            f.write(string + '\n')  # Записываем строку с переводом строки
    finally:
        f.close()  # Закрываем файл
    return strings_positions


def main():
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]


    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)


if __name__ == '__main__':
    main()
