Summary:	DVD input plugin for Xine
Summary(pl):	Plugin odczytu DVD dla Xine
Name:		xine-dmd-plugin
Version:	1.0.2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.geocities.com/xinedvdplugin/xine_dmd_plugin_%{version}.tgz
URL:		http://www.geocities.com/xinedvdplugin/
BuildRequires:	xine-lib-devel >= 0.9.3
Requires:	xine-ui
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_pluginsdir	%{_libdir}/xine/plugins

%description
The name of this plugin is dmd (digital movie disc). With this plugin,
you will be able to watch all what is possible to watch on a DVD. An
other interesting feature is that you can watch multiangle DVD.

%description -l pl
Nazwa tej wtyczki to dmd (digital movie disc). Ta wtyczka pozwala
ogl±daæ wszystko to, co mo¿na ogl±daæ na DVD.

%prep
%setup -qn xine_dmd_plugin-%{version}

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_pluginsdir}/*
