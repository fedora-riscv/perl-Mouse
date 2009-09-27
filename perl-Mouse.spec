Name:       perl-Mouse
Version:    0.35
Release:    1%{?dist}
License:    GPL+ or Artistic
Group:      Development/Libraries
Summary:    Moose minus the antlers
Source:     http://search.cpan.org/CPAN/authors/id/G/GF/GFUJI/Mouse-%{version}.tar.gz
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
BuildRequires: perl(Test::Exception) >= 0.27
BuildRequires: perl(Test::More) >= 0.88

# "soft requires"
BuildRequires: perl(MRO::Compat)

%{?perl_default_filter}

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

find .           -type f -exec chmod -c -x {} +
find t/          -type f -exec perl -pi -e 's|^#!perl|#!%{__perl}|' {} +
find benchmarks/ -type f -exec perl -pi -e 's|^#!perl|#!%{__perl}|' {} +

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
%doc Changes benchmarks/ t/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.35-1
- update filtering
- drop our soft-requires (except 1).  Anything using Mouse by this point
  should know to require them if their bits are needed.
- add benchmarks/ to doc
- auto-update to 0.35 (by cpan-spec-update 0.01)
- altered br on perl(Test::Exception) (0.21 => 0.27)
- altered br on perl(Test::More) (0.8 => 0.88)

* Sat Sep 19 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.28-1
- auto-update to 0.28 (by cpan-spec-update 0.01)

* Fri Jul 31 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.27-1
- auto-update to 0.27 (by cpan-spec-update 0.01)

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
