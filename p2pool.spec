%global debug_package %{nil}

Name:		p2pool
Version:	3.10
Release:	2%{?dist}
Summary:	Decentralized pool for Monero mining

License:	GPL-3.0-only
URL:		https://p2pool.io
Source0:	https://github.com/SChernykh/%{name}/releases/download/v%{version}/%{name}_source.tar.xz

BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	libcurl-devel
BuildRequires:	libsodium-devel
BuildRequires:	libstdc++-static
BuildRequires:	libuv-devel
BuildRequires:	openpgm-devel
BuildRequires:	zeromq-devel

%description
Decentralized pool for Monero mining

%prep
%autosetup -n %{name}
%{set_build_flags}
mkdir build && cd build
cmake ..

%build
cd build
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 build/p2pool %{buildroot}%{_bindir}/p2pool

%files
%license LICENSE
%{_bindir}/p2pool

%changelog
* Thu Feb 29 2024 zpc <dev@zpc.st>
- rebuild
* Fri Jan 05 2024 zpc <dev@zpc.st>
- version 3.10
* Mon Nov 27 2023 zpc <dev@zpc.st>
- version 3.9
* Sat Nov 11 2023 zpc <dev@zpc.st>
- initial release.
