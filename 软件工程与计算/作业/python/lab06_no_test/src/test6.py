s=0
for i in range(1,10):
    s=s+i
    if i % 5==0 :
        print(i*i)
        break
else:
    s=s+i
    print(i)
print(s)
