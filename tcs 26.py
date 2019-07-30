s1=input()
s2=input()
s3=input()
u=s3.upper()
v="aeiou"
str1=""
for i in s1:
    if i in v:
        str1+="%"
    else:
        str1+=i
for i in s2:
    if i in v:
        str1+=i
    else:
        str1+="#"
print(str1+u)

 input:
 enter
the
dragon

str1 -> 'enter' - replacing vowels with % --> %nt%r

str2 -> 'the' - replacing consonants with # --> ##e

str3 -> 'dragon' - convert to upper case --> DRAGON

Concatenating the resultant strings - ""%nt%r##eDRAGON"

Sample Input 1

avengers
infinity
war
        
