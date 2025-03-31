import re 

pattern = '^a[A-Za-z,]{2,3}s$'
txt = 'ar,ts'

found = re.match(pattern, txt)

if found:
    print("Found")
else:
    print("Not found")