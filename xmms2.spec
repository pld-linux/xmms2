# XXX: what about -devel? shouldn't -static be separated?
#
# Conditional build:
%bcond_with	efl	# ecore client library
%bcond_without	java	# Java/JNI module
%bcond_with	python	# Python module (doesn't build with python3-based scons 4)
%bcond_without	ruby	# Ruby modules
%bcond_with	flac	# flac plugin (incompatible with 1.1.3+)

Summary:	Client/server based media player system
Summary(pl.UTF-8):	System odtwarzania multimediów oparty na architekturze klient/serwer
Name:		xmms2
Version:	0.2DrDolittle
Release:	0.1
License:	LGPL v2.1
Group:		Applications/Sound
Source0:	https://downloads.sourceforge.net/xmms2/%{name}-%{version}.tar.bz2
# Source0-md5:	93daf53d21d198d8e05bf4de37976d7a
Patch0:		%{name}-tabs.patch
Patch1:		%{name}-python3.patch
Patch2:		%{name}-link.patch
Patch3:		%{name}-modplug.patch
Patch4:		%{name}-mdns.patch
Patch5:		%{name}-ruby.patch
Patch6:		%{name}-sid-update.patch
Patch7:		%{name}-java.patch
URL:		http://xmms2.xmms.se/
BuildRequires:	SDL-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	avahi-devel
BuildRequires:	avahi-compat-libdns_sd-devel
BuildRequires:	avahi-glib-devel
BuildRequires:	curl-devel >= 7.11.2
%{?with_efl:BuildRequires:	ecore-devel}
BuildRequires:	faad2-devel >= 2
%{?with_flac:BuildRequires:	flac-devel < 1.1.3}
BuildRequires:	gamin-devel
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	gnome-vfs2-devel >= 2.0
BuildRequires:	jack-audio-connection-kit-devel
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libmad-devel
BuildRequires:	libmodplug-devel
BuildRequires:	libmpcdec-devel
BuildRequires:	libsidplay2-devel
BuildRequires:	libsmbclient-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig
%if %{with python}
BuildRequires:	python-Pyrex >= 0.9.4.2
BuildRequires:	python-devel >= 2.3
%endif
BuildRequires:	python3 >= 1:3.2
BuildRequires:	rpmbuild(macros) >= 1.277
%{?with_ruby:BuildRequires:	ruby-modules >= 1:1.8}
BuildRequires:	scons >= 4
BuildRequires:	sed >= 4.0
#BuildRequires:	speex-devel
BuildRequires:	sqlite3-devel >= 3.2
Obsoletes:	xmms2-input-cd < 0.2DrCox
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the daemon that loads plugins and allows clients
to connect.

%description -l pl.UTF-8
Ten pakiet zawiera demona wczytującego wtyczki i pozwalającego
klientom łączyć się.

%package client-cli
Summary:	Simple text-ui for xmms2
Summary(pl.UTF-8):	Prosty tekstowy interfejs dla xmms2
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description client-cli
Simple text-ui for xmms2.

%description client-cli -l pl.UTF-8
Prosty tekstowy interfejs dla xmms2.

%package client-sdlvis
Summary:	Simple SDL visualization client for xmms2
Summary(pl.UTF-8):	Prosty klient wizualizacji SDL dla xmms2
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description client-sdlvis
Simple SDL visualization client for xmms2.

%description client-sdlvis -l pl.UTF-8
Prosty klient wizualizacji SDL dla xmms2.

%package client-lib-ecore
Summary:	ecore client library
Summary(pl.UTF-8):	Biblioteka kliencka ecore
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description client-lib-ecore
ecore client library.

%description client-lib-ecore -l pl.UTF-8
Biblioteka kliencka ecore.

%package client-lib-ecore-ruby
Summary:	Ruby bindings for the xmms2 ecore client library
Summary(pl.UTF-8):	Wiązania Ruby'ego dla biblioteki klienckiej xmms2 ecore
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-client-lib-ecore = %{version}-%{release}

%description client-lib-ecore-ruby
Ruby bindings for the xmms2 ecore client library.

%description client-lib-ecore-ruby -l pl.UTF-8
Wiązania Ruby'ego dla biblioteki klienckiej xmms2 ecore.

%package client-lib-glib
Summary:	GLib client library
Summary(pl.UTF-8):	Biblioteka kliencka GLib
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description client-lib-glib
GLib client library.

%description client-lib-glib -l pl.UTF-8
Biblioteka kliencka GLib.

%package client-lib-glib-ruby
Summary:	Ruby bindings for the xmms2 GLib client library
Summary(pl.UTF-8):	Wiązania Ruby'ego dla biblioteki klienckiej xmms2 GLib
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-client-lib-glib = %{version}-%{release}

%description client-lib-glib-ruby
Ruby bindings for the xmms2 GLib client library.

%description client-lib-glib-ruby -l pl.UTF-8
Wiązania Ruby'ego dla biblioteki klienckiej xmms2 GLib.

