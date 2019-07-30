s=input()
s1=""
s2=""
for i in s:
  n=s.count(i)
  if i in s2:
    continue
  else:
    s2+=i
    s1+=i+str(n)
print(s1)

input:
  aaabbbcc
output:
  a3b3c2
