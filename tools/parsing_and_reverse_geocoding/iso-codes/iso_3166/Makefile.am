DOMAIN = iso_3166
VERSION = @PACKAGE_VERSION@

xmldir = $(datadir)/xml/iso-codes
xml_DATA = $(DOMAIN).xml

pofiles = $(wildcard $(srcdir)/*.po)
mofiles = $(patsubst $(srcdir)/%.po,%.mo, $(pofiles))
noinst_DATA = $(mofiles) $(xml_DATA:.xml=.pot)

iso_3166.pot: iso_3166.xml
	../iso2pot.py --is-version $(VERSION) --comments alpha_3_code \
		--fields name,names,official_name,common_name --outfile $@ $<

EXTRA_DIST = \
	$(pofiles)	\
	$(xml_DATA)	\
	iso_3166.pot

MOSTLYCLEANFILES = \
	$(mofiles)

check-local: check-content

include $(top_srcdir)/rules.make
