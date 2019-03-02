#
# Conditional build:
%bcond_without	tests	# unit tests

%define 	module	ipaddr

Summary:	Python module is useful to manipulate IP addresses (sets)
Summary(pl.UTF-8):	Moduł języka Python do operowania adresami lub zbiorami adresów IP
Name:		python-%{module}
Version:	2.2.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ipaddr/
Source0:	https://files.pythonhosted.org/packages/source/i/ipaddr/%{module}-%{version}.tar.gz
# Source0-md5:	f88353e40dec06410acfa075b8209b27
URL:		https://github.com/google/ipaddr-py
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python >= 2
BuildRequires:	python-modules >= 2
BuildRequires:	rpm-pythonprov
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is useful if you need to manipulate IP addresses or sets
of IP addresses.

%description -l pl.UTF-8
Moduł języka Python do operowania adresami lub zbiorami adresów IP.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%if %{with tests}
%{__python} ipaddr_test.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/ipaddr.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
