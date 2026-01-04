%bcond clang 1
%bcond esound 0
%bcond libart 1
%bcond xscreensaver 1
%bcond jack 1
%bcond gamin 1

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 3

%define tde_pkg tdeartwork
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Summary:	Additional artwork (themes, sound themes, ...) for TDE
Version:	%{tde_version}
Release:	%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Group:		System/GUI/Other
URL:		http://www.trinitydesktop.org/

License:	GPLv2+

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DWITH_ALL_OPTIONS=ON -DWITH_ARTS=ON
BuildOption:    -DWITH_OPENGL=ON -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}
BuildOption:    -DWITH_XSCREENSAVER=%{!?with_xscreensaver:OFF}%{?with_xscreensaver:ON}
BuildOption:    -DWITH_LIBART=%{!?with_libart:OFF}%{?with_libart:ON}

Obsoletes:	trinity-kdeartwork < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdeartwork = %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	fdupes

BuildRequires:	gettext

BuildRequires:	pkgconfig(libidn)

# ESOUND support
%{?with_esound:BuildRequires:  pkgconfig(esound)}

# ACL support
BuildRequires:  pkgconfig(libacl)

# MESA support
BuildRequires:  pkgconfig(glu)

# LIBART support
%{?with_libart:BuildRequires:	pkgconfig(libart-2.0)}

# XSCREENSAVER support
BuildRequires:	xscreensaver
BuildRequires:	xscreensaver-base
BuildRequires:	xscreensaver-gl
BuildRequires:  pkgconfig(xscrnsaver)

BuildRequires:  pkgconfig(xrender)


# JACK support
%{?with_jack:BuildRequires:	pkgconfig(jack)}

# GAMIN support
%{?with_gamin:BuildRequires:	pkgconfig(gamin)}

# OPENSSL support
BuildRequires:	pkgconfig(openssl)


# Metapackage
Requires: %{name}-emoticons = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-misc = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-style = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-theme-icon = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-theme-window = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdewallpapers = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdescreensaver = %{?epoch:%{epoch}:}%{version}-%{release}

%if %{with xscreensaver}
Requires: trinity-tdescreensaver-xsavers = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdescreensaver-xsavers-extra = %{?epoch:%{epoch}:}%{version}-%{release}
%endif


%description
TDE (the Trinity Desktop Environment) is a powerful Open Source graphical
desktop environment for Unix workstations. It combines ease of use,
contemporary functionality, and outstanding graphical design with the
technological superiority of the Unix operating system.

This metapackage includes a collection of artistic extras (themes, widget
styles, screen savers, wallpaper, icons, emoticons and so on) provided
with the official release of TDE.


%files

##########

%package emoticons
Summary:	Emoticon collections for tDE chat clients
Group:		System/GUI/Other

%description emoticons
This package contains several collections of emoticons used by official
and unofficial TDE chat clients, such as Kopete and Konversation.

This package is part of TDE, and a component of the TDE artwork module.

%files emoticons
%defattr(-,root,root,-)
%{tde_prefix}/share/emoticons/

##########

%package misc
Summary:	Various multimedia goodies released with TDE
Group:		System/GUI/Other

%description misc
This package contains miscellaneous multimedia goodies for TDE.
Included are additional TDE sounds and kworldclock themes.

This package is part of Trinity, and a component of the TDE artwork module.

%files misc
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/kworldclock/
%{tde_prefix}/share/sounds/KDE_Logout_new.wav
%{tde_prefix}/share/sounds/KDE_Startup_new.wav

##########

%package style
Summary:	Widget styles released with Trinity
Group:		System/GUI/Other

%description style
This package contains additional widget styles for Trinity. Widget styles
can be used to customise the look and feel of interface components such
as buttons, scrollbars and so on.  They can be applied using the style
manager in the Trinity Control Center.

This package is part of Trinity, and a component of the TDE artwork module.

%files style
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/plugins/styles/
%{tde_prefix}/%{_lib}/trinity/tdestyle_phase_config.la
%{tde_prefix}/%{_lib}/trinity/tdestyle_phase_config.so
%{tde_prefix}/share/apps/tdestyle/

