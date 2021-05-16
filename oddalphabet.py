oddalphabets={'a','c','e','g','i','k','m','o','q','s','u','w','y'}
allOddAlpha = True
str = 'A C E'
str = str.replace(' ', '').lower()
print(str)
for c in str:
    if c not in oddalphabets:
        allOddAlpha = False
        break;
 
if allOddAlpha:
    print ("All odd alphabets")
else:
    print ("Not all odd alphabets")
