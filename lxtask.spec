#
# Conditional build:
%bcond_with	gtk3	# use GTK+3 instead of GTK+2

Summary:	Lightweight task manager
Summary(pl.UTF-8):	Lekki zarządca zadań
Name:		lxtask
Version:	0.1.10
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	https://downloads.sourceforge.net/lxde/%{name}-%{version}.tar.xz
# Source0-md5:	27b5258847afc237a5b89666e7a8b45b
URL:		http://www.lxde.org/
BuildRequires:	gettext-tools
%{!?with_gtk3:BuildRequires:	gtk+2-devel >= 2:2.12.0}
%{?with_gtk3:BuildRequires:	gtk+3-devel >= 3.0.0}
BuildRequires:	intltool
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%{!?with_gtk3:Requires:	gtk+2 >= 2:2.12.0}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LXTask is a lightweight and desktop-independent task manager derived
from xfce4-taskmanager with all dependencies on XFCE removed, new
features, and some improvement of the user interface.

%description -l pl.UTF-8
LXTask to lekki i niezależny od środowiska zarządca zadań, wywodzący
się z pakietu xfce4-taskmanager z usuniętymi zależnościami od XFCE,
nowymi możliwościami i pewnymi ulepszeniami interfejsu użytkownika.

%prep
%setup -q

%build
%configure \
	%{?with_gtk3:--enable-gtk3}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# unify name
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{tt_RU,tt}
# duplicate of ur
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ur_PK
# unsupported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/frp

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/lxtask
%{_desktopdir}/lxtask.desktop
%{_mandir}/man1/lxtask.1*
