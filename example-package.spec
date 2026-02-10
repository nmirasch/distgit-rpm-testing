Name:           example-package
Version:        1.0.0
Release:        1%{?dist}
Summary:        An example package for dist-git RPM testing

License:        MIT
URL:            https://github.com/nmirasch/distgit-rpm-testing
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

%description
This is an example package used to demonstrate dist-git repository
structure for RPM package generation.

%prep
%setup -q

%build
# Nothing to build for this example

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -p README.txt %{buildroot}%{_datadir}/%{name}/

%files
%{_datadir}/%{name}/README.txt

%changelog
* Mon Feb 10 2025 Dist-git Testing <test@example.com> - 1.0.0-1
- Initial package release
