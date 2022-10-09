# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(s):
    encoding = ""
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1
    return encoding
 
text = 'AABBCCCD'
encoded_val = rle_encode(text)
print(encoded_val)

def rle_decode(data): 
    decode = '' 
    count = '' 
    for char in data: 
        if char.isdigit(): 
            count += char 
        else: 
            decode += char * int(count) 
            count = '' 
    return decode

decoded_val = rle_decode(encoded_val)
print(decoded_val)