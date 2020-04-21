def nyinyir_translate(phrase):
    result = ''
    for letter in phrase:
        if letter.lower() in 'aiueo':
            if letter.isupper():
                result = result + 'I'
            else:
                result = result + 'i'
        else:
            result = result + letter
    return result

prompt = input('Masukkan kalimat anda: ')
print(nyinyir_translate((prompt)))

