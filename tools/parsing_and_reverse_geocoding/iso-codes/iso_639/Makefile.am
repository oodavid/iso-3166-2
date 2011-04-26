DOMAIN = iso_639
VERSION = @PACKAGE_VERSION@

xmldir = $(datadir)/xml/iso-codes
xml_DATA = $(DOMAIN).xml

pofiles = $(wildcard $(srcdir)/*.po)
mofiles = $(patsubst $(srcdir)/%.po,%.mo, $(pofiles))
noinst_DATA = $(mofiles) iso_639.pot

iso_639.pot: iso_639.xml
	$(top_srcdir)/iso2pot.py --is-version $(VERSION) \
		--comments iso_639_2T_code \
		--comments iso_639_1_code \
	        --fields name --outfile $@ iso_639.xml

EXTRA_DIST = \
	$(pofiles)	\
	$(xml_DATA)	\
	iso_639.pot

MOSTLYCLEANFILES = \
	$(mofiles)

check-local: check-content

include $(top_srcdir)/rules.make
