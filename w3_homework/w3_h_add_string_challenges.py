# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])
print("------------------")

# Вывести количество букв "а" в слове
word = 'Архангельск'
letters = ','.join(word.lower())
print(letters.count('а'))
print("------------------")

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
count = 0
for letter in word.lower():
    for vowel in vowels:
        if vowel == letter:
            count += 1
print(count)
print("------------------")

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'

words_only = sentence.split()
print(len(words_only))
print("------------------")

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words_only = sentence.split()
for word in words_only:
    print(word[0])
print("------------------")

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
summ = 0
avg = 0.0
words_only = sentence.split()
for word_len in words_only:
    summ += int(len(word_len))
avg = round(summ / len(words_only), 2)
print(avg)
print("------------------")
