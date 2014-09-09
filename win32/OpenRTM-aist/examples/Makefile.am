## -*- Makefile -*-
##---------------------------------------------------------------------------
## Makefile.am for win32/OpenRTM-aist/examples
##
## $Id: Makefile.am 1680 2010-01-17 15:12:59Z n-ando $
##---------------------------------------------------------------------------
SUBDIRS = Composite ConfigSample SimpleIO SeqIO SimpleService USBCamera .

wxs:
	cp -p example.yaml ../installer/

clean-local:
	rm -f *~

dist-hook: clean-local wxs

EXTRA_DIST = example.yaml
