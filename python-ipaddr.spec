%include	/usr/lib/rpm/macros.python
%define 	module ipaddr

Summary:	Python module is useful to manipulate IP addresses (sets)
Summary(pl):	Modu� pythona u�yteczny do manipulacji adresami/zbiorami adr IP
Name:		python-%{module}
Version:	1.1
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	ftp://ftp.cendio.se/pub/playground/python/%{module}-%{version}.tar.gz
URL:		http://www.vex.net/parnassus/apyllo.py/126307487
%pyrequires_eq 	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is useful if you need to manipulate IP addresses or sets
of IP addresses.

%description -l pl
Modu� przydatny do manipulacji adresami IP oraz ich zbiorami.

%prep
%setup -q -n %{module}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}
install * $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%{py_sitedir}/*.py[co]
