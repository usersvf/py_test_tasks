def find_in_different_registers(words: list):
    unique_words = set(words)
    unique_words_lower_case = set(word.lower() for word in words)

    [unique_words_lower_case.remove(word.lower()) for word in unique_words if words.count(word) > 1]

    non_duplicates = sorted(list(unique_words_lower_case))

    return print(non_duplicates)

#tests
words = ['Мама', 'МАМА', 'Мама', 'папа', 'ПАПА', 'Мама', 'ДЯдя', 'брАт', 'Дядя', 'Дядя', 'Дядя']
find_in_different_registers(words)

words = ['Typology', 'anglican', 'Ten-ruble', 'Bacteriologist', 'Ill-fated', 'Disposition', 'BRAce', 'Legend', 'Diploma', 'Diploma', 'BRAce', 'Mercantilist']
find_in_different_registers(words)

words = ['Мама', 'МАМА', 'МаМа', 'папа', 'ПАПА', 'МамА', 'ДЯдя', 'брАт', 'Дядя', 'ДЯДя', 'дядя']
find_in_different_registers(words)