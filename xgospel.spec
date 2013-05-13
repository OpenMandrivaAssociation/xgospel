%define	name	xgospel
%define	version	1.12d
%define	release	%mkrel 20

Summary:	An X11 client for Internet Go Server
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Strategy
Source0:	http://img.teaser.fr/~jlgailly/%{name}-%{version}.tar.bz2
Patch0:		menu-crash-fix.diff
Patch1:		xgospel-1.12d-prefix.patch
Patch2:		xgospel-1.12d-new-server.patch
URL:		http://gailly.net/xgospel/index.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xmu)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xt)
BuildRequires:	bison
BuildRequires:	imagemagick

%description
Xgospel is an X11 client for Internet Go Server, it provides a graphical 
interface with a lot of features to play on the Internet using IGS 
(a place with players of all countries playing Go).

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p0

%build
%define Werror_cflags %nil
%configure2_5x
make

%install
rm -fr %buildroot
%makeinstall

mkdir -p %buildroot%{_datadir}/%{name}
cp *.xpm *.res my/*.xpm %buildroot%{_datadir}/%{name}
 
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=xgospel
Comment=An X11 client for Internet Go Server
Exec=%{name}    
Icon=%{name}    
Terminal=false  
Type=Application
Categories=Game;StrategyGame;
EOF

mkdir -p %buildroot%_iconsdir/hicolor/{48x48,32x32,16x16}/apps
convert -resize 48x48 my/XgospelIcon.xpm %buildroot%_iconsdir/hicolor/48x48/apps/%name.png
convert -resize 32x32 my/XgospelIcon.xpm %buildroot%_iconsdir/hicolor/32x32/apps/%name.png
convert -resize 16x16 my/XgospelIcon.xpm %buildroot%_iconsdir/hicolor/16x16/apps/%name.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif
 
%if %mdkversion < 200900
%postun
%{clean_menus} 
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES FAQ INSTALL README README.1ST TODO my/COPYRIGHTS
%{_bindir}/*
%{_datadir}/xgospel
%{_iconsdir}/hicolor/*/*/*
%{_datadir}/applications/*.desktop


%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 1.12d-20mdv2011.0
+ Revision: 634902
- simplify BR

* Mon Sep 21 2009 Thierry Vignaud <tv@mandriva.org> 1.12d-19mdv2010.0
+ Revision: 446188
- rebuild

* Sun Apr 05 2009 Funda Wang <fwang@mandriva.org> 1.12d-18mdv2009.1
+ Revision: 364147
- fix crash

* Sun Apr 05 2009 Funda Wang <fwang@mandriva.org> 1.12d-17mdv2009.1
+ Revision: 364105
- add icons

* Sun Apr 05 2009 Funda Wang <fwang@mandriva.org> 1.12d-16mdv2009.1
+ Revision: 364092
- use new server
- fix str fmt
- use normal prefix

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 1.12d-15mdv2009.0
+ Revision: 262434
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.12d-14mdv2009.0
+ Revision: 257091
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.12d-12mdv2008.1
+ Revision: 130210
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import xgospel


* Mon Oct 09 2006 Lenny Cartier <lenny@mandriva.com> 1.12d-12mdv2007.1
- xdg

* Wed Jul 06 2005 Lenny Cartier <lenny@mandriva.com> 1.12d-11mdk
- rebuild

* Wed Jun 16 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.12d-10mdk
- rebuild
- drop Prefix tag
- cosmetics

* Fri Jun 11 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.12d-9mdk
- rebuild

* Sun Dec 07 2003 Franck Villaume <fvill@freesurf.fr> 1.12d-8mdk
- some BuildRequires

* Fri Jan 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.12d-7mdk
- rebuild

* Thu  Aug 22 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.12d-6mdk
- rebuild

* Wed Dec 26 2001 David BAUDENS <baudens@mandrakesoft.com> 1.12d-5mdk
- Use default strategy icon for menu entry

* Fri Aug 24 2001 Etienne Faure <etienne@mandrakesoft.com> 1.12d-4mdk
- rebuild

* Wed Sep 20 2000  Lenny Cartier <lenny@mandrakesoft.com> 1.12d-3mdk
- build release
- menu

* Thu May 04 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.12d-2mdk
- fix group

* Wed Dec 29 1999 Jerome Dumonteil <jd@mandrakesoft.com>
- initial release
- relocated default xpm to /usr/X11R6/lib/xgospel
