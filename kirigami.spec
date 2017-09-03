%define major 5
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kirigami
Version: 5.38.0
Release: 1
Source0: http://download.kde.org/%{stable}/%{name}/%{name}2-%{version}.tar.xz
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
%rename kirigami2

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
%setup -qn %{name}2-%{version}
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
TOP="$(pwd)"
cd %{buildroot}
for i in .%{_datadir}/locale/*/*/*.qm; do
	echo "%%lang($(echo $i |cut -d/ -f5)) $(echo $i |cut -b2-)" >>${TOP}/translations.lang
done

%files -f translations.lang
%dir %{_libdir}/cmake/KF5Kirigami2
%{_libdir}/qt5/qml/org/kde/kirigami.2
%{_libdir}/cmake/KF5Kirigami2/*.cmake
%{_libdir}/qt5/mkspecs/modules/*.pri
