Summary:	Python bindings for MATE's caja
Name:		python-caja
Version:	1.4.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Development/Python
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	mate-common
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(mate-python-2.0)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(python)

Requires:	mate-python-mateconf

%description
These are bindings for the caja extension library
introduced in MATE.

%package devel
Summary:	Pkgconfig file and examples for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}

%description devel
Pkgconfig file and examples for %{name}.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x

%make

%install
%makeinstall_std


find $RPM_BUILD_ROOT -name '*.la' -exec rm {} \;

%files
%doc AUTHORS ChangeLog NEWS 
%{_libdir}/caja-python/caja.so
%{_libdir}/caja/extensions-2.0/*

%files devel
%{_libdir}/pkgconfig/caja-python.pc
%doc %{_datadir}/doc/caja-python/README
%doc %{_datadir}/doc/caja-python/examples/*




%changelog
* Thu Jun 07 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 803195
- imported package python-caja

