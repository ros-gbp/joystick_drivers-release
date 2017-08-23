Name:           ros-lunar-joy
Version:        1.11.0
Release:        0%{?dist}
Summary:        ROS joy package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/joy
Source0:        %{name}-%{version}.tar.gz

Requires:       linuxconsoletools
Requires:       ros-lunar-diagnostic-updater
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-sensor-msgs
BuildRequires:  linuxconsoletools
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-diagnostic-updater
BuildRequires:  ros-lunar-rosbag
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-sensor-msgs

%description
ROS driver for a generic Linux joystick. The joy package contains joy_node, a
node that interfaces a generic Linux joystick to ROS. This node publishes a
&quot;Joy&quot; message, which contains the current state of each one of the
joystick's buttons and axes.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Wed Aug 23 2017 Jonathan Bohren <jbo@jhu.edu> - 1.11.0-0
- Autogenerated by Bloom

