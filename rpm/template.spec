Name:           ros-melodic-wiimote
Version:        1.12.0
Release:        0%{?dist}
Summary:        ROS wiimote package

Group:          Development/Libraries
License:        GPL
URL:            http://www.ros.org/wiki/wiimote
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       cwiid
Requires:       numpy
Requires:       ros-melodic-genmsg
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-roslib
Requires:       ros-melodic-rospy
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
BuildRequires:  cwiid
BuildRequires:  cwiid-devel
BuildRequires:  numpy
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-genmsg
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roslib
BuildRequires:  ros-melodic-roslint
BuildRequires:  ros-melodic-rospy
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs

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
* Mon Jun 11 2018 Jonathan Bohren <jbo@jhu.edu> - 1.12.0-0
- Autogenerated by Bloom

