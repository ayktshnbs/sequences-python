pangram = "The quick brown fox jumps over the lazy dog"
letters = sorted(pangram)
print(letters)

numbers = [1.6, 8.3, 4.7, 9.5, 2.6]
sorted_numbers = sorted(numbers)
print(numbers)
print(sorted_numbers)

numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog", key=str.casefold)
print(missing_letter)

names = ["Graham",
         "John",
         "Terry",
         "eric",
         "Terry",
         "michael"
         ]
names.sort(key=str.casefold)
print(names)