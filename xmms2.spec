Summary:	Client/server based media player system
Name:		xmms2
Version:	0.1
%define	_dr	1.1
Release:	0.DR%{_dr}.0.1
License:	LGPL v2.1
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/xmms2/%{name}-%{version}DR%{_dr}.tar.gz
URL:		http://xmms2.xmms.se/
BuildRequires:	SDL-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	curl-devel
BuildRequires:	ecore-devel
BuildRequires:	flac-devel
BuildRequires:	glib-devel >= 2.2.0
BuildRequires:	gnome-vfs2-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libmad-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libvorbis-devel
BuildRequires:	python-Pyrex
BuildRequires:	python-devel
BuildRequires:	ruby
BuildRequires:	scons >= 0.94
BuildRequires:	speex-devel
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_rubyarchdir	%(ruby -r rbconfig -e 'print Config::CONFIG["sitearchdir"]')

%description
This package contains the daemon that loads plugins and allows clients
to connect.

%package client-cli
Summary:	Simple text-ui for xmms2
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description client-cli
Simple text-ui for xmms2.

%package client-sdlvis
Summary:	Simple SDL visualization client for xmms2
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description client-sdlvis
Simple SDL visualization client for xmms2.

%package client-lib-ecore
Summary:	ecore client library
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description client-lib-ecore
ecore client library.

%package client-lib-ecore-ruby
Summary:	Ruby bindings for the xmms2 ecore client library
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-client-lib-ecore = %{version}-%{release}

%description client-lib-ecore-ruby
Ruby bindings for the xmms2 ecore client library.

%package client-lib-glib
Summary:	GLib client library
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description client-lib-glib
GLib client library.

%package client-lib-glib-ruby
Summary:	Ruby bindings for the xmms2 GLib client library
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-client-lib-glib = %{version}-%{release}

%description client-lib-glib-ruby
Ruby bindings for the xmms2 GLib client library.

%package client-lib-python
Summary:	XMMS2 Python bindings
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description client-lib-python
Python bindings for the xmms2 clientlib.

%package client-lib-ruby
Summary:	Ruby bindings for the XMMS2 client library
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description client-lib-ruby
Ruby bindings for the xmms2 client library.

%package input-cd
Summary:	CD transport and decoder
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-cd
This package enables direct reading of CDs for xmms2.

%package input-flac
Summary:	FLAC decorer
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-flac
This package enables flac decoding for xmms2.

%package input-mad
Summary:	mad-based mp3 decoder
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-mad
This package enables mp3 decoding for xmms2.

%package input-modplug
Summary:	mod decoder
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-modplug
This package enables modplug decoding for xmms2.

%package input-sid
Summary:	sid decoder
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-sid
This package enables sid decoding for xmms2.

%package input-speex
Summary:	speex decoder
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-speex
This package enables speex decoding for xmms2.

%package input-vorbis
Summary:	vorbis decoder
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-vorbis
This package enables ogg-vorbis decoding for xmms2.

%package input-wav
Summary:	wav decoder
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-wav
This package enables wav decoding for xmms2.

%package output-alsa
Summary:	ALSA output
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description output-alsa
This package enables ALSA output for xmms2.

%package output-jack
Summary:	JACK output
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description output-jack
This package enables JACK output for xmms2.

%package output-oss
Summary:	OSS output
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description output-oss
This package enables OSS output for xmms2.

%package transport-curl
Summary:	HTTP curl transport
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description transport-curl
This package contains a HTTP transport for xmms2.

%package transport-gnomevfs
Summary:	GnomeVFS transport
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description transport-gnomevfs
This package contains a GnomeVFS transport for xmms2.

%package transport-samba
Summary:	Samba transport
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description transport-samba
This package contains a Samba transport for xmms2.

%package devel
Summary:	Development libraries and header files
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the development libaries and header
files for xmm2.

%prep
%setup -q -n %{name}-%{version}DR%{_dr}
sed -i xmmsenv.py \
	-e '/os\.path\.join(self\.install_prefix.*"lib/s@"lib@"%{_lib}@'
sed -i src/clients/lib/python/Library \
	-e 's/get_python_lib()/get_python_lib("false")/'

%build
scons \
	CC=%{__cc}		\
	CXX=%{__cxx}		\
	CCFLAGS="%{rpmcflags}"	\
	PREFIX=%{_prefix}	\
	MANDIR=%{_mandir}	\
	PKGCONFIGDIR=%{_pkgconfigdir}

%install
rm -rf $RPM_BUILD_ROOT

scons install \
	INSTALLDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/xmms2d
%attr(755,root,root) %{_libdir}/libxmmsclient.so.*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libxmms_diskwrite.so
%attr(755,root,root) %{_libdir}/%{name}/libxmms_eq.so
%attr(755,root,root) %{_libdir}/%{name}/libxmms_file.so
%attr(755,root,root) %{_libdir}/%{name}/libxmms_html.so
%attr(755,root,root) %{_libdir}/%{name}/libxmms_m3u.so
%attr(755,root,root) %{_libdir}/%{name}/libxmms_pls.so
%attr(755,root,root) %{_libdir}/%{name}/libxmms_replaygain.so
%{_datadir}/%{name}

### clients
%files client-cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmms2

%files client-sdlvis
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sdl-vis

%files client-lib-ecore
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmmsclient-ecore.so.*

%files client-lib-ecore-ruby
%defattr(644,root,root,755)
%attr(755,root,root) %{_rubyarchdir}/xmmsclient_ecore.so

%files client-lib-glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmmsclient-glib.so.*

%files client-lib-glib-ruby
%defattr(644,root,root,755)
%attr(755,root,root) %{_rubyarchdir}/xmmsclient_glib.so

%files client-lib-python
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/xmmsclient.so

%files client-lib-ruby
%defattr(644,root,root,755)
%attr(755,root,root) %{_rubyarchdir}/xmmsclient.so

### input
%if 0
%files input-cd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_cdtransport.so
%attr(755,root,root) %{_libdir}/%{name}/libxmms_cddecoder.so
%endif

%files input-flac
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_flac.so

%files input-mad
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_mad.so

%files input-modplug
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_modplug.so

%if 0
%files input-sid
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_sid.so
%endif

%files input-speex
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_speex.so

%files input-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_vorbisfile.so

%files input-wav
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_wave.so

### output
%files output-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_alsa.so

%files output-jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_jack.so

%files output-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_oss.so

%files transport-curl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_curl_http.so

%files transport-gnomevfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_gnomevfs.so

%files transport-samba
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_smb.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
%{_libdir}/*.a
%{_pkgconfigdir}/*
