%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Python bindings for MATE's caja
Name:		python-caja
Version:	1.8.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Development/Python
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	gtk-doc
BuildRequires:	mate-common
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(python)

%description
These are bindings for the caja extension library
introduced in MATE.

%package devel
Summary:	Pkgconfig file and examples for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
Pkgconfig file and examples for %{name}.

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh

%build
%configure2_5x

%make

%install
%makeinstall_std
mkdir -p %{buildroot}%{_datadir}/caja-python/extensions

%files
%doc AUTHORS ChangeLog NEWS 
%dir %{_libdir}/caja
%dir %{_libdir}/caja/extensions-2.0
%{_libdir}/caja/extensions-2.0/*
%dir %{_datadir}/caja-python
%dir %{_datadir}/caja-python/extensions

%files devel
%{_libdir}/pkgconfig/caja-python.pc

