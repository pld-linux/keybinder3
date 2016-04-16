#
# Conditional build:
%bcond_without	static_libs	# static library build
#
Summary:	keybinder library for GTK+3
Summary(pl.UTF-8):	Biblioteka keybinder dla GTK+3
Name:		keybinder3
Version:	0.3.1
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	https://github.com/engla/keybinder/archive/keybinder-3.0-v%{version}.tar.gz
# Source0-md5:	c2f534d7977b337b333313ac9b8bd6c9
URL:		https://github.com/engla/keybinder/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.9.2
BuildRequires:	gobject-introspection-devel >= 0.6.7
BuildRequires:	gnome-common
BuildRequires:	gtk-doc >= 1.14
BuildRequires:	gtk+3-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
keybinder is a library for registering global keyboard shortcuts.
Keybinder works with GTK-based applications using the X Window System.

%description -l pl.UTF-8
keybinder jest biblioteką umożliwiającą rejestrowanie globalnych
skrótów klawiszowych. Działa z aplikacjami opartymi na GTK.

%package devel
Summary:	Header files for keybinder3 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki keybinder3
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3-devel

%description devel
Header files for keybinder3 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki keybinder3.

%package static
Summary:	Static keybinder3 library
Summary(pl.UTF-8):	Statyczna biblioteka keybinder3
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static keybinder3 library.

%description static -l pl.UTF-8
Statyczna biblioteka keybinder3.

%package doc
Summary:	HTML documentation for keybinder3 library
Summary(pl.UTF-8):	Dokumentacja w HTML biblioteki keybinder3
Group:		Documentation
Requires:	%{name} = %{version}-%{release}

%description doc
HTML documentation for keybinder3 library.

%description devel -l pl.UTF-8
Dokumentacja w HTML biblioteki keybinder3.

%prep
%setup -q -n keybinder-keybinder-3.0-v%{version}

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %ghost %{_libdir}/libkeybinder-3.0.so.0
%attr(755,root,root) %{_libdir}/libkeybinder-3.0.so.*.*.*
%{_libdir}/girepository-1.0/Keybinder-3.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkeybinder-3.0.so
%{_libdir}/libkeybinder-3.0.la
%{_datadir}/gir-1.0/Keybinder-3.0.gir
%dir %{_includedir}/keybinder-3.0
%{_includedir}/keybinder-3.0/keybinder.h
%{_pkgconfigdir}/keybinder-3.0.pc
%{_examplesdir}/%{name}-%{version}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libkeybinder-3.0.a
%endif

%files doc
%defattr(644,root,root,755)
%{_gtkdocdir}/keybinder-3.0
