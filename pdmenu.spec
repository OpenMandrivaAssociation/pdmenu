Summary:	A simple text-based menu program
Name:		pdmenu
Version:	1.3.2
Release:	2
License:	GPLv2+
Group:		Shells
Url:		http://kitenet.net/programs/pdmenu/
Source0:	http://ftp.debian.org/debian/pool/main/p/pdmenu/pdmenu_%version.tar.gz
Source1:	pdmenurc
Buildrequires:	slang-devel
Requires:	gpm >= 1.17.8
Conflicts:	menu < 2.0.0

%description
A simple full screen menu program, intended to be a comfortable login shell for
inexperienced users.

%prep
%setup -q -n pdmenu

%files -f %{name}.lang
%doc README doc/BUGS doc/TODO doc/ANNOUNCE debian/changelog examples 
%config(noreplace) %{_sysconfdir}/pdmenurc
%{_bindir}/*
%{_datadir}/pdmenu
%{_mandir}/man1/*
%{_mandir}/man5/*

%postun
if [ "$1" = 0 ]; then
  rm -rf %{_localstatedir}/lib/pdmenu
fi

#----------------------------------------------------------------------------

%build
%configure2_5x
%make

%install
make INSTALL_PREFIX=%{buildroot} install

install -m 0755 examples/newbie/modem-check \
                examples/newbie/rpm-info-on-command \
                %{buildroot}%{_datadir}/pdmenu

rm -f examples/*.in examples/newbie/*.in examples/newbie/modem-check \
      examples/newbie/rpm-info-on-command examples/editdir.pl \
      examples/showdir.pl

cp -f %{SOURCE1} %{buildroot}%{_sysconfdir}/pdmenurc

%find_lang %{name}

