# characters frequency
# get the frequency of each character

word    = "Hello World"
result  = {}
for char in word:
    count = result.get(char, 0)
    count += 1
    result[char] = count

print(result);
# print(sorted(result.values()));
# for char in result:
#     print(char);
#     print(result[char]);

