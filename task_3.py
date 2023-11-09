# TODO  Напишите функцию count_letters


# TODO Напишите функцию calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

def count_letters(text_):
    low_letter= text_.lower()
    number_of_letters = {}
    for letter in low_letter:
        if letter.isalpha():
            if letter in number_of_letters:
                number_of_letters[letter] = number_of_letters[letter] + 1
            else:
                number_of_letters[letter] = 1
    return number_of_letters



def calculate_frequency(number_of_letters):
    frequency_value = {}
    sum_letters = sum(number_of_letters.values())
    for letter, count in number_of_letters.items():
        frequency = count / sum_letters
        frequency_value[letter] = round(frequency, 2)
    return frequency_value




dict_ = count_letters(main_str)
dict_frequency = calculate_frequency(dict_)

for letter, frequency in dict_frequency.items():
    print(f"{letter}: {frequency:.2f}")

# TODO Распечатайте в столбик букву и её частоту в тексте
