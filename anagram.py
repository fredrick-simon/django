def ana(s1,s2):
    s1=sorted(s1)
    s2=sorted(s2)
    if s1==s2:
        print(True)
    else:
        print(False)
s1=list(input().strip())
s2=list(input().strip())

ana(s1,s2)

