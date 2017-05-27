#!/usr/bin/env python
# -*- coding: utf-8 -*

import zipfile
import os
import sys
import locale

#try:
#    import chardet
#except:
#    chardet=None


ALL_CODEC_CANDIDATE = [
    ("ascii",["646","us-ascii",],["English",] ),
    ("big5",["big5-tw","csbig5",],["Traditional Chinese",] ),
    ("big5hkscs",["big5-hkscs","hkscs",],["Traditional Chinese",] ),
    ("cp037",["IBM037","IBM039",],["English",] ),
    ("cp424",["EBCDIC-CP-HE","IBM424",],["Hebrew",] ),
    ("cp437",["437","IBM437",],["English",] ),
    ("cp500",["EBCDIC-CP-BE","EBCDIC-CP-CH","IBM500",],["Western Europe",] ),
    ("cp737",[],["Greek",] ),
    ("cp775",["IBM775",],["Baltic languages",] ),
    ("cp850",["850","IBM850",],["Western Europe",] ),
    ("cp852",["852","IBM852",],["Central and Eastern Europe",] ),
    ("cp855",["855","IBM855",],["Bulgarian","Byelorussian","Macedonian","Russian","Serbian",] ),
    ("cp856",[],["Hebrew",] ),
    ("cp857",["857","IBM857",],["Turkish",] ),
    ("cp860",["860","IBM860",],["Portuguese",] ),
    ("cp861",["861","CP-IS","IBM861",],["Icelandic",] ),
    ("cp862",["862","IBM862",],["Hebrew",] ),
    ("cp863",["863","IBM863",],["Canadian",] ),
    ("cp864",["IBM864",],["Arabic",] ),
    ("cp865",["865","IBM865",],["Danish","Norwegian",] ),
    ("cp866",["866","IBM866",],["Russian",] ),
    ("cp869",["869","CP-GR","IBM869",],["Greek",] ),
    ("cp874",[],["Thai",] ),
    ("cp875",[],["Greek",] ),
    ("cp932",["932","ms932","mskanji","ms-kanji",],["Japanese",] ),
    ("cp949",["949","ms949","uhc",],["Korean",] ),
    ("cp950",["950","ms950",],["Traditional Chinese",] ),
    ("cp1006",[],["Urdu",] ),
    ("cp1026",["ibm1026",],["Turkish",] ),
    ("cp1140",["ibm1140",],["Western Europe",] ),
    ("cp1250",["windows-1250",],["Central and Eastern Europe",] ),
    ("cp1251",["windows-1251",],["Bulgarian","Byelorussian","Macedonian","Russian","Serbian",] ),
    ("cp1252",["windows-1252",],["Western Europe",] ),
    ("cp1253",["windows-1253",],["Greek",] ),
    ("cp1254",["windows-1254",],["Turkish",] ),
    ("cp1255",["windows-1255",],["Hebrew",] ),
    ("cp1256",["windows1256",],["Arabic",] ),
    ("cp1257",["windows-1257",],["Baltic languages",] ),
    ("cp1258",["windows-1258",],["Vietnamese",] ),
    ("euc_jp",["eucjp","ujis","u-jis",],["Japanese",] ),
    ("euc_jis_2004",["jisx0213","eucjis2004",],["Japanese",] ),
    ("euc_jisx0213",["eucjisx0213",],["Japanese",] ),
    ("euc_kr",["euckr","korean","ksc5601","ks_c-5601","ks_c-5601-1987","ksx1001","ks_x-1001",],["Korean",] ),
    ("gb2312",["chinese","csiso58gb231280","euc-cn","euccn","eucgb2312-cn","gb2312-1980","gb2312-80"],["iso-ir-58 Simplified Chinese",] ),
    ("gbk",["936","cp936","ms936",],["Unified Chinese",] ),
    ("gb18030",["gb18030-2000",],["Unified Chinese",] ),
    ("hz",["hzgb","hz-gb","hz-gb-2312",],["Simplified Chinese",] ),
    ("iso2022_jp",["csiso2022jp","iso2022jp","iso-2022-jp",],["Japanese",] ),
    ("iso2022_jp_1",["iso2022jp-1","iso-2022-jp-1",],["Japanese",] ),
    ("iso2022_jp_2",["iso2022jp-2","iso-2022-jp-2",],["Japanese","Korean","Simplified Chinese","Western Europe","Greek",] ),
    ("iso2022_jp_2004 iso2022jp-2004","iso-2022-jp-2004",["Japanese",] ),
    ("iso2022_jp_3",["iso2022jp-3","iso-2022-jp-3",],["Japanese",] ),
    ("iso2022_jp_ext",["iso2022jp-ext","iso-2022-jp-ext",],["Japanese",] ),
    ("iso2022_kr",["csiso2022kr","iso2022kr","iso-2022-kr",],["Korean",] ),
    ("latin_1",["iso-8859-1","iso8859-1","8859","cp819","latin","latin1","L1",],["West Europe",] ),
    ("iso8859_2",["iso-8859-2","latin2","L2",],["Central and Eastern Europe",] ),
    ("iso8859_3",["iso-8859-3","latin3","L3",],["Esperanto","Maltese",] ),
    ("iso8859_4",["iso-8859-4","latin4","L4",],["Baltic languagues",] ),
    ("iso8859_5",["iso-8859-5","cyrillic",],["Bulgarian","Byelorussian","Macedonian","Russian","Serbian",] ),
    ("iso8859_6",["iso-8859-6","arabic",],["Arabic",] ),
    ("iso8859_7",["iso-8859-7","greek","greek8",],["Greek",] ),
    ("iso8859_8",["iso-8859-8","hebrew",],["Hebrew",] ),
    ("iso8859_9",["iso-8859-9","latin5","L5",],["Turkish",] ),
    ("iso8859_10",["iso-8859-10","latin6","L6",],["Nordic languages",] ),
    ("iso8859_13",["iso-8859-13",],["Baltic languages",] ),
    ("iso8859_14",["iso-8859-14","latin8","L8",],["Celtic languages",] ),
    ("iso8859_15",["iso-8859-15",],["Western Europe",] ),
    ("johab",["cp1361","ms1361",],["Korean",] ),
    ("koi8_r",[],["Russian",] ),
    ("koi8_u",[],["Ukrainian",] ),
    ("mac_cyrillic",["maccyrillic",],["Bulgarian","Byelorussian","Macedonian","Russian","Serbian",] ),
    ("mac_greek",["macgreek",],["Greek",] ),
    ("mac_iceland",["maciceland",],["Icelandic",] ),
    ("mac_latin2",["maclatin2","maccentraleurope",],["Central and Eastern Europe",] ),
    ("mac_roman",["macroman",],["Western Europe",] ),
    ("mac_turkish",["macturkish",],["Turkish",] ),
    ("ptcp154",["csptcp154","pt154","cp154","cyrillic-asian",],["Kazakh",] ),
    ("shift_jis",["csshiftjis","shiftjis","sjis","s_jis",],["Japanese",] ),
    ("shift_jis_2004",["shiftjis2004","sjis_2004","sjis2004",],["Japanese",] ),
    ("shift_jisx0213",["shiftjisx0213","sjisx0213","s_jisx0213",],["Japanese",] ),
    ("utf_16",["U16","utf16",],["all languages",] ),
    ("utf_16_be",["UTF-16BE",],["all languages (BMP only)",] ),
    ("utf_16_le",["UTF-16LE",],["all languages (BMP only)",] ),
    ("utf_8",["U8","UTF","utf8",],["all languages",] ),
    ("utf_8_sig",[],["all languages",] ),
    ("utf_7",["U7","unicode-1-1-utf-7",],["all languages",] ),
    ]


