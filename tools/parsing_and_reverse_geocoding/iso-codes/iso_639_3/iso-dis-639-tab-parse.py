#!/usr/bin/env python
"""
Parse the SIL.org iso_639_3.tab file and create
an XML file for our own use.
"""

inverted_names = {}
names=open("iso_639_3_Name_Index.tab")
for li in names.readlines():
	(code, name, inverted_name) = li.split('\t')
	inverted_name = inverted_name.strip()
	if inverted_name != name:
		inverted_names[code] = inverted_name
names.close()


f=open("iso_639_3.tab")

ot=open("iso_639_3.xml","w")

ot.write("""<?xml version="1.0" encoding="UTF-8" ?>

<!--
This file gives a list of all languages in the ISO 639-3
standard, and is used to provide translations via gettext

Copyright (C) 2005 Alastair McKinstry <mckinstry@computer.org>
Copyright (C) 2008 Tobias Quathamer <toddy@debian.org>

    This file is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.

    This file is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
    Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public
    License along with this file; if not, write to the Free Software
    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

Source: <http://www.sil.org/iso639-3/>
-->

<!DOCTYPE iso_639_3_entries [
	<!ELEMENT iso_639_3_entries (iso_639_3_entry+)>
	<!ELEMENT iso_639_3_entry EMPTY>
	<!ATTLIST iso_639_3_entry
		id		CDATA	#REQUIRED
		name		CDATA	#REQUIRED
		type		CDATA	#REQUIRED
		scope 		CDATA   #REQUIRED
		part1_code	CDATA	#IMPLIED
		part2_code	CDATA	#IMPLIED
	>
]>

<iso_639_3_entries>
""")

f.readline()		# throw away the header
for li in f.readlines():
	(code, part2b, part2t, part1, scope, type, name, comment) = li.split('\t')
	comment = comment.strip()
	ot.write('\t<iso_639_3_entry\n')
	ot.write('\t\tid="%s"\n' % code)
	if part1 != '':
		ot.write('\t\tpart1_code="%s"\n' % part1)
	if part2b != '':
		ot.write('\t\tpart2_code="%s"\n' % part2b)
	ot.write('\t\tscope="%s"\n' % scope)
	ot.write('\t\ttype="%s"\n' % type)
	if inverted_names.has_key(code):
		name = inverted_names[code]
	ot.write('\t\tname="%s" />\n' % name)

ot.write('</iso_639_3_entries>\n')
ot.close()
f.close()
	
	

