#!/usr/bin/python

SYSMSG_CN_UTF = "sysmsg_cn_merge.txt"

SYSMSG_CN_SPLIT_UTF = "sysmsg_cn2_split1_merge.txt"

files = [
         (SYSMSG_CN_SPLIT_UTF, SYSMSG_CN_UTF)
         ]

def merge():
    for f in files:
        content = []
        with open(f[0]) as fin, open(f[1], 'w') as fout:
            content = fin.read()
            blocks = content.split('#'*10 + '\n')[:-1] #trim the last empty block
            
            # for each block, split into lines, trim the first line and last empty block
            blocks = [('\n'.join(b.split('\n')[1:-1])) for b in blocks]
            content = '\x00'.join(blocks)
            fout.write(content)

merge()
