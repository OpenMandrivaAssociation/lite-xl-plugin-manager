# set to nil when packaging a release, 
# or the long commit tag for the specific git branch
%global commit_tag %{nil}

# set with the commit date only if commit_tag not nil 
# git version (i.e. master) in format date +Ymd
%if "%{commit_tag}" != "%{nil}"
%global commit_date %(git show -s --date=format:'%Y%m%d' %{commit_tag})
%endif

%global debug_package %{nil}

Name:           lite-xl-plugin-manager
Version:        1.4.5
Release:        1
Summary:        A lite-xl plugin manager.
Group:          Development
License:        MIT
URL:            https://github.com/lite-xl/lite-xl-plugin-manager

# change the source URL depending on if the package is a release version or a git version
%if "%{commit_tag}" != "%{nil}"
Source0:        %{url}/archive/%{commit_tag}.tar.gz#/%{name}-%{version}.tar.x
%else
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif

BuildRequires:  pkgconfig(liblzma)
BuildRequires:  lib64git2-devel
BuildRequires:  lib64mbedtls-devel
BuildRequires:  lib64z-devel
BuildRequires:  lib64zip-devel
BuildRequires:  lib64lua-devel
BuildRequires:  meson

Requires:       lite-xl

%description
A standalone binary that provides an easy way of installing, 
and uninstalling plugins from lite-xl, as well as different version of lite-xl.

%prep
%autosetup -p1
CFLAGS="%{?optflags} -DLPM_DEFAULT_RELEASE=%{nil}" \
%meson -Dstatic=true 

%build
%meson_build -C build

%check
#./lpm test t/run.lua

%install
install -m 755 -D %{_builddir}/%{name}-%{version}/build/lpm %{buildroot}/%{_bindir}/lpm
install -m 644 -D %{_builddir}/%{name}-%{version}/plugins/welcome.lua %{buildroot}/%{_datadir}/lite-xl/plugins/welcome.lua
install -m 644 -D %{_builddir}/%{name}-%{version}/plugins/plugin_manager/init.lua %{buildroot}/%{_datadir}/lite-xl/plugins/plugin_manager/init.lua
install -m 644 -D %{_builddir}/%{name}-%{version}/plugins/plugin_manager/plugin_view.lua %{buildroot}/%{_datadir}/lite-xl/plugins/plugin_manager/plugin_view.lua
install -m 644 -D %{_builddir}/%{name}-%{version}/libraries/json.lua %{buildroot}/%{_datadir}/lite-xl/libraries/json.lua

%files
%license LICENSE
%doc README.md CHANGELOG.md SPEC.md
%{_bindir}/lpm
%{_datadir}/lite-xl/plugins/*
%{_datadir}/lite-xl/libraries/*

