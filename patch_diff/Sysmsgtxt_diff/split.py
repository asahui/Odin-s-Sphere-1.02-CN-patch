#!/usr/bin/python

SYSMSG_JP_UTF = "sysmsg_jp_utf.txt"
SYSMSG_CN_UTF = "sysmsg_cn_utf.txt"
SYSMSG_PATCH_UTF = "sysmsg_patch_utf.txt"

SYSMSG_JP_SPLIT_UTF = "sysmsg_jp_utf_split.txt"
SYSMSG_CN_SPLIT_UTF = "sysmsg_cn_utf_split.txt"
SYSMSG_PATCH_SPLIT_UTF = "sysmsg_patch_utf_split.txt"

SYSMSG_CN_JOIN_SPLIT = "sysmsg_cn_utf_join_split.txt"
SYSMSG_CN_JOIN = "sysmsg_cn_utf_join.txt"

# split jp and patch for manual diff, split cn for merging diff in it
files = [(SYSMSG_JP_UTF, SYSMSG_JP_SPLIT_UTF),
         (SYSMSG_CN_UTF, SYSMSG_CN_SPLIT_UTF),
         (SYSMSG_PATCH_UTF, SYSMSG_PATCH_SPLIT_UTF)]

# test join
files1 =  [(SYSMSG_CN_JOIN, SYSMSG_CN_JOIN_SPLIT)]


def split():
    for f in files1:
        with open(f[0]) as fin, open(f[1], "w") as fout:
            #fin.seek(0x40)
            content = fin.read()
            blocks = content.split('\x00')
            print '%-20s has %d blocks' % (f[0], len(blocks))
            for idx, b in enumerate(blocks):
                fout.write('#%d#\n' % idx)
                fout.write(b)
                fout.write('\n')
                fout.write('#'*10)
                fout.write('\n')

split()

