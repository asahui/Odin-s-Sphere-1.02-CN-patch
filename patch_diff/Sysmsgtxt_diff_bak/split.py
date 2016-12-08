#!/usr/bin/python

SYSMSG_JP_UTF = "sysmsg_jp2.txt"
SYSMSG_CN_UTF = "sysmsg_cn2.txt"
SYSMSG_PATCH_UTF = "sysmsg_patch2.txt"

SYSMSG_JP_SPLIT_UTF = "sysmsg_jp2_split1.txt"
SYSMSG_CN_SPLIT_UTF = "sysmsg_cn2_split1.txt"
SYSMSG_PATCH_SPLIT_UTF = "sysmsg_patch2_split1.txt"

SYSMSG_CN_MERGE = "sysmsg_cn_merge.txt"
SYSMSG_CN_SPLIT = "sysmsg_cn_split.txt"

files = [(SYSMSG_JP_UTF, SYSMSG_JP_SPLIT_UTF),
         (SYSMSG_CN_UTF, SYSMSG_CN_SPLIT_UTF),
         (SYSMSG_PATCH_UTF, SYSMSG_PATCH_SPLIT_UTF)]
files1 =  [(SYSMSG_CN_MERGE, SYSMSG_CN_SPLIT)]


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

