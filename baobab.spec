%define url_ver	%(echo %{version}|cut -d. -f1,2)

Summary:	Disk Usage Analyzer (aka Baobab)
Name:		baobab
Version:	3.4.1
Release:	1
License:	GPLv2+
Group:		File tools
Url:		http://live.gnome.org/GnomeUtils/Baobab
Source0:	http://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	itstool
BuildRequires:	intltool
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(glib-2.0) >= 2.30.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:	pkgconfig(libgtop-2.0)
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
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

for l in C cs da de el en_GB es eu fi gl hu it oc pl pt_BR ru sl sv uk zh_CN zh_HK zh_TW; do
	echo "%%dir %%{_datadir}/help/$l"
	echo "%%lang($l) %%{_datadir}/help/$l/%%{name}"
done >> %{name}.lang

%files -f %{name}.lang
%doc README NEWS AUTHORS TODO ChangeLog
%{_bindir}/baobab
%{_datadir}/baobab/
%{_datadir}/glib-2.0/schemas/org.gnome.baobab.gschema.xml
%{_datadir}/applications/baobab.desktop
%{_datadir}/icons/hicolor/*/apps/baobab.png
%{_mandir}/man1/baobab.1.*

