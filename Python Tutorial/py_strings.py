# 1. String Creation & Concatenation
# Concatenation
s1 = "Hello"
s2 = "World"
print(s1 + " " + s2)  # Hello World

# Replication
print("ha" * 3)  # hahaha


# 2. Length & Indexing
text = "Python"

# Length
print(len(text))  # 6

# Indexing
print(text[0])  # P
print(text[-1]) # n

# Slicing
print(text[0:3])   # Pyt
print(text[::-1])  # nohtyP (reversing)
print(text[0:6:2]) # Pto (skipping)


# 3. Case Conversion
s = "hELLo WoRLD"
print(s.lower())   # hello world
print(s.upper())   # HELLO WORLD
print(s.capitalize())  # Hello world
print(s.title())       # Hello World
print(s.swapcase())    # HellO wOrld


# 4. Trimming / Stripping
s = "   ###Hello###   "

print(s.strip())       # ###Hello###
print(s.strip('#'))    # Hello
print(s.lstrip())      # "###Hello###   "
print(s.rstrip())      # "   ###Hello###"


## 5. Replace & Count
s = "banana banana"

print(s.replace("banana", "apple"))  # apple apple
print(s.count("a"))  # 6
print(s.count("na", 0, 6))  # 2 (within range)


## 6. Search & Find
s = "hello world"

print(s.find("world"))  # 6
print(s.rfind("l"))     # 9 (last occurrence)
print(s.startswith("he"))  # True
print(s.endswith("ld"))    # True


## 7. Character Type Checks
s1 = "Python3"
s2 = "12345"

print(s1.isalpha())   # False
print("Python".isalpha())  # True
print(s2.isdigit())   # True
print("hello".islower())   # True
print("WORLD".isupper())   # True
print(" ".isspace())       # True


## 8. Text Alignment
s = "hello"

print(s.center(10, '-'))  # --hello---
print(s.ljust(10, '*'))   # hello*****
print(s.rjust(10, '+'))   # +++++hello


## 9. Extra Examples
text = "  hello world! this is an example string.  "

# Title + Swapcase + Find
mod = text.strip().title().swapcase()
print(mod.find("Example"))  # 29


##  10. Splitting & Joining (used a LOT in NLP / Web scraping)
s = "apple,banana,grape"

print(s.split(","))   # ['apple', 'banana', 'grape']
print(s.rsplit(",", 1)) # ['apple,banana', 'grape']

words = ["Python", "is", "fun"]
print(" ".join(words))  # "Python is fun"

name = "Alice"
age = 22

## 11. String formating
print("My name is {} and I am {} years old".format(name, age))
print(f"My name is {name} and I am {age} years old")  # modern way

## 12. Counting and frequency 
s = "leetcode"

# Count occurrences of a char
count_e = s.count('e')

# or Frequency map using Counter (from collections)
from collections import Counter
freq = Counter(s)  # {'l':1, 'e':3, 't':1, 'c':1, 'o':1, 'd':1}

# Access frequency of 'e'
freq_e = freq['e']

# Useful String Algorithms & Techniques
# Two Pointers: For palindrome check, substring search, or merging sorted strings.
# Sliding Window: For longest substring without repeating characters, anagram finding.
# Hashing: Use frequency/count maps to detect duplicates, anagrams, or subpatterns.
# Prefix/Suffix Arrays: Preprocessing for range queries or substring checks.
# KMP (Knuth–Morris–Pratt): Efficient substring search algorithm (advanced).
# Trie Data Structure: Fast prefix-based string queries.