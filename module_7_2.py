def custom_write(file_name, strings):
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as f:
        for i, string in enumerate(strings, start=1):
            pos = f.tell()
            f.write(string + '\n')
            strings_positions[(i, pos)] = string
    return strings_positions

info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
