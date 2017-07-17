%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Python bindings for MATE's caja
Name:		python-caja
Version:	1.18.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Development/Python
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	mate-common
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(pygobject-3.0)
BuildRequires:	pkgconfig(python)

#Provides:	python2-caja

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides bindings for the caja extension library with Python.

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS 
%dir %{_libdir}/caja
%dir %{_libdir}/caja/extensions-2.0
%{_libdir}/caja/extensions-2.0/*
%dir %{_datadir}/caja-python
%dir %{_datadir}/caja-python/extensions
%{_datadir}/caja/extensions/libcaja-python.caja-extension

#---------------------------------------------------------------------------

%package devel
Summary:	Pkgconfig file and examples for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
Pkgconfig file and examples for %{name}.

%files devel
%{_libdir}/pkgconfig/caja-python.pc

#---------------------------------------------------------------------------

%prep
%setup -q

# force to python
find examples/ -name \*py -exec sed -i -e 's|#!/usr/bin/python|#!/usr/bin/env python|' '{}' \;

%build
export PYTHON=%{__python2}

#NOCONFIGURE=yes ./autogen.sh
%configure
%make

%install
%makeinstall_std
mkdir -p %{buildroot}%{_datadir}/caja-python/extensions

# locales
%find_lang %{name} --with-gnome --all-name

