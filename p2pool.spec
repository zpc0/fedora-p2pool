# SPDX-License-Identifier: GPL-3.0-or-later
%global debug_package %{nil}

# disable LTO to fix build problem
%global _lto_cflags %{nil}

Name:		p2pool
Version:	4.2
Release:	1%{?dist}
Summary:	Decentralized pool for Monero mining

License:	GPL-3.0-only
URL:		https://p2pool.io
Source0:	https://github.com/SChernykh/%{name}/releases/download/v%{version}/%{name}_source.tar.xz
Source1:	https://github.com/SChernykh/%{name}/releases/download/v%{version}/sha256sums.txt.asc
Source2:	SChernykh.asc

# for source tarball verification
BuildRequires:	coreutils
BuildRequires:	gnupg2

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
# check PGP signature
gpg --import %{SOURCE2}
gpg --output SChernykh-keyring.gpg --export sergey.v.chernykh@gmail.com
gpgv --keyring ./SChernykh-keyring.gpg %{SOURCE1}

# calc hashes
trusted_hash=$(sed -n '/Name:\sp2pool_source.tar.xz/,/SHA256:\s/p' %{SOURCE1} | tail -c 65 | head -c 64)
archive_hash=$(sha256sum %{SOURCE0} | head -c 64 | tr '[:lower:]' '[:upper:]')

# check against correct hash
if ! [ $trusted_hash = $archive_hash ]; then
	exit 1
fi

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
%autochangelog
