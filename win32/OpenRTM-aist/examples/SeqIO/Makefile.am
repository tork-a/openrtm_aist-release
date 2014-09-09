## -*- Makefile -*-
##---------------------------------------------------------------------------
## Makefile.am for win32/OpenRTM-aist/examples/SeqIO
##
## $Id: Makefile.am 2289 2012-02-03 02:33:33Z kurihara $
##---------------------------------------------------------------------------
clean-local:
	rm -rf Debug Release
	rm -rf *~ *.cpp *.h *.idl rtc.conf
	rm -rf *.vcproj *.vcxproj *.user *.ncb *.suo
	rm -rf SeqIn SeqInComp SeqOut SeqOutComp

src:
	cp -p $(top_srcdir)/examples/SeqIO/*.cpp .
	cp -p $(top_srcdir)/examples/SeqIO/*.h .
	cp -p $(top_srcdir)/examples/SeqIO/rtc.conf .
	qkc -O- -ms *.cpp
	qkc -O- -ms *.h

dist-hook: src
