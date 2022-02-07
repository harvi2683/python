
#AIM: You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
# harvi sheth 20ce136
#pyhton practical 3
import collections;

N = int(input())
d = collections.OrderedDict()

for i in range(N):
    word = input()
    if word in d:
        d[word] +=1
    else:
        d[word] = 1

print(len(d));

for k,v in d.items():
    print(v,end = " ");
