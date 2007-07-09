Summary:	A set of tools and helper libs for Ruby Reports
Summary(pl.UTF-8):	Zestaw narzędzi i bibliotek pomocniczych dla systemu Ruby Reports
Name:		ruby-ruport-util
Version:	0.7.2
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://gems.rubyforge.org/gems/ruport-util-%{version}.gem
# Source0-md5:	574309d449f221b736f60dbcd0711b00
URL:		http://code.rubyreports.org/
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	setup.rb = 3.3.1
Requires:	ruby-ruport >= 0.11.0
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ruport-util provides a number of utilities and helper libs for Ruby
Reports.

%description -l pl.UTF-8
Ten pakiet udostępnia zestaw narzędzi i bibliotek pomocniczych dla
systemu Ruby Reports.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%attr(755,root,root) %{_bindir}/rope
%attr(755,root,root) %{_bindir}/csv2ods
%{ruby_rubylibdir}/ruport/util
%{ruby_rubylibdir}/ruport/util.rb
