import re
text ="Nan #lavi a fok ou kanpe #djanm pou ou ka reyisi"
pattern=r'\#(.*?)\ '
result=re.sub(pattern, r'<a href= #\1<\\<a>' , text)
print(result)