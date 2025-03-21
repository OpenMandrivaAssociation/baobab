%define url_ver	%(echo %{version}|cut -d. -f1,2)

%global optflags %{optflags} -Wno-incompatible-function-pointer-types

Summary:	Disk Usage Analyzer (aka Baobab)
Name:		baobab
Version:	48.0
Release:	1
License:	GPLv2+
Group:		File tools
Url:		https://live.gnome.org/GnomeUtils/Baobab
Source0:	https://ftp.gnome.org/pub/GNOME/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	itstool
BuildRequires:	intltool
BuildRequires:	vala-tools
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(glib-2.0) >= 2.30.0
BuildRequires:	pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	meson
Conflicts:	gnome-utils < 1:3.3.1

%description
Disk Usage Analyzer is is a graphical, menu-driven application to analyze
disk usage in any Gnome environment. Disk Usage Analyzer can easily scan
either the whole file-system tree, or a specific user-requested directory
branch (local or remote).

It also auto-detects in real-time any changes made to your home directory
as far as any mounted/unmounted device. Disk Usage Analyzer also provides
a full graphical tree-map window for each selected folder.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

#we don't want these
find %{buildroot} -name '*.la' -delete

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc README.md NEWS AUTHORS
%{_bindir}/baobab
%{_datadir}/metainfo/org.gnome.baobab.metainfo.xml
%{_datadir}/applications/org.gnome.baobab.desktop
%{_datadir}/dbus-1/services/org.gnome.baobab.service
%{_datadir}/glib-2.0/schemas/org.gnome.baobab.gschema.xml
%{_datadir}/icons/hicolor/*/*/*
%{_mandir}/man1/baobab.1.*

