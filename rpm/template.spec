Name:           ros-melodic-openrtm-aist
Version:        1.1.2
Release:        0%{?dist}
Summary:        ROS openrtm_aist package

Group:          Development/Libraries
License:        EPL
URL:            http://ros.org/wiki/openrtm_aist
Source0:        %{name}-%{version}.tar.gz

Requires:       libuuid-devel
Requires:       omniORB
Requires:       omniORB-devel
Requires:       omniORB-servers
Requires:       ros-melodic-catkin
BuildRequires:  automake
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libuuid-devel
BuildRequires:  omniORB
BuildRequires:  omniORB-devel
BuildRequires:  omniORB-servers
BuildRequires:  pkgconfig

%description
This package represents OpenRTM-aist that's built within ROS eco system.
Although being ROS-agnostic by itself, you can use this via ROS together with
the packages in rtmros_common that bridge between two framework. OpenRTM-aist is
an RT-Middleware-baseed, component-oriented software platform to robotics
development that is made and maintained in AIST (National Institute of Advanced
Industrial Science and Technology) in Japan (excerpts from here) Its development
is happening at openrtm.org/pub/OpenRTM-aist. The repository listed below is
where the development of its ROS wrapper happening.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Wed Sep 05 2018 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 1.1.2-0
- Autogenerated by Bloom

