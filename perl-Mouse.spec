Name:       perl-Mouse
Version:    0.25
Release:    2%{?dist}
License:    GPL+ or Artistic
Group:      Development/Libraries
Summary:    Moose minus the antlers
Source:     http://search.cpan.org/CPAN/authors/id/S/SA/SARTAK/Mouse-%{version}.tar.gz
Url:        http://search.cpan.org/dist/Mouse
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:   perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:  noarch

BuildRequires: perl(Class::Method::Modifiers) >= 1.01
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Scalar::Util) >= 1.14
# tests
BuildRequires: perl(Moose)
BuildRequires: perl(Test::Exception) >= 0.21
BuildRequires: perl(Test::More) >= 0.8

# Strictly speaking, since 0.09 these are "soft dependencies", that is, Mouse
# will take advantage of them (and run faster) if they're there; but can cope
# otherwise.  As they're already all in Fedora, and we don't have a
# "recommends" in rpm yet, let's manually require them here.
Requires:      perl(Class::Method::Modifiers) >= 1.01
Requires:      perl(Test::Exception)          >= 0.27
Requires:      perl(Scalar::Util)             >= 1.14
Requires:      perl(MRO::Compat)              >= 0.09


%description
Moose, a powerful metaobject-fuelled extension of the Perl 5 object system,
is wonderful.  (For more information on Moose, please see 'perldoc Moose'
after installing the perl-Moose package.)

Unfortunately, it's a little slow. Though significant progress has been
made over the years, the compile time penalty is a non-starter for some
applications.  Mouse aims to alleviate this by providing a subset of Moose's
functionality, faster.

%prep
%setup -q -n Mouse-%{version}

find t/ -type f -exec perl -pi -e 's|^#!perl|#!/usr/bin/perl|' {} +

# make sure doc/tests don't generate provides
# note we first filter out the bits in _docdir...
cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} `perl -p -e 's|%{_docdir}/%{name}-%{version}\S+||'`
EOF

%define __perl_provides %{_builddir}/Mouse-%{version}/%{name}-prov
chmod +x %{__perl_provides}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes t/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.25-1
- auto-update to 0.25 (by cpan-spec-update 0.01)
- altered req on perl(Scalar::Util) (1.19 => 1.14)

* Tue Jun 02 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.23-1
- auto-update to 0.23 (by cpan-spec-update 0.01)
- altered br on perl(Test::Exception) (0 => 0.21)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- altered br on perl(Test::More) (0 => 0.8)

* Sun May 03 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.22-1
- update to 0.22

* Thu Apr 02 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.19-1
- update to 0.19

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 22 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.17-1
- update to 0.17

* Tue Feb 10 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.16-1
- update to 0.16

* Tue Dec 30 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.14-1
- update to 0.14

* Tue Dec 16 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.13-1
- update to 0.13

* Mon Oct 06 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.09-2
- bump

* Wed Oct 01 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.09-1
- update to 0.09
- add manual requires on the "soft" dependencies

* Mon Sep 08 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.06-2
- update description a touch.

* Sat Sep 06 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.06-1
- initial Fedora packaging
- generated with cpan2dist (CPANPLUS::Dist::Fedora version 0.0.1)
