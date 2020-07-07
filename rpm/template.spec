%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-wiimote
Version:        1.14.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS wiimote package

License:        GPL
URL:            http://www.ros.org/wiki/wiimote
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       cwiid-devel
Requires:       python3-numpy
Requires:       ros-noetic-geometry-msgs
Requires:       ros-noetic-message-runtime
Requires:       ros-noetic-roscpp
Requires:       ros-noetic-roslib
Requires:       ros-noetic-rospy
Requires:       ros-noetic-sensor-msgs
Requires:       ros-noetic-std-msgs
Requires:       ros-noetic-std-srvs
BuildRequires:  cwiid-devel
BuildRequires:  python3-numpy
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-geometry-msgs
BuildRequires:  ros-noetic-message-generation
BuildRequires:  ros-noetic-roscpp
BuildRequires:  ros-noetic-roslib
BuildRequires:  ros-noetic-roslint
BuildRequires:  ros-noetic-rospy
BuildRequires:  ros-noetic-sensor-msgs
BuildRequires:  ros-noetic-std-msgs
BuildRequires:  ros-noetic-std-srvs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
The wiimote package allows ROS nodes to communicate with a Nintendo Wiimote and
its related peripherals, including the Nunchuk, Motion Plus, and
(experimentally) the Classic. The package implements a ROS node that uses
Bluetooth to communicate with the Wiimote device, obtaining accelerometer and
gyro data, the state of LEDs, the IR camera, rumble (vibrator), buttons,
joystick, and battery state. The node additionally enables ROS nodes to control
the Wiimote's LEDs and vibration for feedback to the human Wiimote operator.
LEDs and vibration may be switched on and off, or made to operate according to a
timed pattern.

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Tue Jul 07 2020 Jonathan Bohren <jbo@jhu.edu> - 1.14.0-1
- Autogenerated by Bloom

