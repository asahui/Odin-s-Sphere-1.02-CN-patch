#!/usr/bin/python

SYSMSG_CN_UTF_SPLIT_MANUAL_MERGE = "sysmsg_cn_utf_split_manual_merge.txt"
SYSMSG_CN_UTF_JOIN = "sysmsg_cn_utf_join.txt"

files = [
         (SYSMSG_CN_UTF_SPLIT_MANUAL_MERGE, SYSMSG_CN_UTF_JOIN)
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
