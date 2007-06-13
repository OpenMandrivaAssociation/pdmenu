Summary:	A simple text-based menu program
Name:		pdmenu
Version:	1.2.69
Release:	7mdk
URL:		http://kitenet.net/programs/pdmenu/

Source:		%name-%version.tar.bz2
Patch0:		pdmenu-1.2.61-menu.patch.bz2

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

%setup -q

%build

%configure

%make

%install
rm -fr %buildroot

make INSTALL_PREFIX=%buildroot install

install -m 0755 examples/newbie/modem-check examples/newbie/rpm-info-on-command %buildroot/%_libdir/pdmenu

rm -f examples/*.in examples/newbie/*.in examples/newbie/modem-check examples/newbie/rpm-info-on-command examples/editdir.pl examples/showdir.pl

install -m755 debian/cpp.pl %buildroot/%_libdir/pdmenu
cp -f debian/pdmenurc.debian %buildroot/%_sysconfdir/pdmenurc

for CVSDIR in `find . -type d -name CVS`; do
   rm -rf $CVSDIR
done


%clean
rm -fr %buildroot


%postun
if [ "$1" = 0 ]; then
  rm -rf %{_localstatedir}/pdmenu
fi
  

%files
%defattr (-,root,root,-)
%doc README doc/BUGS doc/TODO doc/ANNOUNCE debian/changelog examples 
%config(noreplace) %_sysconfdir/pdmenurc
%_bindir/*
%_mandir/man1/*
%_mandir/man5/*
%_libdir/pdmenu
