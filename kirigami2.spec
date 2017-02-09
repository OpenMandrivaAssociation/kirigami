%define major 5
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kirigami2
Version: 2.0.0
Release: 1
Source0: http://download.kde.org/%{stable}/%{name}/%{name}-%{version}.tar.xz
Summary: KDE user interface framework for mobile and convergent applications
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(KF5Plasma)

%description
Kirigami is KDE’s lightweight user interface framework for mobile and
convergent applications. It allows Qt developers to easily create
applications that run on most major mobile and desktop platforms
without modification (though adapted user interfaces for different
form-factors are supported and recommended for optimal user
experience).

It extends the touch-friendly Qt Quick Controls with larger
application building blocks, following the design philosophy
laid out in the Kirigami Human Interface Guidelines. 

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%dir %{_libdir}/cmake/KF5Kirigami2
%{_libdir}/qt5/qml/org/kde/kirigami.2
%{_libdir}/cmake/KF5Kirigami2/*.cmake
%{_libdir}/qt5/mkspecs/modules/*.pri
%lang(ast) %{_datadir}/locale/ast/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(ca) %{_datadir}/locale/ca/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(ca@valencia) %{_datadir}/locale/ca@valencia/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(cs) %{_datadir}/locale/cs/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(de) %{_datadir}/locale/de/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(en_GB) %{_datadir}/locale/en_GB/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(es) %{_datadir}/locale/es/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(fr) %{_datadir}/locale/fr/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(gl) %{_datadir}/locale/gl/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(ja) %{_datadir}/locale/ja/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(nl) %{_datadir}/locale/nl/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(nn) %{_datadir}/locale/nn/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(pt) %{_datadir}/locale/pt/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(pt_BR) %{_datadir}/locale/pt_BR/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(ru) %{_datadir}/locale/ru/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(sk) %{_datadir}/locale/sk/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(sl) %{_datadir}/locale/sl/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(sv) %{_datadir}/locale/sv/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(uk) %{_datadir}/locale/uk/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(zh_CN) %{_datadir}/locale/zh_CN/LC_MESSAGES/libkirigami2plugin_qt.qm
%lang(zh_TW) %{_datadir}/locale/zh_TW/LC_MESSAGES/libkirigami2plugin_qt.qm
