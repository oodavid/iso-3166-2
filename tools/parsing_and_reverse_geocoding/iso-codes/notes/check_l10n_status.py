#!/usr/bin/env python

import sys
import glob
import os.path
from subprocess import Popen, PIPE

basedir = os.path.realpath(os.path.join(os.path.split(sys.argv[0])[0], ".."))
iso_639_dir = os.path.join(basedir, "iso_639")
iso_639_3_dir = os.path.join(basedir, "iso_639_3")
iso_3166_dir = os.path.join(basedir, "iso_3166")
iso_3166_2_dir = os.path.join(basedir, "iso_3166_2")
iso_4217_dir = os.path.join(basedir, "iso_4217")
iso_15924_dir = os.path.join(basedir, "iso_15924")
dirs = [iso_639_dir,
        iso_639_3_dir,
        iso_3166_dir,
        iso_3166_2_dir,
        iso_4217_dir,
        iso_15924_dir]

def _cmp(l, r):
    return -cmp(l[1:], r[1:])

def main():
    first = True
    for dir_ in dirs:
        if first:
            first = False
        else:
            print
            print
        key = os.path.split(dir_)[1]
        print key
        print "=" * len(key)
        print

        pattern = os.path.join(dir_, "*.po")
        keys = ["translated", "fuzzy", "untranslated"]
        ress = []
        for fname in sorted(glob.glob(pattern)):
            locale = os.path.split(fname)[1][:-3]
            log = Popen(["env", "-i", "msgfmt", "-v", fname],
                         stderr=PIPE).stderr.read().split()
            res = [locale, 0, 0, 0]
            for idx, key in enumerate(keys):
                try:
                    if key in log:
                        res[idx+1] = int(log[log.index(key)-1])
                except:
                    pass
            ress.append(res)
        ress.sort(cmp=_cmp)
        print 'locale\t%12s / %12s / %12s' % (keys[0], keys[1], keys[2])
        for x in ress:
            print "%s\t%12i / %12i / %12i" % tuple(x)

if __name__ == '__main__':
    main()


