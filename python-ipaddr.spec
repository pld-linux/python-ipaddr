
%define 	module	ipaddr

Summary:	Python module is useful to manipulate IP addresses (sets)
Summary(pl.UTF-8):	Moduł języka Python do manipulacji adresami IP
Name:		python-%{module}
Version:	2.1.9
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://ipaddr-py.googlecode.com/files/%{module}-%{version}.tar.gz
# Source0-md5:	c8943c95fdf0d7d99bc26b484e1bbd99
URL:		http://code.google.com/p/ipaddr-py/
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
%pyrequires_eq 	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is useful if you need to manipulate IP addresses or sets
of IP addresses.

%description -l pl.UTF-8
Moduł języka Python do manipulacji adresami IP.

%prep
%setup -q -n %{module}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}
install *.py $RPM_BUILD_ROOT%{py_sitedir}

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitedir}/*.py[co]
