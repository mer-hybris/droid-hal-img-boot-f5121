%define device f5121

%define mkbootimg_cmd mkbootimg --ramdisk %{initrd}  --kernel %{kernel} --base 0x80000000 --pagesize 2048 --cmdline "selinux=0 lpm_levels.sleep_disabled=1 user_debug=31 androidboot.selinux=permissive msm_rtb.filter=0x3F ehci-hcd.park=3 dwc3.maximum_speed=high dwc3_msm.prop_chg_detect=Y coherent_pool=8M sched_enable_power_aware=1 androidboot.hardware=suzu zram.num_devices=4"  --output

%define root_part_label userdata
%define factory_part_label system

%define display_brightness_path /sys/class/leds/lcd-backlight/brightness
%define display_brightness 16

%define lvm_root_size 4000

# mkbootimg needs python
BuildRequires:  python

%include initrd/droid-hal-device-img-boot.inc
