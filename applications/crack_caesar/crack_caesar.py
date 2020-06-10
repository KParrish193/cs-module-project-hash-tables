# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

import string

def ciphertext(text):
    freq = {c: 0 for c in string.ascii_uppercase}
    most_frequent = ["E", "T", "A", "O", "H", "N", "R", "I", "S", "D", "L",
                    "W", "U", "G", "F", "B", "M", "Y", "C", "P", "K", "V", "Q", "J", "X", "Z"]

    string_list = list(text)

    for char in string_list:

        if char in string.ascii_uppercase:
            freq[char] += 1

    # sort so we could map
    sorted_freq = {key: val for key, val in sorted(
        freq.items(), key=lambda item: item[1], reverse=True)}

    # replace values with most frequently used letters
    i = 0
    mapped_freq = {}
    for key in sorted_freq:
        mapped_freq[key] = most_frequent[i]
        i += 1

    for i in range(len(string_list)):
        if string_list[i] in string.ascii_uppercase:
            string_list[i] = mapped_freq[string_list[i]]

    return "".join(string_list)

# open ciphertext
with open("ciphertext.txt", "r") as f:
    file = f.read()


print(ciphertext(file))