def get_candidate_for_language(language):
    r=[]
    for (codec,als,lng) in ALL_CODEC_CANDIDATE:
        for ll in lng:
            if ll.startswith(language):
                r.append((codec,als,lng))
                continue
            elif ll.endswith(language):
                r.append((codec,als,lng))
                continue
    return r

def codec_try_and_check(teststrings, codecandidates):
    accept=[]
    done=[]
    for codecdata in codecandidates:
        try:
            rr=[]
            for t in teststrings:
                rr.append(t.decode(codecdata[0]))
            if not rr in done:
                accept.append(codecdata)
                done.append(rr)
        except:
            continue
    return accept

def detect_file_name_codec(zf,language=""):
    teststrings=[f for f in zf.namelist()]
#    if chardet:
#        pass
    codecandidates=get_candidate_for_language(language)
    if language != "" and language != "all":
        codecandidates=codecandidates+get_candidate_for_language("all")
    return codec_try_and_check(teststrings, codecandidates)

def get_file_name_dict(zf, codec, basedir):
    r={}
    for f in zf.namelist():
        r[f] = os.path.join(basedir,f.decode(codec))
    return r    

def rename_and_unzip(zf, fndic, forth=False):
    for originalname in zf.namelist():
        newname = fndic[originalname]
        newdir = os.path.dirname(newname)
        if not os.path.exists(newdir):
            print "  creating:", newdir
            os.makedirs(newdir)
        if os.path.basename(newname):
            if not forth:
                if os.path.exists(newname):
                    print "replace", newname,
                    ans = raw_input("? [y]es, [n]o, [A]ll, [N]one, (rename;not implemented yet):")
                    if(ans.startswith("y")):
                        pass
                    elif(ans.startswith("n")):
                        continue 
                    elif(ans.startswith("A")):
                        forth=True
                    else:
                        break
            print "  inflating:", newname
            newfile = file(newname, 'wb')
            newfile.write(zf.read(originalname))
            newfile.close()

