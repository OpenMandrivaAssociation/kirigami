%define major 5
%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
%define libname %mklibname KF5Kirigami2 5
%define devname %mklibname -d KF5Kirigami2

Name: kirigami
Version: 5.93.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version}|cut -d. -f1-2)/%{name}2-%{version}.tar.xz
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
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: qt5-qtgraphicaleffects
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant
Requires: %{libname} = %{EVRD}
Requires: qt5-qtquickcontrols
Requires: qt5-qtgraphicaleffects
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

%package -n %{libname}
Summary: Libraries for Kirigami
Group: System/Libraries
Requires: %{name} = %{EVRD}
%rename %{_lib}kf5kirigami2_5

%description -n %{libname}
Libraries for Kirigami.

%files -n %{libname}
%{_libdir}/libKF5Kirigami2.so.*

%package -n %{devname}
Summary: Development files for Kirigami
Group: Development/KDE and Qt
Requires: %{libname} = %{EVRD}
Provides: kirigami-devel = %{EVRD}
%rename %{_lib}kf5kirigami2-devel

%description -n %{devname}
Development files for Kirigami.

%package -n %{name}-devel-docs
Summary: Developer documentation for %{name} for use with Qt Assistant
Group: Documentation
Suggests: %{devname} = %{EVRD}

%description -n %{name}-devel-docs
Developer documentation for %{name} for use with Qt Assistant

%files -n %{devname}
%dir %{_libdir}/cmake/KF5Kirigami2
%{_libdir}/libKF5Kirigami2.so
%{_includedir}/KF5/Kirigami2
%{_libdir}/cmake/KF5Kirigami2/*.cmake
%{_libdir}/qt5/mkspecs/modules/*.pri
%{_datadir}/kdevappwizard/templates/kirigami.tar.bz2

%prep
%autosetup -p1 -n %{name}2-%{version}
%cmake_kde5 -G "Unix Makefiles"

%build
%make_build -C build

%install
%make_install -C build
TOP="$(pwd)"
cd %{buildroot}
for i in .%{_datadir}/locale/*/*/*.qm; do
	echo "%%lang($(echo $i |cut -d/ -f5)) $(echo $i |cut -b2-)" >>${TOP}/translations.lang
done

%files -f translations.lang
%{_libdir}/qt5/qml/org/kde/kirigami.2

%files -n %{name}-devel-docs
%{_docdir}/qt5/*.{tags,qch}
