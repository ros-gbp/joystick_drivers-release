Name:           ros-indigo-wiimote
Version:        1.11.0
Release:        1%{?dist}
Summary:        ROS wiimote package

Group:          Development/Libraries
License:        GPL
URL:            http://www.ros.org/wiki/wiimote
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       cwiid
Requires:       numpy
Requires:       ros-indigo-genmsg
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-roslib
Requires:       ros-indigo-rospy
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
BuildRequires:  cwiid
BuildRequires:  cwiid-devel
BuildRequires:  numpy
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-genmsg
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-roslib
BuildRequires:  ros-indigo-roslint
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs

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
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Feb 11 2017 Jonathan Bohren <jbo@jhu.edu> - 1.11.0-1
- Autogenerated by Bloom

* Thu Jan 19 2017 Jonathan Bohren <jbo@jhu.edu> - 1.11.0-0
- Autogenerated by Bloom

* Sun May 24 2015 Jonathan Bohren <jbo@jhu.edu> - 1.10.1-0
- Autogenerated by Bloom

