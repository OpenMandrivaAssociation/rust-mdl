# Generated by rust2rpm
%bcond_with check
%global debug_package %{nil}

%global crate mdl

Name:           rust-%{crate}
Version:        1.0.4
Release:        3%{?dist}
Summary:        Data model library to share app state between threads and process

# Upstream license specification: GPL-3.0
# https://gitlab.gnome.org/danigm/mdl/issues/2
License:        GPLv3
URL:            https://crates.io/crates/mdl
Source:         %{crates_source}
# Initial patched metadata
# * Exclude unneeded files, https://gitlab.gnome.org/danigm/mdl/merge_requests/1
Patch0:         mdl-fix-metadata.diff

ExclusiveArch:  %{rust_arches}

BuildRequires:  rust-packaging
BuildRequires:  (crate(bincode/default) >= 1.0.1 with crate(bincode/default) < 2.0.0)
BuildRequires:  (crate(failure/default) >= 0.1.2 with crate(failure/default) < 0.2.0)
BuildRequires:  (crate(lmdb/default) >= 0.8.0 with crate(lmdb/default) < 0.9.0)
BuildRequires:  (crate(serde/default) >= 1.0.79 with crate(serde/default) < 2.0.0)
BuildRequires:  (crate(serde_derive/default) >= 1.0.79 with crate(serde_derive/default) < 2.0.0)

%global _description \
Data model library to share app state between threads and process and persist\
the data in the filesystem. Implements a simple way to store structs instances\
in a LMDB database and other methods like BTreeMap.

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Apr 28 19:13:40 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.4-1
- Initial package
