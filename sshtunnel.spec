#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sshtunnel
Version  : 0.1.5
Release  : 4
URL      : https://files.pythonhosted.org/packages/c5/5c/4b320d7ec4b0d5d4d6df1fdf66a5799625b3623d0ce4efe81719c6f8dfb3/sshtunnel-0.1.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/c5/5c/4b320d7ec4b0d5d4d6df1fdf66a5799625b3623d0ce4efe81719c6f8dfb3/sshtunnel-0.1.5.tar.gz
Summary  : Pure python SSH tunnels
Group    : Development/Tools
License  : MIT
Requires: sshtunnel-bin = %{version}-%{release}
Requires: sshtunnel-python = %{version}-%{release}
Requires: sshtunnel-python3 = %{version}-%{release}
Requires: Sphinx
Requires: paramiko
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : paramiko
BuildRequires : paramiko-python
BuildRequires : tox
BuildRequires : tox-python

%description
|pyversions| |license|

%package bin
Summary: bin components for the sshtunnel package.
Group: Binaries

%description bin
bin components for the sshtunnel package.


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
%setup -q -n sshtunnel-0.1.5
cd %{_builddir}/sshtunnel-0.1.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588710753
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sshtunnel

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
