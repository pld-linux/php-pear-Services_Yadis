%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Services_Yadis
Summary:	%{_pearname} - Implementation of the Yadis Specification 1.0 protocol for PHP5
Summary(pl.UTF-8):	%{_pearname} - Implementacja protokołu Yadis 1.0 dla PHP5
Name:		php-pear-%{_pearname}
Version:	0.4.0
Release:	2
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8ec981bf2ecfc5db4050eeec6c61b94e
URL:		http://pear.php.net/package/Services_Yadis/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-date
Requires:	php-dom
Requires:	php-pear
Requires:	php-pear-HTTP_Request2 >= 0.5.1
Requires:	php-pear-Net_URL2
Requires:	php-pear-PEAR-core >= 1:1.3.6
Requires:	php-pear-Validate
Requires:	php-simplexml
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Implementation of the Yadis Specification 1.0 protocol allowing a
client to discover a list of Services a Yadis Identity Provider
offers.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten dostarcza implementację protokołu Yadis 1.0 umożliwiającego
klientowi na rozpoznanie usług udostępnianych przez dostawcę
tożsamości Yadis.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/Yadis
%{php_pear_dir}/Services/Yadis.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/%{_pearname}
