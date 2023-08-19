# Activity Selection Algorithm
# start and end refer to the start time and end time for a lecture.
# We have to get all lectures which we can attend
# the logic is to select the lecture if the end time is less than or equal to the start time of the next lecture

start   = [9, 10, 11, 12, 13, 15]
end     = [11, 11, 12, 14, 15, 16]

result  = [0]
i = 1;
j = 0;
while i < len(start):
    if start[i] >= end[j]:
        result.append(i)
        j=i
    i+=1

print(result)