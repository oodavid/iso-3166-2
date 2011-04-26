DOMAIN = iso_3166_2
VERSION = @PACKAGE_VERSION@

xmldir = $(datadir)/xml/iso-codes
xml_DATA = $(DOMAIN).xml

pofiles = $(wildcard $(srcdir)/*.po)
mofiles = $(patsubst $(srcdir)/%.po,%.mo, $(pofiles))
noinst_DATA = $(mofiles) $(xml_DATA:.xml=.pot) 

iso_3166_2.pot: iso_3166_2.xml
	../iso2pot.py --is-version ${VERSION} --comment code \
		--fields name --outfile $@ $< 

EXTRA_DIST = \
	$(pofiles)	\
	$(xml_DATA)	\
	iso_3166_2.pot

MOSTLYCLEANFILES = \
	$(mofiles)

check-local: check-content

include $(top_srcdir)/rules.make
