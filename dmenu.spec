Summary:	dmenu is a generic menu for X
Summary(hu.UTF-8):	dmenu egy általános menü X-hez
Summary(pl.UTF-8):	System menu dla X
Name:		dmenu
Version:	4.0
Release:	2
License:	MIT/X
Group:		Applications
Source0:	http://code.suckless.org/dl/tools/%{name}-%{version}.tar.gz
# Source0-md5:	66e761a653930cc8a21614ba9fedf903
URL:		http://tools.suckless.org/dmenu
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dynamic menu is a generic menu for X, originally designed for dwm. It
manages huge amounts (up to 10.000 and more) of user defined menu
items efficiently.

%description -l hu.UTF-8
Dynamic menu egy általános menü X-hez, eredetileg a dwm-hez készítve.
Valóban nagy mennyiségű (10.000 és több) felhasználó által definiált
menüelemet képes hatékonyan kezelni.

%description
System menu ogólnego przeznaczenia dla serwrea X. dmenu został
pierwotnie zaprojektowany dla dla zarządcy okien dwm, ale jest
wykorzystywany również przez inne aplikacje. dmenu może efektywnie
zarządzać ogromną ilością (10000 i więcej) zdefiniowanych przez
użytkownika pozycji menu.

%prep
%setup -q

%build
cat << 'EOF' >> config.mk
PREFIX=%{_prefix}
CFLAGS:=%{rpmcflags} $(filter-out -Os,$(CFLAGS))
LDFLAGS:=%{rpmldflags} $(LDFLAGS)
EOF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/dmenu
%attr(755,root,root) %{_bindir}/dmenu_path
%attr(755,root,root) %{_bindir}/dmenu_run
%{_mandir}/man1/dmenu.1*
