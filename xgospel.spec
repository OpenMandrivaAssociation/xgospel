%define	name	xgospel
%define	version	1.12d
%define	release	%mkrel 17

Summary:	An X11 client for Internet Go Server
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Strategy
Source0:	http://img.teaser.fr/~jlgailly/%{name}-%{version}.tar.bz2
Patch1:		xgospel-1.12d-prefix.patch
Patch2:		xgospel-1.12d-new-server.patch
URL:		http://gailly.net/xgospel/index.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	X11-devel bison xpm-devel
BuildRequires:	imagemagick

%description
Xgospel is an X11 client for Internet Go Server, it provides a graphical 
interface with a lot of features to play on the Internet using IGS 
(a place with players of all countries playing Go).

%prep
%setup -q
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
