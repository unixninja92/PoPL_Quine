# Charles Teese
# Principles of Programming Languages
# HW 1
# Language: Python

def quotes():
    s = ""
    for q in range(3):
        s += "'"
    return s

code = [
'''# Charles Teese''',
'''# Principles of Programming Languages''',
'''# HW 1''',
'''# Language: Python''',
'''''',
'''def quotes():''',
'''    s = ""''',
'''    for q in range(3):''',
'''        s += "'"''',
'''    return s''',
'''''',
'''code = [''',
''']''',
'''''',
'''for i in range(12):''',
'''    print(code[i])''',
'''''',
'''for j in range(len(code)-1):''',
'''    print("{0}{1}{2},".format(quotes(), code[j], quotes()))''',
'''print("{0}{1}{2}".format(quotes(), code[len(code)-1], quotes()))''',
'''''',
'''for k in range(12, len(code)):''',
'''    print(code[k])'''
]

for i in range(12):
    print(code[i])

for j in range(len(code)-1):
    print("{0}{1}{2},".format(quotes(), code[j], quotes()))
print("{0}{1}{2}".format(quotes(), code[len(code)-1], quotes()))

for k in range(12, len(code)):
    print(code[k])
