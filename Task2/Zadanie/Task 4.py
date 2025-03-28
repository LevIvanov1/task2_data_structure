def main(text):
    text_slova = text.split()
    dell_set_slova = set(text_slova)
    volume_store = {}
    for word in dell_set_slova:
        volume_store[word] = text_slova.count(word)
    return volume_store
input_string = input("ввод строки: ")
result = main(input_string)
for word, count in result.items():
    print(f"{word}: "
          f"{count}")