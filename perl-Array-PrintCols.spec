#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Array
%define	pnam	PrintCols
Summary:	Array::PrintCols - print or format array elements in vertically sorted columns
Summary(pl):	Array::PrintCols - formatowanie tablicy w pionowo posortowanych kolumnach
Name:		perl-Array-PrintCols
Version:	2.1
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b8780d4eda58c33d70c0999232c633bd
Patch0:		%{name}-fix.patch
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Array::PrintCols defines a subroutine to print arrays of elements in
alphabetically, vertically sorted columns.  Optional arguments can be
given to control either the width or number of the columns, the total
width of the output, and the amount of indentation.

%description -l pl
Modu³ Array::PrintCol definiuje funkcjê do wypisywania tablic
elementów alfabetycznie, w pionowych posortowanych kolumnach. Mo¿na
przekazaæ opcjonalne parametry, kontroluj±ce szeroko¶æ lub liczbê
kolumn, ca³kowit± szeroko¶æ wyj¶cia oraz liczbê wciêæ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
