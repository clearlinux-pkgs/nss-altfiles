#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nss-altfiles
Version  : 2.19.2
Release  : 11
URL      : https://github.com/aperezdc/nss-altfiles/archive/v2.19.2.tar.gz
Source0  : https://github.com/aperezdc/nss-altfiles/archive/v2.19.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: nss-altfiles-lib

%description
NSS altfiles module
===================
[![Build Status](https://drone.io/github.com/aperezdc/nss-altfiles/status.png)](https://drone.io/github.com/aperezdc/nss-altfiles/latest)

%package lib
Summary: lib components for the nss-altfiles package.
Group: Libraries

%description lib
lib components for the nss-altfiles package.


%prep
%setup -q -n nss-altfiles-2.19.2

%build
%configure --disable-static --datadir=/usr/share/defaults/etc \
--with-types=all
make V=1  %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
