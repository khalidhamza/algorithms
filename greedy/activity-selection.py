# Activity Selection Algorithm

start   = [9, 10, 11, 12, 13, 15]
end     = [11, 11, 12, 14, 15, 16]

result  = [0];
i = 1;
j = 0;
while i < len(start):
    if start[i] >= end[j]:
        result.append(i)
        j=i
    i+=1

print(result)