%package client-lib-java
Summary:	xmms2 Java bindings
Summary(pl.UTF-8):	Wiązania Javy do XMMS2
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	jre

%description client-lib-java
Java bindings for the xmms2 clientlib.

%description client-lib-java -l pl.UTF-8
Wiązania Javy do xmms2.

%package client-lib-python
Summary:	xmms2 Python bindings
Summary(pl.UTF-8):	Wiązania Pythona do XMMS2
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	python-libs

%description client-lib-python
Python bindings for the xmms2 clientlib.

%description client-lib-python -l pl.UTF-8
Wiązania Pythona do xmms2.

%package client-lib-ruby
Summary:	Ruby bindings for the xmms2 client library
Summary(pl.UTF-8):	Wiązania Ruby'ego dla biblioteki klienckiej xmms2
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description client-lib-ruby
Ruby bindings for the xmms2 client library.

%description client-lib-ruby -l pl.UTF-8
Wiązania Ruby'ego dla biblioteki klienckiej xmms2.

%package input-faad
Summary:	AAC decorer
Summary(pl.UTF-8):	Dekoder AAC
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-faad
This package enables AAC decoding using faad2 library for xmms2.

%description input-faad -l pl.UTF-8
Ten pakiet umożliwia dekodowanie plików AAC przez xmms2 przy użyciu
biblioteki faad2.

%package input-flac
Summary:	FLAC decorer
Summary(pl.UTF-8):	Dekoder FLAC
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-flac
This package enables FLAC decoding for xmms2.

%description input-flac -l pl.UTF-8
Ten pakiet umożliwia dekodowanie FLAC przez xmms2.

%package input-mad
Summary:	mad-based MP3 decoder
Summary(pl.UTF-8):	Oparty na mad dekoder MP3
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-mad
This package enables MP3 decoding for xmms2.

%description input-mad -l pl.UTF-8
Ten pakiet umożliwia dekodowanie MP3 przez xmms2.

%package input-modplug
Summary:	MOD decoder
Summary(pl.UTF-8):	Dekoder MOD
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-modplug
This package enables MOD decoding through modplug decoding for xmms2.

%description input-modplug -l pl.UTF-8
Ten pakiet umożliwia dekodowanie MOD przez xmms2 poprzez modplug.

%package input-musepack
Summary:	MPC decoder
Summary(pl.UTF-8):	Dekoder MPC
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-musepack
This package enables MPC decoding for xmms2.

%description input-musepack -l pl.UTF-8
Ten pakiet umożliwia dekodowanie MPC przez xmms2.

%package input-sid
Summary:	SID decoder
Summary(pl.UTF-8):	Dekoder SID
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-sid
This package enables SID decoding for xmms2.

%description input-sid -l pl.UTF-8
Ten pakiet umożliwia dekodowanie SID przez xmms2.

%package input-speex
Summary:	speex decoder
Summary(pl.UTF-8):	Dekoder speex
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-speex
This package enables speex decoding for xmms2.

%description input-speex -l pl.UTF-8
Ten pakiet umożliwia dekodowanie speex przez xmms2.

%package input-vorbis
Summary:	Ogg/Vorbis decoder
Summary(pl.UTF-8):	Dekoder Ogg/Vorbis
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-vorbis
This package enables Ogg/Vorbis decoding for xmms2.

%description input-vorbis -l pl.UTF-8
Ten pakiet umożliwia dekodowanie Ogg/Vorbis przez xmms2.

%package input-wav
Summary:	WAV decoder
Summary(pl.UTF-8):	Dekoder WAV
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description input-wav
This package enables WAV decoding for xmms2.

%description input-wav -l pl.UTF-8
Ten pakiet umożliwia dekodowanie WAV przez xmms2.

%package output-alsa
Summary:	ALSA output
Summary(pl.UTF-8):	Wyjście ALSA
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description output-alsa
This package enables ALSA output for xmms2.

%description output-alsa -l pl.UTF-8
Ten pakiet udostępnia wyjście ALSA dla xmms2.

%package output-jack
Summary:	JACK output
Summary(pl.UTF-8):	Wyjście JACK
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description output-jack
This package enables JACK output for xmms2.

%description output-jack -l pl.UTF-8
Ten pakiet udostępnia wyjście JACK dla xmms2.

%package output-oss
Summary:	OSS output
Summary(pl.UTF-8):	Wyjście OSS
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description output-oss
This package enables OSS output for xmms2.

%description output-oss -l pl.UTF-8
Ten pakiet udostępnia wyjście OSS dla xmms2.

%package transport-curl
Summary:	HTTP curl transport
Summary(pl.UTF-8):	Transport HTTP poprzez curl
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description transport-curl
This package contains a HTTP transport for xmms2.

%description transport-curl -l pl.UTF-8
Ten pakiet zawiera transport HTTP dla xmms2.

%package transport-gnomevfs
Summary:	GnomeVFS transport
Summary(pl.UTF-8):	Transport GnomeVFS
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description transport-gnomevfs
This package contains a GnomeVFS transport for xmms2.

