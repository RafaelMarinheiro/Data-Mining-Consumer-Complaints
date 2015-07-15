# -*- coding: UTF-8 -*-

import unicodedata
import sys
import codecs

def main():
    fname = sys.argv[1]
    with codecs.open(fname, "r", "latin_1") as f:
        with open(fname[:-4]+"_sanitized.csv", "w") as fs:
            for l in f:
                s = l
                # s = unicode(l, 'latin_1')
                s = unicodedata.normalize('NFKD', unicode(s)).encode('ascii','ignore')
                fs.write(s)



if __name__ == '__main__':
    main()