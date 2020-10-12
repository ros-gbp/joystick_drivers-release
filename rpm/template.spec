%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-ps3joy
Version:        1.15.0
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ps3joy package

License:        BSD
URL:            http://www.ros.org/wiki/ps3joy
Source0:        %{name}-%{version}.tar.gz

Requires:       bluez-libs
Requires:       libusb-devel
Requires:       linuxconsoletools
Requires:       pybluez
Requires:       ros-noetic-diagnostic-msgs
Requires:       ros-noetic-rosgraph
Requires:       ros-noetic-rospy
Requires:       ros-noetic-sensor-msgs
BuildRequires:  bluez-libs
BuildRequires:  libusb-devel
BuildRequires:  linuxconsoletools
BuildRequires:  pybluez
BuildRequires:  ros-noetic-catkin
BuildRequires:  ros-noetic-diagnostic-msgs
BuildRequires:  ros-noetic-rosgraph
BuildRequires:  ros-noetic-roslint
BuildRequires:  ros-noetic-rospy
BuildRequires:  ros-noetic-sensor-msgs
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Playstation 3 SIXAXIS or DUAL SHOCK 3 joystick driver. Driver for the Sony
PlayStation 3 SIXAXIS or DUAL SHOCK 3 joysticks. In its current state, this
driver is not compatible with the use of other Bluetooth HID devices. The driver
listens for a connection on the HID ports, starts the joystick streaming data,
and passes the data to the Linux uinput device so that it shows up as a normal
joystick.

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
* Mon Oct 12 2020 Jonathan Bohren <jbo@jhu.edu> - 1.15.0-1
- Autogenerated by Bloom

* Tue Jul 07 2020 Jonathan Bohren <jbo@jhu.edu> - 1.14.0-1
- Autogenerated by Bloom

