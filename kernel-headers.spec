#
# Spec file generated by kdist version v0.4-12-g6143
#
%define name		kernel-headers
%define version		3.3.4
%define src_uname_r	3.3.4-1
%define source_release	1
%define build_release	1%{nil}
%define archive		kernel-headers-3.3.4-1.1

%define build_srpm	1
%define no_source	1

%define _source_path	/usr/src/linux-%{src_uname_r}
%if %no_source
%define source_path	%{_source_path}/
%else
%define source_path	./
%endif

Name:			%{name}
Summary:		Linux kernel header files mostly used by your C library
Version:		%{version}
Release:		%mkrel %{source_release}.%{build_release}
Epoch:			1
License:		GPLv2
Group:			System/Kernel and hardware
URL:			http://www.kernel.org
%if %build_srpm
Source:			%{archive}.tar.bz2
%endif
BuildRoot:		%{_tmppath}/%{name}-%{version}-root
AutoReqProv:		no
%if %no_source
BuildRequires:		kernel-source = %{version}-%{mkrel %{source_release}}
%endif

%rename linux-userspace-headers

%define debug_package	%{nil}
%define __check_files	%{nil}

%description
C header files from the Linux kernel. The header files define
structures and constants that are needed for building most
standard programs, notably the C library.

This package is not suitable for building kernel modules, you
should use the '%{name}-devel' package instead.

%if %build_srpm
%prep
%setup -q -n %{archive}
%endif

%install
# Unfortunately we can't use "make outputmakefile" here because for
# some reasons this target requires a .config installed.
%if %no_source
extra_opts="O=$(pwd)"
%endif
make -C %{source_path} INSTALL_HDR_PATH=%{buildroot}/usr $extra_opts headers_install

%clean
rm -rf %{buildroot}

%files
%defattr (-, root, root)
/usr/include


%changelog
* Fri Apr 27 2012 Franck Bui <franck.bui@mandriva.com> 
  + Mandriva Release v3.3.4-1
  + drm/i915: enable RC6 by default on Sandy Bridge
  + cpupower tools: add install target to the debug tools' makefiles
  + cpupower tools: allow to build debug tools in a separate directory too
  + cpupower tool: allow to build in a separate directory
  + cpupower tool: makefile: simplify the recipe used to generate cpupower.pot target
  + cpupower tool: remove use of undefined variables from the clean target of the top makefile
  + perf doc: allow producing documentation in a specified output directory
  + [overlayfs] fs: limit filesystem stacking depth
  + [overlayfs] overlay filesystem documentation
  + [overlayfs] implement show_options
  + [overlayfs] add statfs support
  + [overlayfs] overlay filesystem
  + [overlayfs] vfs: introduce clone_private_mount()
  + [overlayfs] vfs: export do_splice_direct() to modules
  + [overlayfs] vfs: add i_op->open()
  + [overlayfs] vfs: pass struct path to __dentry_open()
  + usb: ehci: make HC see up-to-date qh/qtd descriptor ASAP
  + Mandriva Linux boot logo.
  + media video pwc lie in proc usb devices
  + usb storage unusual_devs add id 2.6.37 buildfix
  + Change to usb storage of unusual_dev.
  + Add blacklist of usb hid modules
  + bluetooth hci_usb disable isoc transfers
  + sound alsa hda ad1884a hp dc model
  + Support a Bluetooth SCO.
  + Include kbuild export pci_ids
  + platform x86 add shuttle wmi driver
  + net netfilter psd 2.6.35 buildfix
  + ipt_psd: Mandriva changes
  + net netfilter psd
  + net netfilter IFWLOG 2.6.37 buildfix
  + IFWLOG netfilter: fix return value of ipt_IFWLOG_checkentry()
  + net netfilter IFWLOG 2.6.35 buildfix
  + netfilter ipt_IFWLOG: Mandriva changes
  + net netfilter IFWLOG
  + net sis190 fix list usage
  + gpu drm mach64 3.3 buildfix
  + gpu drm mach64 3.2 buildfix
  + gpu drm mach64 2.6.39 buildfix
  + gpu drm mach64 2.6.37 buildfix
  + gpu drm mach64 2.6.36 buildfix
  + gpu drm mach64 fix for changed drm_ioctl
  + gpu drm mach64 fix for changed drm_pci_alloc
  + gpu drm mach64 2.6.31 buildfix
  + gpu drm mach64 fixes
  + gpu drm mach64
  + agp/intel: add new host bridge id for Q57 system
  + mpt scsi modules for VMWare's emulated
  + ppscsi: build fix for 2.6.39
  + scsi megaraid new sysfs name
  + scsi ppscsi mdvbz45393
  + scsi ppscsi update for scsi_data_buffer
  + scsi ppscsi sg helper update
  + scsi ppscsi_fixes
  + scsi ppscsi-2.6.2
  + acpi video add blacklist to use vendor driver
  + acpi processor M720SR limit to C2
  + CLEVO M360S acpi irq workaround
  + acpi add proc event regs
  + acpi dsdt initrd v0.9c fixes
  + acpi dsdt initrd v0.9c 2.6.28
  + UBUNTU: SAUCE: isapnp_init: make isa PNP scans occur async
  + pnp pnpbios off by default
  + PCI: Add ALI M5229 IDE comaptibility mode quirk
  + Card bus's PCI last bus
  + x86, cpufreq: set reasonable default for scaling_min_freq with p4-clockmod
  + x86 cpufreq speedstep dothan 3
  + x86 boot video 80x25 if break
  + x86 pci toshiba equium a60 assign busses
  + kdist: make the config name part of the localversion
  + kdist: give a name to the config file