%description transport-gnomevfs -l pl.UTF-8
Ten pakiet zawiera transport GnomeVFS dla xmms2.

%package transport-samba
Summary:	Samba transport
Summary(pl.UTF-8):	Transport Samba
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description transport-samba
This package contains a Samba transport for xmms2.

%description transport-samba -l pl.UTF-8
Ten pakiet zawiera transport Samba dla xmms2.

%package devel
Summary:	Development libraries and header files
Summary(pl.UTF-8):	Biblioteki programistyczne i pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the development libaries and header
files for xmms2.

%description devel -l pl.UTF-8
Ten pakiet zawiera biblioteki programistyczne i pliki nagłówkowe dla
xmms2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%{__sed} -i xmms2.pc.in \
	-e '/^libdir/ s,/lib$,/%{_lib},'
%{__sed} -i SConstruct \
	-e '/%PKGLIBDIR%/ s,/lib/,/%{_lib}/,'
%{__sed} -i xmmsenv.py \
	-e '/os\.path\.join(self\.install_prefix.*"lib/s@"lib@"%{_lib}@'
%{__sed} -i src/clients/lib/python/Library \
	-e 's/get_python_lib()/get_python_lib(plat_specific=True)/'

# avoid invalid version in .pc files
%{__sed} -i -e '/^XMMS_VERSION/ s/ \(Dr[^ ]*\) (git commit: %s%s)/\1/; s/ % .*//;' SConstruct

iconv -f iso-8859-1 -t utf8 doc/xmms2.1 -o doc/xmms2.1.utf8
%{__mv} doc/xmms2.1.utf8 doc/xmms2.1

%build
scons \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CCFLAGS="%{rpmcflags} %{rpmcppflags} $(pkg-config --cflags smbclient)"	\
	PREFIX=%{_prefix} \
	MANDIR=%{_mandir} \
	PKGCONFIGDIR=%{_pkgconfigdir}

%install
rm -rf $RPM_BUILD_ROOT

scons install \
	--install-sandbox $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/xmms2-launcher
%attr(755,root,root) %{_bindir}/xmms2d
%attr(755,root,root) %{_libdir}/libxmmsclient.so.0
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libxmms_diskwrite.so
%attr(755,root,root) %{_libdir}/%{name}/libxmms_eq.so
%attr(755,root,root) %{_libdir}/%{name}/libxmms_file.so
%attr(755,root,root) %{_libdir}/%{name}/libxmms_html.so
%attr(755,root,root) %{_libdir}/%{name}/libxmms_m3u.so
%attr(755,root,root) %{_libdir}/%{name}/libxmms_null.so
%attr(755,root,root) %{_libdir}/%{name}/libxmms_pls.so
%attr(755,root,root) %{_libdir}/%{name}/libxmms_replaygain.so
%{_datadir}/%{name}
%{_mandir}/man8/xmms2d.8*

### clients
%files client-cli
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmms2
%attr(755,root,root) %{_bindir}/xmms2-et
%attr(755,root,root) %{_bindir}/xmms2-find-avahi
%attr(755,root,root) %{_bindir}/xmms2-mdns-avahi
%attr(755,root,root) %{_bindir}/xmms2-mdns-dnssd
%attr(755,root,root) %{_bindir}/xmms2-mlib-updater
%{_mandir}/man1/xmms2.1*

%files client-sdlvis
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sdl-vis

%if %{with efl}
%files client-lib-ecore
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmmsclient-ecore.so.0

%if %{with ruby}
%files client-lib-ecore-ruby
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_sitearchdir}/xmmsclient_ecore.so
%endif
%endif

%files client-lib-glib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmmsclient-glib.so.0

%if %{with ruby}
%files client-lib-glib-ruby
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_vendorarchdir}/xmmsclient_glib.so
%endif

%if %{with java}
%files client-lib-java
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxmms2java.so
%{_javadir}/xmms2java.jar
%endif

%if %{with python}
%files client-lib-python
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/xmmsclient.so
%endif

%if %{with ruby}
%files client-lib-ruby
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_vendorarchdir}/xmmsclient.so
%endif

### input
%files input-faad
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_faad.so

%if %{with flac}
%files input-flac
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_flac.so
%endif

%files input-mad
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_mad.so

%files input-modplug
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_modplug.so

%files input-musepack
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_musepack.so

%files input-sid
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_sid.so

%if 0
# disabled in DR2.1
%files input-speex
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}/libxmms_speex.so
%endif

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
%attr(755,root,root) %{_libdir}/libxmmsclient.so
%attr(755,root,root) %{_libdir}/libxmmsclient-glib.so
%{_includedir}/xmms2
%{_libdir}/libxmmsclient.a
%{_libdir}/libxmmsclient-glib.a
%{_pkgconfigdir}/xmms2-client.pc
%{_pkgconfigdir}/xmms2-client-cpp.pc
%{_pkgconfigdir}/xmms2-client-ecore.pc
%{_pkgconfigdir}/xmms2-client-glib.pc
%{_pkgconfigdir}/xmms2-plugin.pc
