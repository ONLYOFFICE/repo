Name:           %{_package_name}
Version:        %{_product_version}
Release:        %{_build_number}
Summary:        ONLYOFFICE repository configuration

Group:          System Environment/Base
License:        AGPL

URL:            https://github.com/ONLYOFFICE/repo/tree/master/centos

BuildArch:     noarch

Vendor: ONLYOFFICE
Packager: ONLYOFFICE <support@onlyoffice.com>

%description
This package contains the ONLYOFFICE repository
GPG key as well as configuration for yum.

%prep
rm -rf "%{buildroot}"

%build

%install
mkdir -p %{buildroot}/etc/yum.repos.d
install -pm 755 ../../onlyoffice.repo %{buildroot}/etc/yum.repos.d

#GPG Key
install -Dpm 644 ../../RPM-GPG-KEY-ONLYOFFICE \
    %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-ONLYOFFICE

%clean
rm -rf "%{buildroot}"

%files
%config %attr(-, root, root) /etc/yum.repos.d/onlyoffice.repo
%config(noreplace) /etc/pki/rpm-gpg/*

%pre

%post

%preun

%postun

%changelog
* Fri Nov 21 2017 ONLYOFFICE <support@onlyoffice.com>
- Initial release.
