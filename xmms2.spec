# XXX: what about -devel? shouldn't -static be separated?
Summary:	Client/server based media player system
Summary(pl):	System odtwarzania multimediów oparty na architekturze klient/serwer
Name:		xmms2
Version:	0.1
%define	_dr	2.1
Release:	0.DR%{_dr}.0.2
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
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gnome-vfs2-devel
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	libmad-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libvorbis-devel
BuildRequires:	python-Pyrex
BuildRequires:	python-devel
BuildRequires:	ruby-modules
BuildRequires:	scons >= 0.94
BuildRequires:	speex-devel
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_rubyarchdir	%(ruby -r rbconfig -e 'print Config::CONFIG["sitearchdir"]')

%description
This package contains the daemon that loads plugins and allows clients
to connect.

%description -l pl
Ten pakiet zawiera demona wczytuj±cego wtyczki i pozwalaj±cego
klientom ³±czyæ siê.

%package client-cli
Summary:	Simple text-ui for xmms2
Summary(pl):	Prosty tekstowy interfejs dla xmms2
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description client-cli
Simple text-ui for xmms2.

%description client-cli -l pl
Prosty tekstowy interfejs dla xmms2.

%package client-sdlvis
Summary:	Simple SDL visualization client for xmms2
Summary(pl):	Prosty klient wizualizacji SDL dla xmms2
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description client-sdlvis
Simple SDL visualization client for xmms2.

%description client-sdlvis -l pl
Prosty klient wizualizacji SDL dla xmms2.

%package client-lib-ecore
Summary:	ecore client library
Summary(pl):	Biblioteka kliencka ecore
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description client-lib-ecore
ecore client library.

%description client-lib-ecore -l pl
Biblioteka kliencka ecore.

%package client-lib-ecore-ruby
Summary:	Ruby bindings for the xmms2 ecore client library
Summary(pl):	Wi±zania Ruby'ego dla biblioteki klienckiej xmms2 ecore
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-client-lib-ecore = %{version}-%{release}

%description client-lib-ecore-ruby
Ruby bindings for the xmms2 ecore client library.

%description client-lib-ecore-ruby -l pl
Wi±zania Ruby'ego dla biblioteki klienckiej xmms2 ecore.

%package client-lib-glib
Summary:	GLib client library
Summary(pl):	Biblioteka kliencka GLib
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description client-lib-glib
GLib client library.

%description client-lib-glib -l pl
Biblioteka kliencka GLib.

%package client-lib-glib-ruby
Summary:	Ruby bindings for the xmms2 GLib client library
Summary(pl):	Wi±zania Ruby'ego dla biblioteki klienckiej xmms2 GLib
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-client-lib-glib = %{version}-%{release}

%description client-lib-glib-ruby
Ruby bindings for the xmms2 GLib client library.

%description client-lib-glib-ruby -l pl
Wi±zania Ruby'ego dla biblioteki klienckiej xmms2 GLib.

%package client-lib-python
Summary:	xmms2 Python bindings
Summary(pl):	Wi±zania Pythona do XMMS2
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
%pyrequires_eq	python-libs

%description client-lib-python
Python bindings for the xmms2 clientlib.

%description client-lib-python -l pl
Wi±zania Pythona do xmms2.

%package client-lib-ruby
Summary:	Ruby bindings for the xmms2 client library
Summary(pl):	Wi±zania Ruby'ego dla biblioteki klienckiej xmms2
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description client-lib-ruby
Ruby bindings for the xmms2 client library.

%description client-lib-ruby -l pl
Wi±zania Ruby'ego dla biblioteki klienckiej xmms2.

%package input-cd
Summary:	CD transport and decoder
Summary(pl):	Transport i dekoder CD
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-cd
This package enables direct reading of CDs for xmms2.

%description input-cd -l pl
Ten pakiet umo¿liwia bezpo¶rednie czytanie p³yt CD przez xmms2.

%package input-flac
Summary:	FLAC decorer
Summary(pl):	Dekoder FLAC
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-flac
This package enables FLAC decoding for xmms2.

