Summary:	netstat-nat displays NAT connections
Summary(pl.UTF-8):   Program wyświetlający połączenia NAT
Name:		netstat-nat
Version:	1.4.7
Release:	1
License:	GPL
Group:		Networking/Utilities
Vendor:		D.Wijsman <mardan@tweegy.demon.nl>
Source0:	http://tweegy.demon.nl/download/%{name}-%{version}.tar.gz
# Source0-md5:	46bccc302288da7ebd4f0f3dadf1fad9
URL:		http://tweegy.demon.nl/projects/netstat-nat/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Netstat-nat is a small program written in C. It displays NAT
connections, managed by netfilter/iptables which comes with the >=
2.4.x Linux kernels. The program reads its information from
'/proc/net/ip_conntrack', which is the temporary conntrack-storage of
netfilter. (http://netfilter.samba.org/) Netstat-nat takes several
arguments (but not needed).

%description -l pl.UTF-8
Netstat-nat to mały program napisany w C. Wyświetla połączenia NAT,
obsługiwane przez netfilter/iptables obecne w jądrach Linuksa >=
2.4.x. Program czyta informacje z /proc/net/ip_conntrack, gdzie
netfilter umieszcza dane o śledzonych połączeniach
(http://netfilter.samba.org/). Netstat-nat może być wywoływany z
kilkoma parametrami, ale nie są one obowiązkowe.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
