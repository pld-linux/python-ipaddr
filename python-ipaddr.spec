
%define 	module	ipaddr

Summary:	Python module is useful to manipulate IP addresses (sets)
Summary(pl.UTF-8):	Moduł języka Python do operowania adresami lub zbiorami adresów IP
Name:		python-%{module}
Version:	2.1.11
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/i/ipaddr/%{module}-%{version}.tar.gz
# Source0-md5:	f2c7852f95862715f92e7d089dc3f2cf
URL:		http://code.google.com/p/ipaddr-py/
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
%{__python} setup.py build --build-base build-2

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/ipaddr.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
