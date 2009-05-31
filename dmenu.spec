Summary:	dmenu is a generic menu for X
Summary(hu.UTF-8):	dmenu egy általános menü X-hez
Name:		dmenu
Version:	4.0
Release:	0.1
License:	MIT/X
Group:		Applications
Source0:	http://code.suckless.org/dl/tools/%{name}-%{version}.tar.gz
# Source0-md5:	66e761a653930cc8a21614ba9fedf903
URL:		http://tools.suckless.org/dmenu
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dynamic menu is a generic menu for X, originally designed for dwm. It
manages huge amounts (up to 10.000 and more) of user defined menu
items efficiently.

%description -l hu.UTF-8
dynamic menu egy általános menü X-hez, eredetileg a dwm-hez készítve.
Valóban nagy mennyiségű (10.000 és több) felhasználó által definiált
menüelemet képes hatékonyan kezelni.

%prep
%setup -q
sed -i "s@^PREFIX.*@PREFIX=%{_prefix}@" config.mk
sed -i "s@^\(CFLAGS.*\)-Os\(.*\)@\1 \2 %{rpmcflags}@" config.mk
sed -i "s@^\(LDFLAGS.*\)@\1 %{rpmldflags}@" config.mk


%build
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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/dmenu*
