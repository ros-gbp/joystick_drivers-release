Name:           ros-kinetic-ps3joy
Version:        1.11.0
Release:        0%{?dist}
Summary:        ROS ps3joy package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ps3joy
Source0:        %{name}-%{version}.tar.gz

Requires:       bluez-libs
Requires:       libusb-devel
Requires:       linuxconsoletools
Requires:       pybluez
Requires:       ros-kinetic-diagnostic-msgs
Requires:       ros-kinetic-rosgraph
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-sensor-msgs
BuildRequires:  bluez-libs
BuildRequires:  libusb-devel
BuildRequires:  linuxconsoletools
BuildRequires:  pybluez
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-diagnostic-msgs
BuildRequires:  ros-kinetic-rosgraph
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-sensor-msgs

%description
Playstation 3 SIXAXIS or DUAL SHOCK 3 joystick driver. Driver for the Sony
PlayStation 3 SIXAXIS or DUAL SHOCK 3 joysticks. In its current state, this
driver is not compatible with the use of other Bluetooth HID devices. The driver
listens for a connection on the HID ports, starts the joystick streaming data,
and passes the data to the Linux uinput device so that it shows up as a normal
joystick.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sat Feb 11 2017 Jonathan Bohren <jbo@jhu.edu> - 1.11.0-0
- Autogenerated by Bloom

* Wed May 04 2016 Jonathan Bohren <jbo@jhu.edu> - 1.10.1-0
- Autogenerated by Bloom

