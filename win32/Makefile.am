## -*- Makefile -*-
##---------------------------------------------------------------------------
## Makefile.am for win32/OpenRTM-aist
##
## $Id: Makefile.am 725 2008-05-13 16:49:04Z n-ando $
##---------------------------------------------------------------------------
SUBDIRS = OpenRTM-aist .


clean-clocal:
	rm -rf ../$(PACKAGE_TARNAME)-$(VERSION)-win32.zip *~


dist-hook:
	rm -rf ../$(PACKAGE_TARNAME)-$(VERSION)-win32.zip
	find ./OpenRTM-aist/ \! -path '*.svn*' \! -path '*CVS*' \
		\! -path '*#*' \! -path '*~' > zip_list
	cat zip_list | zip -@ ../$(PACKAGE_TARNAME)-$(VERSION)-win32.zip
	rm -f zip_list