##########

%package theme-icon
Summary:	Icon themes released with Trinity
Group:		System/GUI/Other

Obsoletes:	trinity-kdeartwork-icons < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdeartwork-icons = %{?epoch:%{epoch}:}%{version}-%{release}

%description theme-icon
This package contains additional icon themes for Trinity. Icon themes can be
used to customise the appearance of standard icons throughout TDE. They
can be applied using the icon manager in the Trinity Control Centre.

This package is part of Trinity, and a component of the TDE artwork module.

%files theme-icon
%defattr(-,root,root,-)
%{tde_prefix}/share/icons/ikons/
%{tde_prefix}/share/icons/kdeclassic/
%{tde_prefix}/share/icons/kids/
%{tde_prefix}/share/icons/slick/
%{tde_prefix}/share/icons/locolor/index.theme
%{tde_prefix}/share/icons/locolor/*/*/*.png

##########

%package theme-window
Summary:	Window decoration themes released with Trinity
Group:		System/GUI/Other

%description theme-window
This package contains additional window decoration themes for Trinity. Window
decoration themes can be used to customise the look of window borders and
buttons, and can be applied using the window decoration manager in the Trinity
Control Center.

This package is part of Trinity, and a component of the TDE artwork module.

%files theme-window
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/twin*
%{tde_prefix}/share/apps/twin/

##########

%package -n trinity-tdewallpapers
Summary:	Wallpapers released with Trinity
Group:		System/GUI/Other
Obsoletes:	trinity-kdewallpapers < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdewallpapers = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdewallpapers
This package contains additional wallpapers for Trinity. Wallpapers can be
applied using the background manager in the Trinity Control Center.

This package is part of Trinity, and a component of the TDE artwork module.

