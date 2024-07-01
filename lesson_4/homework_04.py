import re
import string
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")


# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = re.sub(r'\s+', ' ', adwentures_of_tom_sawer).strip()


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.count('h')


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = adwentures_of_tom_sawer.split()
count_upper_words = sum(1 for word in words if word[0] in string.ascii_uppercase)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
second_tom_position = adwentures_of_tom_sawer.find('Tom', adwentures_of_tom_sawer.find('Tom') + 1)


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = re.split(r'[.?!]', adwentures_of_tom_sawer)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3].strip().lower()


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
starts_with_by_the_time = any(sentence.strip().startswith('By the time') for sentence in adwentures_of_tom_sawer_sentences)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence_words = adwentures_of_tom_sawer_sentences[-1].strip().split()
num_words_last_sentence = len(last_sentence_words)

print("Task 01 Result:")
print(adwentures_of_tom_sawer)
print("\nTask 02 Result:")
print(adwentures_of_tom_sawer)
print("\nTask 03 Result:")
print(adwentures_of_tom_sawer)
print("\nTask 04 Result:")
print(count_h)
print("\nTask 05 Result:")
print(count_upper_words)
print("\nTask 06 Result:")
print(second_tom_position)
print("\nTask 08 Result:")
print(fourth_sentence)
print("\nTask 09 Result:")
print(starts_with_by_the_time)
print("\nTask 10 Result:")
print(num_words_last_sentence)