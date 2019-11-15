import re
x = 'This is a a desk.'
pattern = re.compile(r'\b(\w+)(\s+\1){1,}\b')
matchResult = pattern.search(x)
x = pattern.sub(matchResult.group(1),x)
print(x)