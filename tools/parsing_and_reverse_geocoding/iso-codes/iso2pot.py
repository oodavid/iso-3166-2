#!/usr/bin/env python
# coding: utf-8
#
# Read iso-codes data file and output a .pot file
#
# Copyright © 2004,2005 Alastair McKinstry <mckinstry@debian.org>
# Copyright © 2006,2007 Tobias Quathamer <toddy@debian.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

from xml.sax import make_parser, SAXException, SAXParseException
from xml.sax.handler import feature_namespaces, ContentHandler
import sys, os, getopt, urllib2, locale, time

class printPot(ContentHandler):
    def __init__(self, nameslist,comment, ofile):
         """ 
	 nameslist is the elements to be printed in msgid strings,
	 comment is the attribute to be used in the comment line
	 """
         self.attrnames = nameslist
	 self.comment = comment
	 self.ofile = ofile
	 self.done = {}
         self.result = []


    def startElement(self, name, attrs):
        # Get the name attributes
	for aname in self.attrnames:
            n = attrs.get(aname, None)
            date_withdrawn = attrs.get('date_withdrawn', None)
            c = [attrs.get(x, None) for x in self.comment]
            if type(n) == unicode:
                n = n.encode('UTF-8')
            for i in range(len(c)):
                if type(c[i]) == unicode:
                    c[i] = c[i].encode('UTF-8')
            if n != None:
                if not self.done.has_key(n):
                    self.result.append([n])
                    self.done[n] = len(self.result)-1
                comment_str = ", ".join([x for x in c if x is not None])
                if comment_str:
                    # Special case for ISO 3166 and ISO 4217, as they contain
                    # historic entries. In order to not trigger bug reports
                    # from translators for "obsolete" entries, we specially
                    # mark those historic entries.
                    if date_withdrawn is not None:
                        translator_comment = 'historic %s for %s (withdrawn %s)' % \
                        (aname, comment_str, date_withdrawn)
                    else:
                        translator_comment = '%s for %s' % \
                        (aname, comment_str)
                    self.result[self.done[n]].append(translator_comment)

def printHeader(ofile, iso_standard, report_bugs_to, version):
    """Print the file header
    """
    description = "# Translation of ISO " + iso_standard[0]
    if iso_standard[1]:
        description += " (" + iso_standard[1] + ")"
    description += " to LANGUAGE"

    ofile.write (description + "\n")
    ofile.write ("#\n")
    ofile.write ("# This file is distributed under the same license as the iso-codes package.\n")
    ofile.write ("#\n")
    ofile.write ("# Copyright ©\n")
    ofile.write ("# FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.\n")
    ofile.write ("#\n")
    ofile.write ("msgid \"\"\n")
    ofile.write ("msgstr \"\"\n")
    ofile.write ("\"Project-Id-Version: iso_" + iso_standard[0] + " " + version + "\\n\"\n")
    ofile.write ("\"Report-Msgid-Bugs-To: " + report_bugs_to + "\\n\"\n")
    ofile.write ("\"POT-Creation-Date: " + time.strftime('%F %H:%M%z') + "\\n\"\n")
    ofile.write ("\"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n\"\n")
    ofile.write ("\"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n\"\n")
    ofile.write ("\"Language-Team: LANGUAGE <LL@li.org>\\n\"\n")
    ofile.write ("\"MIME-Version: 1.0\\n\"\n")
    ofile.write ("\"Content-Type: text/plain; charset=UTF-8\\n\"\n")
    ofile.write ("\"Content-Transfer-Encoding: 8bit\\n\"\n")


## 
## MAIN
##

locale.setlocale(locale.LC_ALL, 'C')

try:
    (opts,trail)=getopt.getopt(sys.argv[1:],"f:c:o:v:",
                               ["fields=", "comments=", "is-version=", "outfile="])
    assert trail, "No argument provided"
except Exception,e:
    print "ERROR: %s" % e
    print
    print "Usage: iso2pot filename [filename ...]"
    print " filename: xml data file from iso-codes package"
    print " outfilename: Write to this file"
    sys.exit(1)

version = "VERSION"
report_bugs_to = "Debian iso-codes team <pkg-isocodes-devel@lists.alioth.\"\n\"debian.org>"
fields = ["name","official_name"]
comment = []
ofile = sys.stdout

for opt, arg in opts:
    if opt in ('-v', '--is-version'):
        version = arg
    elif opt in ('-f', '--fields'):
    	fields = arg.split(',')
    elif opt in ('-c','--comments'):
        comment.append(arg)
    elif opt in ('-o','--outfile'):
        ofile = open(arg, 'w')
if not comment:
    comment = ["code"]

# derive the ISO standard from the first file's name
# e.g. iso_3166_2.xml -> 3166-2
iso_number = trail[0].rstrip('.xml').split('_')
iso_number.remove('iso')
iso_number = '-'.join(iso_number)

if iso_number == '639' or iso_number == '639-3':
	iso_desc = 'language names'
elif iso_number == '3166':
	iso_desc = 'country names'
elif iso_number == '3166-2':
	iso_desc = 'country subdivision names'
elif iso_number == '4217':
	iso_desc = 'currency names'
elif iso_number == '15924':
	iso_desc = 'script names'
else:
	iso_desc = ''

iso_standard = [iso_number, iso_desc]

printHeader(ofile, iso_standard, report_bugs_to, version)

p = make_parser()

try:
    dh = printPot(fields, comment, ofile)
    p.setContentHandler(dh)
    for infile in trail:
        p.parse(infile)
    for x in dh.result:
        ofile.write("\n")
        if len(x) > 1:
            ofile.write("#. " + ', '.join(x[1:]) +  "\n")
        ofile.write ("msgid \"" + x[0] + "\"\n")
        ofile.write ("msgstr \"\"\n")
except SAXParseException, e:
    sys.stderr.write('%s:%s:%s: %s\n' % (e.getSystemId(),
                                         e.getLineNumber(),
                                         e.getColumnNumber(),
                                         e.getMessage()))
    sys.exit(1)
#except Exception, e:
#    sys.stderr.write('<unknown>: %s\n' % str(e))
#    sys.exit(1)


ofile.close()
