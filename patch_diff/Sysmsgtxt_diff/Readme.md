#step1
original file (sjis):
sysmsg_jp.txt
sysmsg_cn.txt
sysmsg_patch.txt

#step2
seek from 0x41 and rm the last \x00, and then convert from sjis to utf8:
`iconv -f SHIFT_JIS-2004 -t utf-8 sysmsg_xx.txt >  sysmsg_xx_utf.txt`

sysmsg_jp_utf.txt
sysmsg_cn_utf.txt
sysmsg_patch_utf.txt


#step3
split utf file:
sysmsg_jp_utf_split.txt
sysmsg_cn_utf_split.txt
sysmsg_patch_utf_split.txt


#step4
manual merge patch diff into cn:
sysmsg_cn_utf_split_manual_merge.txt

#step5
join splited file:
sysmsg_cn_utf_join.txt

#ste6
`iconv -f utf-8 -t SHIFT_JIS-2004 sysmsg_cn_utf_join.txt >  sysmsg_cn_join.txt`
add header (0x8A0A) and a end \0x00



