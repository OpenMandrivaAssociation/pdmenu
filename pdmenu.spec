Summary:	A simple text-based menu program
Name:		pdmenu
Version:	1.2.98
Release:	%mkrel 1
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



%changelog
* Sat Aug 01 2009 Frederik Himpe <fhimpe@mandriva.org> 1.2.98-1mdv2010.0
+ Revision: 407074
- update to new version 1.2.98

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2.90-3mdv2009.0
+ Revision: 241140
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jun 13 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.2.90-1mdv2008.0
+ Revision: 39035
- Updated to version 1.2.90.
- Removed unused menu patch.
- Added custom pdmenurc file.
- Cleanups.
- Import pdmenu




* Fri Jul 23 2004 Marcel Pol <mpol@mandrake.org> 1.2.69-7mdk
- again build against new slang

* Wed Jul 21 2004 Marcel Pol <mpol@mandrake.org> 1.2.69-6mdk
- build against new slang
- adjust buildrequires

* Mon May 05 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.2.69-5mdk
- buildrequires

* Tue Jan 28 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.2.69-4mdk
- rebuild

* Thu Jul 18 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.2.69-3mdk
- use gcc rather than egcs

* Tue Dec 25 2001 David BAUDNS <baudens@mandrakesoft.com> 1.2.69-2mdk
- Remove menu entry (no available category)

* Thu Aug 23 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2.69-1mdk
- updated to 1.2.69

* Thu Mar 01 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2.65-2mdk
- fix build
- remove CVS files

* Mon Jan 08 2001 Stefan van der Eijk <s.vandereijk@chello.nl> 1.2.65-1mdk
- macro's
- update to 1.2.65

* Thu Jun 22 2000 Matthew Campbell <mattcamp@crosswinds.net> 1.2.61-1mdk
- Updated to version 1.2.61.
- Fixed Source line to use variables for name and version.
- Changed Packager line (was formerly jeff.covey@pobox.com).
- Changed Buildroot line to use _tmppath variable instead of /var/tmp.
- Took out Requires line; RPM will fill in that information.
- Made some cosmetic changes to the spec file.
- Replaced ./configure with %%configure and took out the --mandir option
  on that command line.
- Changed the "make" command lien to the format recommended in the Mandrake
  RPM HOWTO.
- Changed installation of example scripts so that the install command makes
  sure the scripts are executable, and so that the RPM_BUILD_ROOT variable
  is used.
- Generally simplified installation of examples.
- Removed stuff to copy man pages to /usr/man, since they're now put there
  automatically.
- Added "-n pdmenu" option to %%setup macro call.
- Added fourth argument (755) to %%defattr macro call.
- Added %%clean section.
- Now depends on gpm >= 1.17.8 and conflicts with menu < 2.0.0, as in the
  Debian package.
- Added support for the menu package.

* Wed May 03 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.2.50-2mdk
- fix group
- fix files section 

* Fri Dec 03 1999 Lenny Cartier <lenny@mandrakesoft.com>
- nex in contribs
- fix attributes
