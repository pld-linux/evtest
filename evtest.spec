Summary:	Event device test program
Summary(pl.UTF-8):	Program do testowania urządzeń wejściowych generujących zdarzenia
Name:		evtest
Version:	1.31
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://cgit.freedesktop.org/evtest/snapshot/%{name}-%{version}.tar.bz2
# Source0-md5:	1d95cd9952d34dd15f93adb197323073
URL:		http://cgit.freedesktop.org/evtest/
BuildRequires:	asciidoc
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libxslt-progs
BuildRequires:	pkgconfig
BuildRequires:	xmlto
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
evtest is a simple utility to query information about input devices
and watch the event stream generated by input devices.

%description -l pl.UTF-8
evtest to proste narzędzie do pobierania informacji o urządzeniach
wejściowych i oglądania strumienia zdarzeń generowanych przez te
urządzenia.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/evtest.1*
