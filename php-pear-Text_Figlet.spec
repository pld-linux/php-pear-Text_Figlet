%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	Figlet
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Render text using FIGlet fonts
Summary(pl):	%{_pearname} - Renderowanie tekstu z u¿yciem fontów FIGleta
Name:		php-pear-%{_pearname}
Version:	0.8.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	843d3307b9483703b32e441243d775a5
URL:		http://pear.php.net/package/Text_Figlet/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.0.4+
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Engine for use FIGlet fonts to rendering text.

In PEAR status of this package is: %{_status}.

%description -l pl
Silnik do renderowania tekstu z u¿yciem fontów FIGleta.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

install -d docs/%{_pearname}
mv ./%{php_pear_dir}/data/%{_pearname}/docs/* docs/%{_pearname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/{docs/*,examples}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
