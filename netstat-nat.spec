Summary:	netstat-nat displays NAT connections
Name:		netstat-nat
Version:	1.4.1
Release:	1
License:	GPL
Group:		Networking/Utilities
Vendor:		D.Wijsman <mardan@tweegy.demon.nl>
Source0:	http://tweegy.demon.nl/download/%{name}-%{version}.tar.gz
URL:		http://tweegy.demon.nl/projects/netstat-nat/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netstat-nat is a small program written in C. It displays NAT
connections, managed by netfilter/iptables which comes with the >
2.4.x linux kernels. The program reads its information from
'/proc/net/ip_conntrack', which is the temporary conntrack-storage of
netfilter. (http://netfilter.samba.org/) Netstat-nat takes several
arguments (but not needed).

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} %{buildroot}%{_bindir}/%{name}
install -D -m 444 netstat-nat.1 %{buildroot}%{_mandir}/man1/netstat-nat.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%doc README AUTHORS CHANGELOG
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
