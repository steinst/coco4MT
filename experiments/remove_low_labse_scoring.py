import sys

infile = sys.argv[1]
outfile = sys.argv[2]
cutoff = 0.5

with open(infile, 'r') as fi, open(outfile, 'w') as fo:
    for line in fi:
        current = line.strip().split('\t')
        try:
            if float(current[2]) > cutoff:
                fo.write(line.strip() + '\n')
        except:
            pass
