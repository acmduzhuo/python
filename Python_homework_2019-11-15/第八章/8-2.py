import os
import re


def deteciframe(fn):
    content = []
    with open(fn, encoding='utf-8')as fp:
        for line in fp:
            content.append(line.strip())
    content = ''.join(content)
    m = re.findall(r'<iframe\s+src=.*?></iframe>', content)
    if m:
        return {fn: m}
    return False


for fn in (f for f in os.listdir('.') if f.endswith(('.html', '.htm'))):
    r = detectiframe(fn)
    if not r:
        continue
    for k, v in r.items():
        print(k)
        for vv in v:
            print('\t', vv)
