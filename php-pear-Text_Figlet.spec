%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	Figlet
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Render text using FIGlet fonts
Summary(pl):	%{_pearname} - Renderowanie tekstu z u¿yciem fontów FIGleta
Name:		php-pear-%{_pearname}
Version:	0.8.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8010fee97da24e69f2c1f879e92939b9
URL:		http://pear.php.net/package/Text_Figlet/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_subclass}*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%{php_pear_dir}/%{_class}/*.php
