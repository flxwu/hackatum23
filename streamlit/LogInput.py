
def get_log_input(): return """
Nov 09 13:11:35 localhost kernel: Linux version 5.15.73 (oe-user@oe-host) (x86_64-poky-linux-gcc (GCC) 11.3.0, GNU ld (GNU Binutils) 2.38.20220708) #1 SMP PREEMPT Sun May 21 21:05:48 UTC 2023
Nov 09 13:11:35 localhost kernel: Command line: BOOT_IMAGE=/boot/vmlinuz root=/dev/sda2 video=eDP-1:d ro
Nov 09 13:11:35 localhost kernel: x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
Nov 09 13:11:35 localhost kernel: x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
Nov 09 13:11:35 localhost kernel: x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
Nov 09 13:11:35 localhost kernel: x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
Nov 09 13:11:35 localhost kernel: x86/fpu: Enabled xstate features 0x7, context size is 832 bytes, using 'compacted' format.
Nov 09 13:11:35 localhost kernel: signal: max sigframe size: 1776
Nov 09 13:11:35 localhost kernel: BIOS-provided physical RAM map:
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x0000000000000000-0x000000000009ffff] usable
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x00000000000a0000-0x00000000000fffff] reserved
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x0000000000100000-0x0000000009601fff] usable
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x0000000009602000-0x00000000097fffff] reserved
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x0000000009800000-0x000000000a1fffff] usable
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x000000000a200000-0x000000000a20afff] ACPI NVS
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x000000000a20b000-0x000000003d5ebfff] usable
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x000000003d5ec000-0x000000003d709fff] reserved
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x000000003d70a000-0x000000003d8a9fff] usable
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x000000003d8aa000-0x000000003dd35fff] ACPI NVS
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x000000003dd36000-0x000000003e4dafff] reserved
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x000000003e4db000-0x000000003e55ffff] type 20
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x000000003e560000-0x000000003effffff] usable
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x000000003f000000-0x000000003fffffff] reserved
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x00000000f8000000-0x00000000fbffffff] reserved
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x00000000fd000000-0x00000000ffffffff] reserved
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x0000000100000000-0x000000047effffff] usable
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x000000047f000000-0x00000004beffffff] reserved
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x00000004bf000000-0x00000004bf33ffff] usable
Nov 09 13:11:35 localhost kernel: BIOS-e820: [mem 0x00000004bf340000-0x00000004bfffffff] reserved
Nov 09 13:11:35 localhost kernel: NX (Execute Disable) protection: active
Nov 09 13:11:35 localhost kernel: efi: EFI v2.70 by American Megatrends
Nov 09 13:11:35 localhost kernel: efi: ACPI 2.0=0x3dcb5000 ACPI=0x3dcb5000 SMBIOS=0x3e390000 SMBIOS 3.0=0x3e38f000 MEMATTR=0x3a4c7018 ESRT=0x3ce10298 
Nov 09 13:11:35 localhost kernel: SMBIOS 3.2.0 present.
Nov 09 13:11:35 localhost kernel: DMI: R&S IPSX4_TS_CMP/IPSX4_TS_CMP, BIOS 3.4 11/19/2021
Nov 09 13:11:35 localhost kernel: tsc: Fast TSC calibration using PIT
Nov 09 13:11:35 localhost kernel: tsc: Detected 3244.097 MHz processor
Nov 09 13:11:35 localhost kernel: e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
Nov 09 13:11:35 localhost kernel: e820: remove [mem 0x000a0000-0x000fffff] usable
Nov 09 13:11:35 localhost kernel: last_pfn = 0x4bf340 max_arch_pfn = 0x400000000
Nov 09 13:11:35 localhost kernel: x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT  
Nov 09 13:11:35 localhost kernel: e820: update [mem 0x40000000-0xffffffff] usable ==> reserved
Nov 09 13:11:35 localhost kernel: last_pfn = 0x3f000 max_arch_pfn = 0x400000000
Nov 09 13:11:35 localhost kernel: esrt: Reserving ESRT space from 0x000000003ce10298 to 0x000000003ce102d0.
Nov 09 13:11:35 localhost kernel: e820: update [mem 0x3ce10000-0x3ce10fff] usable ==> reserved
Nov 09 13:11:35 localhost kernel: Using GB pages for direct mapping
"""