%description input-flac -l pl
Ten pakiet umo¿liwia dekodowanie FLAC przez xmms2.

%package input-mad
Summary:	mad-based MP3 decoder
Summary(pl):	Oparty na mad dekoder MP3
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-mad
This package enables MP3 decoding for xmms2.

%description input-mad -l pl
Ten pakiet umo¿liwia dekodowanie MP3 przez xmms2.

%package input-modplug
Summary:	MOD decoder
Summary(pl):	Dekoder MOD
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-modplug
This package enables MOD decoding through modplug decoding for xmms2.

%description input-modplug -l pl
Ten pakiet umo¿liwia dekodowanie MOD przez xmms2 poprzez modplug.

%package input-sid
Summary:	SID decoder
Summary(pl):	Dekoder SID
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-sid
This package enables SID decoding for xmms2.

%description input-sid -l pl
Ten pakiet umo¿liwia dekodowanie SID przez xmms2.

%package input-speex
Summary:	speex decoder
Summary(pl):	Dekoder speex
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-speex
This package enables speex decoding for xmms2.

%description input-speex -l pl
Ten pakiet umo¿liwia dekodowanie speex przez xmms2.

%package input-vorbis
Summary:	Ogg/Vorbis decoder
Summary(pl):	Dekoder Ogg/Vorbis
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-vorbis
This package enables Ogg/Vorbis decoding for xmms2.

%description input-vorbis -l pl
Ten pakiet umo¿liwia dekodowanie Ogg/Vorbis przez xmms2.

%package input-wav
Summary:	WAV decoder
Summary(pl):	Dekoder WAV
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-wav
This package enables WAV decoding for xmms2.

%description input-wav -l pl
Ten pakiet umo¿liwia dekodowanie WAV przez xmms2.

%package output-alsa
Summary:	ALSA output
Summary(pl):	Wyj¶cie ALSA
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description output-alsa
This package enables ALSA output for xmms2.

%description output-alsa -l pl
Ten pakiet udostêpnia wyj¶cie ALSA dla xmms2.

%package output-jack
Summary:	JACK output
Summary(pl):	Wyj¶cie JACK
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description output-jack
This package enables JACK output for xmms2.

%description output-jack -l pl
Ten pakiet udostêpnia wyj¶cie JACK dla xmms2.

%package output-oss
Summary:	OSS output
Summary(pl):	Wyj¶cie OSS
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description output-oss
This package enables OSS output for xmms2.

%description output-oss -l pl
Ten pakiet udostêpnia wyj¶cie OSS dla xmms2.

%package transport-curl
Summary:	HTTP curl transport
Summary(pl):	Transport HTTP poprzez curl
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description transport-curl
This package contains a HTTP transport for xmms2.

%description transport-curl -l pl
Ten pakiet zawiera transport HTTP dla xmms2.

%package transport-gnomevfs
Summary:	GnomeVFS transport
Summary(pl):	Transport GnomeVFS
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description transport-gnomevfs
This package contains a GnomeVFS transport for xmms2.

%description transport-gnomevfs -l pl
Ten pakiet zawiera transport GnomeVFS dla xmms2.

%package transport-samba
Summary:	Samba transport
Summary(pl):	Transport Samba
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description transport-samba
This package contains a Samba transport for xmms2.

%description transport-samba -l pl
Ten pakiet zawiera transport Samba dla xmms2.

%package devel
Summary:	Development libraries and header files
Summary(pl):	Biblioteki programistyczne i pliki nag³ówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the development libaries and header
files for xmms2.

%description devel -l pl
Ten pakiet zawiera biblioteki programistyczne i pliki nag³ówkowe dla
xmms2.

%prep
%setup -q -n %{name}-%{version}DR%{_dr}
sed -i xmmsenv.py \
	-e '/os\.path\.join(self\.install_prefix.*"lib/s@"lib@"%{_lib}@'
sed -i src/clients/lib/python/Library \
	-e 's/get_python_lib()/get_python_lib("false")/'

%build
scons \
	CC="%{__cc}"		\
	CXX="%{__cxx}"		\
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
