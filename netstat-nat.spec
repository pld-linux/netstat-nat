Summary:	netstat-nat displays NAT connections
Summary(pl):	Program wy¶wietlaj±cy po³±czenia NAT
Name:		netstat-nat
Version:	1.4.4
Release:	1
License:	GPL
Group:		Networking/Utilities
Vendor:		D.Wijsman <mardan@tweegy.demon.nl>
Source0:	http://tweegy.demon.nl/download/%{name}-%{version}.tar.gz
# Source0-md5:	c6cb0e72a99089e5432be3891f53a419
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

%description -l pl
Netstat-nat to ma³y program napisany w C. Wy¶wietla po³±czenia NAT,
obs³ugiwane przez netfilter/iptables obecne w j±drach Linuksa 2.4.x.
Program czyta informacje z /proc/net/ip_conntrack, gdzie netfilter
umieszcza dane o ¶ledzonych po³±czeniach
(http://netfilter.samba.org/). Netstat-nat mo¿e byæ wywo³ywany z
kilkoma parametrami, ale nie s± one obowi±zkowe.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