%files -n trinity-tdewallpapers
%defattr(-,root,root,-)
%{tde_prefix}/share/wallpapers/*

##########

%package -n trinity-tdescreensaver
Summary:	Additional screen savers released with Trinity
Group:		System/GUI/Other

Obsoletes:	trinity-kscreensaver < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kscreensaver = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdescreensaver
This package contains the screen savers for Trinity. They can be tested and
selected within the Appearance and Themes section of the Trinity Control
Center.

The hooks for the standard xscreensavers are no longer part of this
package. To select and/or configure the standard xscreensavers through
the Trinity Control Center, install the separate package tdescreensaver-xsavers.

This package is part of Trinity, and a component of the TDE artwork module.

%files -n trinity-tdescreensaver
%defattr(-,root,root,-)
%{tde_prefix}/bin/kslideshow.kss
%{tde_prefix}/bin/kpolygon.kss
%{tde_prefix}/bin/krotation.kss
%{tde_prefix}/bin/ksolarwinds.kss
%{tde_prefix}/bin/klorenz.kss
%{tde_prefix}/bin/kvm.kss
%{tde_prefix}/bin/kflux.kss
%{tde_prefix}/bin/kscience.kss
%{tde_prefix}/bin/kbanner.kss
%{tde_prefix}/bin/kclock.kss
%{tde_prefix}/bin/kfiresaver.kss
%{tde_prefix}/bin/keuphoria.kss
%{tde_prefix}/bin/kfountain.kss
%{tde_prefix}/bin/kgravity.kss
%{tde_prefix}/bin/tdepartsaver.kss
%{tde_prefix}/bin/kpendulum.kss
%{tde_prefix}/bin/kblob.kss
%{tde_prefix}/bin/klines.kss
%{tde_prefix}/bin/kwave.kss
%{tde_prefix}/bin/tdeasciiquarium.kss
%{tde_prefix}/share/applnk/System/ScreenSavers/KBanner.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KBlob.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KClock.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KEuphoria.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KFiresaver.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KFlux.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KFountain.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KGravity.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KLines-saver.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KLorenz.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KPendulum.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KPolygon.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KRotation.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KScience.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KSlideshow.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KSolarWinds.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KVm.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KWave.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/tdepartsaver.desktop
%{tde_prefix}/share/apps/kfiresaver/
%{tde_prefix}/share/apps/tdescreensaver/
%{tde_prefix}/share/man/man1/kbanner.kss.1*
%{tde_prefix}/share/man/man1/kblob.kss.1*
%{tde_prefix}/share/man/man1/kclock.kss.1*
%{tde_prefix}/share/man/man1/keuphoria.kss.1
%{tde_prefix}/share/man/man1/kfiresaver.kss.1
%{tde_prefix}/share/man/man1/kflux.kss.1
%{tde_prefix}/share/man/man1/kfountain.kss.1
%{tde_prefix}/share/man/man1/kgravity.kss.1
%{tde_prefix}/share/man/man1/klines.kss.1
%{tde_prefix}/share/man/man1/klorenz.kss.1
%{tde_prefix}/share/man/man1/kpendulum.kss.1
%{tde_prefix}/share/man/man1/kpolygon.kss.1
%{tde_prefix}/share/man/man1/krotation.kss.1
%{tde_prefix}/share/man/man1/kscience.kss.1
%{tde_prefix}/share/man/man1/kslideshow.kss.1
%{tde_prefix}/share/man/man1/ksolarwinds.kss.1
%{tde_prefix}/share/man/man1/kvm.kss.1
%{tde_prefix}/share/man/man1/kwave.kss.1
%{tde_prefix}/share/man/man1/tdeasciiquarium.kss.1
%{tde_prefix}/share/man/man1/tdepartsaver.kss.1

%if %{with xscreensaver}
%{tde_prefix}/bin/kspace.kss
%{tde_prefix}/bin/kswarm.kss
%{tde_prefix}/share/applnk/System/ScreenSavers/KSpace.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/KSwarm.desktop
%{tde_prefix}/share/man/man1/kspace.kss.1
%{tde_prefix}/share/man/man1/kswarm.kss.1
%endif

##########

%if %{with xscreensaver}

%package -n trinity-tdescreensaver-xsavers
Summary:	Trinity hooks for standard xscreensavers
Group:		System/GUI/Other
Requires:	trinity-tdebase-bin >= %{tde_version}
Requires:	xscreensaver

Obsoletes:	trinity-kscreensaver-xsavers < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kscreensaver-xsavers = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdescreensaver-xsavers
This package allows a smooth integration of the standard xscreensavers
into Trinity. With this package installed you can select and/or configure
the standard xscreensavers through the Appearances and Themes section of
the Trinity Control Centre.

Note that this package does not actually contain any screensavers itself.
For the additional screensavers shipped with Trinity, see the separate package
tdescreensaver-trinity. This package does depend on the xscreensaver package, and
recommend the xscreensaver-gl package, as well as contain the necessary
files to integrate these packages into Trinity.

This package is part of Trinity, and a component of the TDE artwork module.

%files -n trinity-tdescreensaver-xsavers
%defattr(-,root,root,-)
%{tde_prefix}/bin/xscreensaver-getimage-file
%{tde_prefix}/bin/xscreensaver-getimage
%{tde_prefix}/bin/kxsconfig
%{tde_prefix}/bin/kxsrun
%{tde_prefix}/share/applnk/System/ScreenSavers/antinspect.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/antspotlight.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/atunnel.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/blinkbox.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/braid.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/bubble3d.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/circuit.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/cubestorm.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/deco.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/distort.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/endgame.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/engine.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/fiberlamp.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/flipflop.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/flipscreen3d.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/flyingtoasters.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/fuzzyflakes.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/galaxy.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/gears.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/gflux.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/glblur.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/gleidescope.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/glknots.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/glslideshow.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/glsnake.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/gltext.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/hypertorus.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/jigglypuff.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/lavalite.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/metaballs.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/mirrorblob.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/moebius.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/molecule.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/morph3d.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/penrose.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/pipes.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/polyhedra.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/polytopes.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/popsquares.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/pulsar.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/queens.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/ripples.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/shadebobs.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/sierpinski3d.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/slidescreen.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/sonar.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/spheremonics.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/stonerview.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/superquadrics.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/swirl.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/xlyap.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/m6502.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/glschool.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/moebiusgears.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/glcells.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/abstractile.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/lockward.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/cwaves.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/topblock.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/voronoi.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/cubicgrid.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/hypnowheel.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/lcdscrub.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/photopile.desktop
%{tde_prefix}/share/applnk/System/ScreenSavers/skytentacles.desktop
%{tde_prefix}/share/man/man1/kxsconfig.1
%{tde_prefix}/share/man/man1/kxsrun.1

%endif

##########

%package -n trinity-tdescreensaver-xsavers-extra
Summary:	Trinity hooks for standard xscreensavers
Group:		System/GUI/Other
Requires:	trinity-tdescreensaver-xsavers = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:	trinity-kscreensaver-xsavers-extra < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kscreensaver-xsavers-extra = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdescreensaver-xsavers-extra
This package allows a smooth integration of the universe xscreensavers
into Trinity. With this package installed you can select and/or configure
the universe xscreensavers through the Appearances and Themes section of
the Trinity Control Centre.

Note that this package does not actually contain any screensavers itself.
For the additional screensavers shipped with TDE, see the separate package
tdescreensaver.

This package is part of Trinity, and a component of the TDE artwork module.

%files -n trinity-tdescreensaver-xsavers-extra
%defattr(-,root,root,-)
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/webcollage.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/antinspect.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/antspotlight.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/atunnel.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/blinkbox.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/braid.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/bubble3d.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/circuit.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/cubestorm.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/deco.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/distort.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/endgame.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/engine.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/fiberlamp.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/flipflop.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/flipscreen3d.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/flyingtoasters.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/fuzzyflakes.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/galaxy.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/gears.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/gflux.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/glblur.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/gleidescope.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/glknots.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/glslideshow.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/glsnake.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/gltext.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/hypertorus.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/jigglypuff.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/lavalite.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/metaballs.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/mirrorblob.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/moebius.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/molecule.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/morph3d.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/penrose.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/pipes.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/polyhedra.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/polytopes.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/popsquares.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/pulsar.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/queens.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/ripples.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/shadebobs.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/sierpinski3d.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/slidescreen.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/sonar.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/spheremonics.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/stonerview.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/superquadrics.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/swirl.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/xlyap.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/m6502.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/glschool.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/moebiusgears.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/glcells.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/abstractile.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/lockward.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/cwaves.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/topblock.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/voronoi.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/cubicgrid.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/hypnowheel.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/lcdscrub.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/photopile.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/skytentacles.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KBanner.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KBlob.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KClock.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KEuphoria.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KFiresaver.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KFlux.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KFountain.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KGravity.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KLines-saver.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KLorenz.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KPendulum.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KPolygon.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KRotation.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KScience.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KSlideshow.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KSolarWinds.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KVm.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KWave.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/tdepartsaver.desktop

%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KSpace.desktop
%exclude %{tde_prefix}/share/applnk/System/ScreenSavers/KSwarm.desktop

%{tde_prefix}/share/applnk/System/ScreenSavers/*.desktop

%prep -a
# http://www.trinitydesktop.org/wiki/bin/view/Developers/HowToBuild
# NOTE: Before building tdeartwork, install any and all xhack screensavers that might be uses, then:
cd tdescreensaver/kxsconfig/
./update_hacks.sh


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
# Should not be here if xscreensaver is disabled
%if %{without xscreensaver}
%__rm -f "%{?buildroot}%{tde_prefix}/bin/xscreensaver-getimage"
%__rm -f "%{?buildroot}%{tde_prefix}/bin/xscreensaver-getimage-file"
%endif

# Duplicate with trinity-kbabel (from tdesdk)
%__rm -f "%{?buildroot}%{tde_prefix}/share/icons/locolor/16x16/apps/kbabel.png"
%__rm -f "%{?buildroot}%{tde_prefix}/share/icons/locolor/32x32/apps/kbabel.png"

# Links duplicate files
%fdupes "%{?buildroot}%{tde_prefix}/share"

# Fix invalid permissions
%if %{with xscreensaver}
chmod +x "%{?buildroot}%{tde_prefix}/bin/xscreensaver-getimage"
chmod +x "%{?buildroot}%{tde_prefix}/bin/xscreensaver-getimage-file"
%endif

