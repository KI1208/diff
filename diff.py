import difflib
import re

fb = open('before.csv')
fblines = fb.readlines()
fb.close()

fa = open('after.csv')
falines = fa.readlines()
fa.close()

d = difflib.Differ()
diff = d.compare(fblines, falines)

f = open('result_difflib_sample.txt','w')

for line in diff:
    # checkmatch = re.search('xdw$', line)
    checkmatch = re.search('^[\+|\-] ', line)
    if checkmatch is not None:
        # print(checkmatch.group(0))
        print(line)
        # f.writelines(line.split(',')[3])
        f.writelines(line)

f.close()
