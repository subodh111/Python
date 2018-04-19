print("----------------------------------------")
print ("Counting number of tokens from the file.")
print("----------------------------------------")
print("digits    = [1,2,3,4,5,6,7,8,9,0] ")
print("keyword   = [ for , in] ")
print("operator  = [ = , +- , + , %] ")
print("function  = [input,print,len,ord,range]")
print("variables = [string,i,hash,sum]")
print("----------------------------------------")
operator=["=","+=","+","%"]
keyword =["for","in"]
digits= ["1","2","3","4","5","6","7","8","9","0"]
function=["input","print","len","ord","range"]
variables=["string","i","hash","sum"]
text_file= open('hash.txt','r')
Lxlist=[]
for line in text_file:
    for word in line.split():
        Lxlist.append(word)    
text_file.close()
k,o,d,f,v=0,0,0,0,0
for j in Lxlist:
    for di in digits:
         if di==j:
            d=d+1
    for ke in keyword:
        if ke==j:
           k=k+1
    for op in operator:
        if op==j:
           o=o+1
    for va in variables:
        if va==j:
           v=v+1
    for fu in function:      
        if fu==j:
           f=f+1               
print("Number of digits    = ",d)
print("Number of keyword   = ",k)
print("Number of operator  = ",o)
print("Number of function  = ",f)
print("Number of variables = ",v)
print("----------------------------------------")
