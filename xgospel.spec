%define	name	xgospel
%define	version	1.12d
%define	release	%mkrel 12

Summary:	An X11 client for Internet Go Server
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Strategy
Source0:	http://img.teaser.fr/~jlgailly/%{name}-%{version}.tar.bz2
URL:		http://gailly.net/xgospel/index.html
BuildRequires:	X11-devel bison xpm-devel

%define	__prefix	%{_prefix}/X11R6

%description
Xgospel is an X11 client for Internet Go Server, it provides a graphical 
interface with a lot of features to play on the Internet using IGS 
(a place with players of all countries playing Go).

%prep
%setup -q

%build
mv resources.c resources.c.orig
sed -e 's|board.xpm|/usr/X11R6/lib/xgospel/board.xpm|' <resources.c.orig >resources.c
mv XGospel.res XGospel.res.orig
sed -e 's|\(board.xpm\)|\(/usr/X11R6/lib/xgospel/board.xpm\)|' <XGospel.res.orig >XGospel.res
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{__prefix}
make

%install
rm -fr %buildroot

mkdir -p $RPM_BUILD_ROOT%{__prefix}
make prefix=$RPM_BUILD_ROOT%{__prefix} install 
mkdir -p $RPM_BUILD_ROOT%{__prefix}/lib/xgospel
mv *.xpm $RPM_BUILD_ROOT%{__prefix}/lib/xgospel
mv my/*.xpm $RPM_BUILD_ROOT%{__prefix}/lib/xgospel
mv *.res $RPM_BUILD_ROOT%{__prefix}/lib/xgospel

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}): \
command="%{__prefix}/bin/xgospel" \
title="Xgospel" \
longtitle="A graphical client for Internet Go Server" \
icon="strategy_section.png" \
needs="x11" \
section="More Applications/Games/Strategy" \
xdg="true"
EOF
 
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=xgospel
Comment=An X11 client for Internet Go Server
Exec=%{name}    
Icon=%{name}    
Terminal=false  
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Strategy;Game;StrategyGame;
EOF

%post
%{update_menus}
 
%postun
%{clean_menus} 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES FAQ INSTALL README README.1ST TODO my/COPYRIGHTS
%dir %{__prefix}/lib/xgospel
%{__prefix}/bin/*
%{__prefix}/lib/xgospel/XGospel.res
%{__prefix}/lib/xgospel/board.xpm
%{__prefix}/lib/xgospel/pagoda.xpm
%{__prefix}/lib/xgospel/XgospelIcon.xpm
%{_menudir}/*
%_datadir/applications/*

