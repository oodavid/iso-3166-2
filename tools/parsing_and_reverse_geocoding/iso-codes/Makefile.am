SUBDIRS = iso_15924 iso_3166 iso_3166_2 iso_4217 iso_639 iso_639_3

pkgconfigdir = $(datadir)/pkgconfig
pkgconfig_DATA = iso-codes.pc

EXTRA_DIST = \
	LICENSE			\
	rules.make		\
	iso2pot.py		\
	check_valid_utf8.pl

DISTCLEANFILES = $(pkgconfig_DATA)


.PHONY: release
release: update-po check distcheck

.PHONY: update-po
update-po:
	for domain in $(SUBDIRS); do \
		cd $$domain && make update-po && cd ..; \
	done

.PHONY: sign-release
sign-release: iso-codes-$(VERSION).tar.bz2
	rm -f iso-codes-$(VERSION).tar.bz2.sig
	gpg --detach-sign iso-codes-$(VERSION).tar.bz2

.PHONY: upload
upload:
	@if [[ "$(ALIOTH_USERNAME)" == "" ]]; then \
		echo "Please set your Alioth username. Example command line:"; \
		echo "  ALIOTH_USERNAME=toddy make upload"; \
	fi
	@if [[ -f "iso-codes-$(VERSION).tar.bz2" ]] \
	&& [[ -f "iso-codes-$(VERSION).tar.bz2.sig" ]] \
	&& [[ -n "$(ALIOTH_USERNAME)" ]]; then \
		scp iso-codes-$(VERSION).tar.* \
		$(ALIOTH_USERNAME)@alioth.debian.org:/var/lib/gforge/chroot/ftproot/pub/pkg-isocodes; \
	fi
