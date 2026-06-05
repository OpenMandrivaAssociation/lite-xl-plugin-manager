Name:           lite-xl-plugin-manager
Version:        1.4.7
Release:        1
Summary:        A lite-xl plugin manager.
Group:          Development
License:        MIT
URL:            https://github.com/lite-xl/lite-xl-plugin-manager

Source0:        %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:    meson

BuildOption:    -Dstatic=true

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

%conf -p
CFLAGS="%{?optflags} -DLPM_DEFAULT_RELEASE=%{nil}" 

%install -a
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

