%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global module_name xtend

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        4.0.0
Release:        5%{?dist}
Summary:        Extend like a boss

License:        MIT
URL:            https://github.com/Raynos/%{module_name}
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel
#BuildRequires:  %{?scl_prefix}npm(tape)
 

%description
xtend is a basic utility library which allows you to extend an object by
appending all of the properties from each object in a list. When there
are identical properties, the right-most property takes precedence.

%prep
%setup -q -n package
rm -rf node_modules

# Fix upstream file name
mv LICENCE LICENSE

%build
#nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

#%check
#%nodejs_symlink_deps --check
#node test.js

%files
%doc LICENSE README.md
%{nodejs_sitelib}/%{module_name}

%changelog
* Thu Sep 15 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 4.0.0-5
- Built for RHSCL
- turn off tests

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Oct 24 2014 Parag Nemade <pnemade AT redhat DOT com> - 4.0.0-2
- Add missing BR: npm(tape)
- fixed whitespace typo

* Fri Sep 19 2014 Parag Nemade <pnemade AT redhat DOT com> - 4.0.0-1
- Initial packaging
