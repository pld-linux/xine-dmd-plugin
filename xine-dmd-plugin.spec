# NOTE: requires update to xine 1.0b API
Summary:	DVD input plugin for Xine
Summary(pl.UTF-8):	Plugin odczytu DVD dla Xine
Name:		xine-dmd-plugin
Version:	1.0.7
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.geocities.com/xinedvdplugin/%(echo %{name} | tr - _)-%{version}.tar.gz
# Source0-md5:	ddf5803249e30d16a8e77154bec93ae9
URL:		http://www.geocities.com/xinedvdplugin/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRequires:	xine-lib-devel >= 0.9.13
%requires_eq	xine-lib
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_pluginsdir	%(xine-config --plugindir)

%description
The name of this plugin is dmd (digital movie disc). With this plugin,
you will be able to watch all what is possible to watch on a DVD. An
other interesting feature is that you can watch multiangle DVD.

%description -l pl.UTF-8
Nazwa tej wtyczki to dmd (digital movie disc). Ta wtyczka pozwala
oglądać wszystko to, co można oglądać na DVD.

%prep
%setup -qn %(echo %{name} | sed s/-/_/g)-%{version}

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	XINE_PLUGINDIR=%{_pluginsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_pluginsdir}/*.so
