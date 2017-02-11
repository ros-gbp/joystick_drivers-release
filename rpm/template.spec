Name:           ros-jade-spacenav-node
Version:        1.11.0
Release:        0%{?dist}
Summary:        ROS spacenav_node package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/spacenav_node
Source0:        %{name}-%{version}.tar.gz

Requires:       libX11-devel
Requires:       libspnav-devel
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       spacenavd
BuildRequires:  libX11-devel
BuildRequires:  libspnav-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs

%description
ROS interface to the 3Dconnexion SpaceNavigator 6DOF joystick.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sat Feb 11 2017 Jonathan Bohren <jbo@jhu.edu> - 1.11.0-0
- Autogenerated by Bloom

* Sun May 24 2015 Jonathan Bohren <jbo@jhu.edu> - 1.10.1-0
- Autogenerated by Bloom