def show_file_name_codec(codecdata):
    print "Detected file name codec:", codecdata[0], 
    if len(codecdata[1])>0:
        print "(aka.",
        for ai in codecdata[1]:
            print ai,
        print ")",
    print "/",
    for li in codecdata[2]:
        print li,
    print 

def cui_mode_main(opt):
    for zipfilepath in opt["zipfile"]:
        zf = zipfile.ZipFile(zipfilepath, 'r')
        if opt["decode"]:
            codec=opt["decode"]
        else:
            candidate = detect_file_name_codec(zf,opt["language"])
            if len(candidate)==1:
                show_file_name_codec(candidate[0])
                codec=candidate[0][0]
            elif len(candidate)==0:
                codec=""
                print "No candidate was detected.  Plese try the following option: --language none"
            else:
                codec=""
                for codecdata in candidate:
                    show_file_name_codec(codecdata)
                print "Many candidates. Plese use the following option:  --decode some_codec_you_chose"
        if codec:
            fndic = get_file_name_dict(zf, codec,opt["outdir"])
            rename_and_unzip(zf, fndic)        
            
        zf.close()




if __name__ == '__main__':
    opt={
        "zipfile":[], 
        "outdir": "", 
        "language": "", 
        "gui": False,
        "decode":"",
        }

    (loc,enc)=locale.getdefaultlocale()
    if loc.startswith("ja"):
        opt["language"]="Japanese"
    elif loc.startswith("ko"):
        opt["language"]="Korean"
    elif loc.startswith("zh"):
        opt["language"]="Chinese"
    elif loc.startswith("ru"):
        opt["language"]="Russian"
        
    key=None
    for arg in sys.argv[1:]:
        if key:
            if key=="language" and arg=="none":
                opt[key]=""
            else:
                opt[key]=arg
            key=None
        else:
            if arg=="--gui":
                opt["gui"]=True
            if arg=="--decode":
                key="decode"
            elif arg=="--language":
                key="language"
            elif arg=="-d":
                key="outdir"
            else:
                opt["zipfile"].append(arg)


    if len(sys.argv)==1:
        print "USAGE:"
        print "\tpython",sys.argv[0],"zipfile.zip [zipfile2.zip ..] [-d outputdir] [--decode (shift_jis_2004|euc_jp|..)] [--language (Japanese|none|..)]"
        print ""
        print "NOTE:"
        print "\tIf omite the option --decode, then try to detect."
        print "\tIf omite the option --language, then try to detect."
        print "\tIf omite the option -d, then use the current directry ./ ."
    elif opt["gui"]:
        print "gui mode have been not implemented yet."
        pass
    else:
        cui_mode_main(opt)
