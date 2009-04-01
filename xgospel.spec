%define	name	xgospel
%define	version	1.12d
%define	release	%mkrel 16

Summary:	An X11 client for Internet Go Server
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Strategy
Source0:	http://img.teaser.fr/~jlgailly/%{name}-%{version}.tar.bz2
Patch0:		xgospel-1.12d-fix-str-fmt.patch
Patch1:		xgospel-1.12d-prefix.patch
URL:		http://gailly.net/xgospel/index.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	X11-devel bison xpm-devel

%description
Xgospel is an X11 client for Internet Go Server, it provides a graphical 
interface with a lot of features to play on the Internet using IGS 
(a place with players of all countries playing Go).

%prep
%setup -q
%patch0 -p1 -b .str
%patch1 -p0

%build
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
%{_datadir}/applications/*.desktop
