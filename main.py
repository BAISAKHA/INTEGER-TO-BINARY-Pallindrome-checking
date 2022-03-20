n=int(input())
b=""
end=""
pallindrome=""
while (n>1 or n>0):
  a=n%2
  n=n//2
  b+=str(a)
for i in range(len(b)-1,-1,-1):
  end+=b[i]
print(end)

for i in range(len(end)-1,-1,-1):
  pallindrome+=end[i]

if (pallindrome==end):
  print("pallindrome")


  
  
  