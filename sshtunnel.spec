#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sshtunnel
Version  : 0.4.0
Release  : 17
URL      : https://files.pythonhosted.org/packages/8d/ad/4c587adf79865be268ee0b6bd52cfaa7a75d827a23ced072dc5ab554b4af/sshtunnel-0.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/8d/ad/4c587adf79865be268ee0b6bd52cfaa7a75d827a23ced072dc5ab554b4af/sshtunnel-0.4.0.tar.gz
Summary  : Pure python SSH tunnels
Group    : Development/Tools
License  : MIT
Requires: sshtunnel-bin = %{version}-%{release}
Requires: sshtunnel-license = %{version}-%{release}
Requires: sshtunnel-python = %{version}-%{release}
Requires: sshtunnel-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(paramiko)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
|pyversions| |license|

%package bin
Summary: bin components for the sshtunnel package.
Group: Binaries
Requires: sshtunnel-license = %{version}-%{release}

%description bin
bin components for the sshtunnel package.


%package license
Summary: license components for the sshtunnel package.
Group: Default

%description license
license components for the sshtunnel package.


%package python
Summary: python components for the sshtunnel package.
Group: Default
Requires: sshtunnel-python3 = %{version}-%{release}

%description python
python components for the sshtunnel package.


%package python3
Summary: python3 components for the sshtunnel package.
Group: Default
Requires: python3-core
Provides: pypi(sshtunnel)
Requires: pypi(paramiko)

%description python3
python3 components for the sshtunnel package.


%prep
%setup -q -n sshtunnel-0.4.0
cd %{_builddir}/sshtunnel-0.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641426574
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sshtunnel
cp %{_builddir}/sshtunnel-0.4.0/LICENSE %{buildroot}/usr/share/package-licenses/sshtunnel/c267ed1b26b2346424c0cb951ed6cd657ed5caba
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sshtunnel

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sshtunnel/c267ed1b26b2346424c0cb951ed6cd657ed5caba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
