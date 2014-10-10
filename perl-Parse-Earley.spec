%define upstream_name    Parse-Earley
%define upstream_version 0.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Parse::Earley - Parse any Context-Free Grammar
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Parse::Earley accepts or rejects a string based on any Context-Free grammar,
specified by a simplified yacc-like specification.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Parse/Earley.pm
%{_mandir}/*/*

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.0
+ Revision: 404285
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.15-5mdv2009.0
+ Revision: 258190
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.15-4mdv2009.0
+ Revision: 246267
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.15-2mdv2008.1
+ Revision: 136330
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-2mdv2008.0
+ Revision: 86767
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.15-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.15-1mdk
- initial Mandriva package

