DOMAIN = iso_639_3
VERSION = @PACKAGE_VERSION@

xmldir = $(datadir)/xml/iso-codes
xml_DATA = $(DOMAIN).xml

pofiles = $(wildcard $(srcdir)/*.po)
mofiles = $(patsubst $(srcdir)/%.po,%.mo, $(pofiles))
noinst_DATA = $(mofiles) $(xml_DATA:.xml=.pot) 

iso_639_3.pot: iso_639_3.xml
	../iso2pot.py --is-version ${VERSION} --comment id \
		--fields name --outfile $@ $< 

EXTRA_DIST = \
	$(pofiles)	\
	$(xml_DATA)	\
	iso_639_3.pot

MOSTLYCLEANFILES = \
	$(mofiles)

check-local: check-content

include $(top_srcdir)/rules.make
