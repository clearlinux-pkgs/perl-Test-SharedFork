#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-SharedFork
Version  : 0.35
Release  : 11
URL      : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-SharedFork-0.35.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-SharedFork-0.35.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libt/libtest-sharedfork-perl/libtest-sharedfork-perl_0.35-1.debian.tar.xz
Summary  : 'fork test'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0 GPL-2.0
Requires: perl-Test-SharedFork-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Requires)

%description
# NAME
Test::SharedFork - fork test
# SYNOPSIS
use Test::More tests => 200;
use Test::SharedFork;

%package dev
Summary: dev components for the perl-Test-SharedFork package.
Group: Development
Provides: perl-Test-SharedFork-devel = %{version}-%{release}

%description dev
dev components for the perl-Test-SharedFork package.


%package license
Summary: license components for the perl-Test-SharedFork package.
Group: Default

%description license
license components for the perl-Test-SharedFork package.


%prep
%setup -q -n Test-SharedFork-0.35
cd ..
%setup -q -T -D -n Test-SharedFork-0.35 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Test-SharedFork-0.35/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Test-SharedFork
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Test-SharedFork/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Test-SharedFork/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Test/SharedFork.pm
/usr/lib/perl5/vendor_perl/5.28.2/Test/SharedFork/Array.pm
/usr/lib/perl5/vendor_perl/5.28.2/Test/SharedFork/Scalar.pm
/usr/lib/perl5/vendor_perl/5.28.2/Test/SharedFork/Store.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::SharedFork.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Test-SharedFork/LICENSE
/usr/share/package-licenses/perl-Test-SharedFork/deblicense_copyright
