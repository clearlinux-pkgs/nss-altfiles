#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nss-altfiles
Version  : 2.23.0
Release  : 124
URL      : https://github.com/aperezdc/nss-altfiles/archive/v2.23.0.tar.gz
Source0  : https://github.com/aperezdc/nss-altfiles/archive/v2.23.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: nss-altfiles-lib = %{version}-%{release}
Requires: nss-altfiles-license = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
Patch1: build.patch
Patch2: remove-res-use-net6-use.patch

%description
NSS altfiles module
===================
[![Build Status](https://drone.io/github.com/aperezdc/nss-altfiles/status.png)](https://drone.io/github.com/aperezdc/nss-altfiles/latest)

%package lib
Summary: lib components for the nss-altfiles package.
Group: Libraries
Requires: nss-altfiles-license = %{version}-%{release}

%description lib
lib components for the nss-altfiles package.


%package lib32
Summary: lib32 components for the nss-altfiles package.
Group: Default
Requires: nss-altfiles-license = %{version}-%{release}

%description lib32
lib32 components for the nss-altfiles package.


%package license
Summary: license components for the nss-altfiles package.
Group: Default

%description license
license components for the nss-altfiles package.


%prep
%setup -q -n nss-altfiles-2.23.0
cd %{_builddir}/nss-altfiles-2.23.0
%patch1 -p1
%patch2 -p1
pushd ..
cp -a nss-altfiles-2.23.0 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605555430
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static --datadir=/usr/share/defaults/etc \
--with-types=all
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static --datadir=/usr/share/defaults/etc \
--with-types=all   --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%install
export SOURCE_DATE_EPOCH=1605555430
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nss-altfiles
cp %{_builddir}/nss-altfiles-2.23.0/COPYING %{buildroot}/usr/share/package-licenses/nss-altfiles/de286744d1c4c25dda24eff0d74f9dda45573722
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/libnss_altfiles.so.2

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libnss_altfiles.so.2

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nss-altfiles/de286744d1c4c25dda24eff0d74f9dda45573722
