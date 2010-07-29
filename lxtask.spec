Summary:	Lightweight task manager
Name:		lxtask
Version:	0.1.3
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.gz
# Source0-md5:	eccfb69ee1a209248b22a5f0a34a4734
URL:		http://www.lxde.org/
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXTask - lightweight and desktop-independent task manager derived from
xfce4-taskmanager with all dependencies on xfce removed, new features,
and some improvement of the user interface.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/{frp,ur_PK}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/lxtask
%{_desktopdir}/lxtask.desktop
