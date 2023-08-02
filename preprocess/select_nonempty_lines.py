import sys

working_folder = sys.argv[1]
file_type = sys.argv[2]
languages = sys.argv[3]

null_lines = []

for lang in languages.split(','):
    ctr = 0
    file = open(working_folder + file_type + '.' + lang, 'r')
    lines = file.readlines()
    for i in lines:
        if i.strip() == '':
            null_lines.append(ctr)
        ctr += 1

for lang in languages.split(','):
    with open(working_folder + file_type + '.' + lang + '.notnull', 'w') as f_out:
        ctr = 0
        file = open(working_folder + file_type + '.' + lang, 'r')
        lines = file.readlines()
        for line in lines:
            if ctr not in null_lines:
                f_out.write(line.strip() + '\n')
            ctr += 1
