%undefine _debugsource_packages

Name:           cosmic-session
Version:        1.0.0
Release:        0.alpha5.0
Summary:        Session manager for the COSMIC desktop environment
License:        GPL-3.0-only
Group:          Session/COSMIC
URL:            https://github.com/pop-os/cosmic-session
Source0:        https://github.com/pop-os/cosmic-session/archive/epoch-%{version}-alpha.5/%{name}-epoch-%{version}-alpha.5.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
Patch0:         fix-justfile.patch

BuildRequires:  rust-packaging
BuildRequires:  just
Requires:       switcheroo-control

%description
%{summary}.

%prep
%autosetup -n %{name}-epoch-%{version}-alpha.5 -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE.md
%{_bindir}/%{name}
%{_bindir}/start-cosmic
%{_datadir}/applications/cosmic-mimeapps.list
%{_datadir}/wayland-sessions/cosmic.desktop
%{_prefix}/lib/systemd/user/cosmic-session.target
%dir %{_datadir}/wayland-sessions
