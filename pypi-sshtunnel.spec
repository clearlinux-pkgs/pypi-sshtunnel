#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sshtunnel
Version  : 0.4.0
Release  : 20
URL      : https://files.pythonhosted.org/packages/8d/ad/4c587adf79865be268ee0b6bd52cfaa7a75d827a23ced072dc5ab554b4af/sshtunnel-0.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/8d/ad/4c587adf79865be268ee0b6bd52cfaa7a75d827a23ced072dc5ab554b4af/sshtunnel-0.4.0.tar.gz
Summary  : Pure python SSH tunnels
Group    : Development/Tools
License  : MIT
Requires: pypi-sshtunnel-bin = %{version}-%{release}
Requires: pypi-sshtunnel-license = %{version}-%{release}
Requires: pypi-sshtunnel-python = %{version}-%{release}
Requires: pypi-sshtunnel-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(paramiko)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(wheel)

%description
|pyversions| |license|

%package bin
Summary: bin components for the pypi-sshtunnel package.
Group: Binaries
Requires: pypi-sshtunnel-license = %{version}-%{release}

%description bin
bin components for the pypi-sshtunnel package.


%package license
Summary: license components for the pypi-sshtunnel package.
Group: Default

%description license
license components for the pypi-sshtunnel package.


%package python
Summary: python components for the pypi-sshtunnel package.
Group: Default
Requires: pypi-sshtunnel-python3 = %{version}-%{release}

%description python
python components for the pypi-sshtunnel package.


%package python3
Summary: python3 components for the pypi-sshtunnel package.
Group: Default
Requires: python3-core
Provides: pypi(sshtunnel)
Requires: pypi(paramiko)

%description python3
python3 components for the pypi-sshtunnel package.


%prep
%setup -q -n sshtunnel-0.4.0
cd %{_builddir}/sshtunnel-0.4.0
pushd ..
cp -a sshtunnel-0.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656369558
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
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sshtunnel
cp %{_builddir}/sshtunnel-0.4.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sshtunnel/c267ed1b26b2346424c0cb951ed6cd657ed5caba
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sshtunnel

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sshtunnel/c267ed1b26b2346424c0cb951ed6cd657ed5caba

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
