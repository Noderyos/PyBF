a,b,c,d,e=[0]*30000,[],0,0,input("Input BF Code: ")
while d < len(e):
 if e[d]==">":c+=1
 if e[d]=="<":c-=1
 if e[d]=="+":a[c]+=1
 if e[d]=="-":a[c]-=1
 if e[d]==".":print(chr(a[c]),end="")
 if e[d]==",":a[c]=ord(input("")[0])
 if e[d]=="[":b.append(d)
 if e[d]=="]"and a[c]!= 0:d=b.pop()-1
 d+=1
