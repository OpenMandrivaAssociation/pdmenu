Summary:	A simple text-based menu program
Name:		pdmenu
Version:	1.2.90
Release:	%mkrel 3
URL:		http://kitenet.net/programs/pdmenu/
Source0:	http://ftp.debian.org/debian/pool/main/p/pdmenu/pdmenu_%version.tar.gz
Source1:	pdmenurc
License:	GPL
Group:		Shells
BuildRoot:	%_tmppath/%name-%version-%release-root
Buildrequires:	slang-devel
Requires:	gpm >= 1.17.8
Conflicts:	menu < 2.0.0

%description
A simple full screen menu program, intended to be a comfortable login shell for
inexperienced users.

%prep
%setup -q -n pdmenu

%build
%configure

%make

%install
rm -fr %buildroot

make INSTALL_PREFIX=%buildroot install

install -m 0755 examples/newbie/modem-check \
                examples/newbie/rpm-info-on-command \
                %buildroot/%_datadir/pdmenu

rm -f examples/*.in examples/newbie/*.in examples/newbie/modem-check \
      examples/newbie/rpm-info-on-command examples/editdir.pl \
      examples/showdir.pl

cp -f %{_sourcedir}/pdmenurc %buildroot/%_sysconfdir/pdmenurc

%find_lang %{name}

%clean
rm -fr %buildroot

%postun
if [ "$1" = 0 ]; then
  rm -rf %{_localstatedir}/lib/pdmenu
fi

%files -f %{name}.lang
%defattr (-,root,root,-)
%doc README doc/BUGS doc/TODO doc/ANNOUNCE debian/changelog examples 
%config(noreplace) %_sysconfdir/pdmenurc
%_bindir/*
%_datadir/pdmenu
%_mandir/man1/*
%_mandir/man5/*

