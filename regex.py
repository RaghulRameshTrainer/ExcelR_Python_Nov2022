import re

"""
match
search
findall
sub
split
compite-finditer

"""

line="pet:cat i love cat pet:dog i love dog"

#matches=re.match('pet:cat',line)
#matches=re.match('pet:dog',line)
#matches=re.match('pet:...',line)
#matches=re.match('pet:.{3}',line)
#matches=re.match('PET:.{3}',line,re.I)
#print(matches.group())

#matches=re.search('pet:dog',line)
#matches=re.search('pet:cat',line)
#matches=re.search('pet:...',line)
#print(matches.group())

#matches=re.findall("pet:cat",line)
matches=re.findall("pet:...",line)
print(matches)