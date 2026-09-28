#count vowels
word="artificial"
count=0
for ch in word:
    if(ch=='a' or ch=='e' or ch=='o' or ch=='u' or ch=='i'):
        count+=1
print(count)