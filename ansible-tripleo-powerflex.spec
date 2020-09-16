%global srcname tripleo_powerflex
%global rolename tripleo-powerflex

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

Name:           ansible-%{rolename}
Version:        XXX
Release:        XXX
Summary:        Ansible role for setting up PowerFlex for TripleO

Group:          System Environment/Base
License:        ASL 2.0
URL:            https://github.com/dell/tripleo-powerflex
Source0:        https://tarballs.openstack.org/%{rolename}/%{rolename}-%{upstream_version}.tar.gz

BuildArch:      noarch
BuildRequires:  git

Requires:       python3dist(ansible)

%description

Ansible role to configure PowerFlex for TripleO

%prep
%autosetup -n %{rolename}-%{upstream_version} -S git


%build
%{py3_build}


%install
export PBR_VERSION=%{version}
export SKIP_PIP_INSTALL=1


%files
%doc README*
%license LICENSE
%{python3_sitelib}/%{srcname}-*.egg-info
%{_datadir}/ansible/roles/


%changelog

