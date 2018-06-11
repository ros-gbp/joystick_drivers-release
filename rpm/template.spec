Name:           ros-lunar-joystick-drivers
Version:        1.12.0
Release:        0%{?dist}
Summary:        ROS joystick_drivers package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/joystick_drivers
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-lunar-joy
Requires:       ros-lunar-ps3joy
Requires:       ros-lunar-spacenav-node
Requires:       ros-lunar-wiimote
BuildRequires:  ros-lunar-catkin

%description
This metapackage depends on packages for interfacing common joysticks and human
input devices with ROS.

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
* Mon Jun 11 2018 Jonathan Bohren <jbo@jhu.edu> - 1.12.0-0
- Autogenerated by Bloom

* Wed Aug 23 2017 Jonathan Bohren <jbo@jhu.edu> - 1.11.0-0
- Autogenerated by Bloom

