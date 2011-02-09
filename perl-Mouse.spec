Name:           perl-Mouse
Summary:        Moose minus the antlers
Version:        0.58
Release:        4%{?dist}
License:        GPL+ or Artistic
Group:          Development/Libraries
Source0:        http://search.cpan.org/CPAN/authors/id/G/GF/GFUJI/Mouse-%{version}.tar.gz 
URL:            http://search.cpan.org/dist/Mouse
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Devel::PPPort) >= 3.19
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(ExtUtils::ParseXS) >= 2.21
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Scalar::Util) >= 1.14
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::Exception) >= 0.29
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Requires) >= 0.03
BuildRequires:  perl(XSLoader) >= 0.1

Requires:       perl(Scalar::Util) >= 1.14
Requires:       perl(XSLoader) >= 0.1

%{?perl_default_filter}
%{?perl_subpackage_tests: %perl_subpackage_tests t/ .proverc }

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

echo '-r' > .proverc

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes benchmarks/ example/ tool/ 
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto
%{_mandir}/man3/*.3*

%changelog
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.58-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.58-3
- 661697 rebuild for fixing problems with vendorach/lib

* Tue May 18 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.58-2
- bump

* Mon May 17 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.58-1
- include .proverc in tests subpackage
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (0.58)

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.53-2
- Mass rebuild with perl-5.12.0 & update

* Fri Apr 16 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.53-1
- update by Fedora::App::MaintainerTools 0.006
- updating to latest GA CPAN version (0.53)
- altered br on perl(Devel::PPPort) (0 => 3.19)
- altered br on perl(ExtUtils::ParseXS) (0 => 2.21)
- altered br on perl(Test::Exception) (0 => 0.29)
- added a new br on perl(Test::Requires) (version 0.03)
- added manual BR on perl(Class::Method::Modifiers) (or override to 0)
- added manual BR on perl(Test::Deep) (or override to 0)
- added manual BR on perl(Test::Output) (or override to 0)
- added manual BR on perl(Path::Class) (or override to 0)
- added manual BR on perl(IO::File) (or override to 0)
- added manual BR on perl(IO::String) (or override to 0)

* Sun Feb 28 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.50-1
- update by Fedora::App::MaintainerTools 0.004
- PERL_INSTALL_ROOT => DESTDIR

* Wed Jan 20 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.47-1
- add perl_default_filter
- we're no longer noarch
- auto-update to 0.47 (by cpan-spec-update 0.01)
- added a new br on perl(Devel::PPPort) 
- added a new br on perl(ExtUtils::ParseXS)
- added a new br on perl(XSLoader) (version 0.1)
- added a new req on perl(Scalar::Util) (version 1.14)
- added a new req on perl(XSLoader) (version 0.1)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.35-2
- rebuild against perl 5.10.1

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
