DOMAIN = iso_4217
VERSION = @PACKAGE_VERSION@

xmldir = $(datadir)/xml/iso-codes
xml_DATA = $(DOMAIN).xml

pofiles = $(wildcard $(srcdir)/*.po)
mofiles = $(patsubst $(srcdir)/%.po,%.mo, $(pofiles))
noinst_DATA = $(mofiles) $(xml_DATA:.xml=.pot) 

iso_4217.pot: iso_4217.xml
	../iso2pot.py --is-version ${VERSION}  --comments letter_code \
		--fields currency_name  --outfile $@ $< 

EXTRA_DIST = \
	$(pofiles)	\
	$(xml_DATA)	\
	iso_4217.pot

MOSTLYCLEANFILES = \
	$(mofiles)

check-local: check-content

include $(top_srcdir)/rules.make
