iso-codes
=========
<http://pkg-isocodes.alioth.debian.org/>

This package provides lists of various ISO standards (e.g. country,
language, language scripts, and currency names) in one place, rather
than repeated in many programs throughout the system.

Currently there are lists of languages and countries embedded in
several different programs, which leads to dozens of lists of
200 languages, translated into more than 30 languages ... not
very efficient.

With this package, we create a single "gettext domain" for every
supported ISO standard which contains the translations of
that domain. It is easy for a programmer to re-use those
translations instead of maintaining their own translation
infrastructure. Moreover, the programmer does not need to follow
changes in the ISO standard and will not work with outdated
information.

To use this translation infrastructure, the programmer just needs
to call dgettext() in their program.

Example:
    dgettext("iso_639", "French")
will return the translation for "French", depending on the
current locale.

Furthermore, this package provides the ISO standards as XML files
to be used by other applications as well. All those XML files
are stored in the directory "/usr/share/xml/iso-codes".


NEWS: iso_3166.tab and iso_639.tab removed
==========================================

Please note that the plain text tabular files "iso_3166.tab" and
"iso_639.tab" have been removed from the directory /usr/share/iso-codes.
If you need that specific format, you can easily regenerate those
files. Install the package isoquery and run the following commands:

$ isoquery | cut -f 1,4 | sort > iso_3166.tab

$ isoquery --iso=639 | \
  sed -e "s/\t\t/\tXX\t/" | \
  awk -F"\t" '{print $2"\t"$1"\t"$3"\t"$4}' | \
  sort > iso_639.tab

See the output of "isoquery --help" or "man isoquery" for more
information and usage examples.


ISO 3166
========

This lists the 2-letter country code and "short" country name. The
official ISO 3166 maintenance agency is ISO. The gettext domain is
"iso_3166".
<http://www.iso.org/iso/country_codes>


ISO 639
=======

This lists the 2-letter and 3-letter language codes and language
names. The official ISO 639 maintenance agency is the Library of
Congress. The gettext domain is "iso_639".
<http://www.loc.gov/standards/iso639-2/>


ISO 639-3
=========

This is a further development of ISO 639-2, see above. All codes
of ISO 639-2 are included in ISO 639-3. ISO 639-3 attempts to
provide as complete an enumeration of languages as possible,
including living, extinct, ancient, and constructed languages,
whether major or minor, written or unwritten. The gettext
domain is "iso_639_3". The official ISO 639-3 maintenance agency
is SIL International.
<http://www.sil.org/iso639-3/>


ISO 4217
========

This lists the currency codes and names. The official ISO 4217
maintenance agency is the British Standards Institution. The
gettext domain is "iso_4217".
<http://www.bsi-global.com/en/Standards-and-Publications/Industry-Sectors/Services/BSI-Currency-Code-Service/>


ISO 15924
=========

This lists the language scripts names. The official ISO 15924
maintenance agency is the Unicode Consortium. The gettext
domain is "iso_15924".
<http://unicode.org/iso15924/>


ISO 3166-2
==========

The ISO 3166 standard includes a "Country Subdivision Code",
giving a code for the names of the principal administrative
subdivisions of the countries coded in ISO 3166. The official
ISO 3166-2 maintenance agency is ISO. The gettext domain is
"iso_3166_2".
<http://www.iso.org/iso/country_codes/background_on_iso_3166/iso_3166-2.htm>


Tracking updates to the various ISO standards
=============================================

Below is a list of websites we use to check for updates to the
standards. Please note that ISO 4217 is missing, because the BSI
does not provide a list of changes.

ISO 3166 and ISO 3166-2:
http://www.iso.org/iso/country_codes/check_what_s_new.htm
http://www.iso.org/iso/country_codes/updates_on_iso_3166.htm
http://www.iso.org/iso/en/prods-services/iso3166ma/02iso-3166-code-lists/list-en1-semic.txt

ISO-639:
http://www.loc.gov/standards/iso639-2/php/code_changes.php

ISO 639-3:
http://www.sil.org/iso639-3/codes.asp?order=639_3&letter=%25

ISO-15924:
http://unicode.org/iso15924/codechanges.html


Adding or updating translations
===============================

You can send your translation as a bug report against the package
iso-codes to the Debian Bug Tracking System. You can either send an email
or use the tool reportbug. More details are on this website:

  <http://bugs.debian.org/>

Another way to send in a translation is using the Translation
Project (TP). You can find more information about it on their
website:

  <http://www.translationproject.org/>


Reporting a bug
===============

If you find a bug in iso-codes, there are several ways to contact us.

* Alioth Bug Tracking System
  <https://alioth.debian.org/tracker/?atid=413077&group_id=30316>
  This system can be accessed via webbrowser.

* Debian Bug Tracking System
  <http://bugs.debian.org/>
  This system can be accessed via e-mail.

* Development mailing list
  <mailto:pkg-isocodes-devel@lists.alioth.debian.org>
  You can subscribe or unsubscribe at this webpage:
  <http://lists.alioth.debian.org/mailman/listinfo/pkg-isocodes-devel>


Developing using pkgconfig
==========================

A pkgconfig file has been included to aid developing with this
package. You can detect the prefix where the translations have
been placed using

$ pkg-config --variable=prefix iso-codes
/usr

You can detect which gettext domains have been installed using
$ pkg-config --variable=domains iso-codes
iso_15924 iso_3166 iso_4217 iso_639 iso_3166_2 iso_639_3


-- 
Alastair McKinstry, <mckinstry@debian.org>, 2003-12-24
Christian Perrier, <bubulle@debian.org>, 2007-09-09
Tobias Quathamer, <toddy@debian.org>, 2008-01-22
