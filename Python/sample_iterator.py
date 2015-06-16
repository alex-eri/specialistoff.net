gpart create -s gpt ada0
gpart add -t freebsd-boot -s 64k ada0
gpart add -t freebsd-swap -s 4G ada0
gpart add -t freebsd-ufs ada0
/sbin/gpart backup ada0 | /sbin/gpart restore -F ada1

gpart bootcode -b /boot/pmbr -p /boot/gptboot -i 1 ada0
gpart bootcode -b /boot/pmbr -p /boot/gptboot -i 1 ada1

gmirror label -vb round-robin boot /dev/ada0p1
gmirror label -vb round-robin swap /dev/ada0p2
gmirror label -vb round-robin root /dev/ada0p3
gmirror load

newfs -O2 -U /dev/mirror/root

mount /dev/mirror/root /mnt

fetch ftp://ftp.freebsd.org/pub/FreeBSD/releases/amd64/10.1-RELEASE/base.txz
fetch ftp://ftp.freebsd.org/pub/FreeBSD/releases/amd64/10.1-RELEASE/kernel.txz

cat base.txz | tar --unlink -xpJf - -C /mnt/
cat kernel.txz | tar --unlink -xpJf - -C /mnt/

echo 'geom_mirror_load="YES"' >> /mnt/boot/loader.conf

echo '# Check FS' >> /mnt/etc/rc.conf
echo 'background_fsck="NO"' >> /mnt/etc/rc.conf
echo 'fsck_y_enable="YES"' >> /mnt/etc/rc.conf

echo 'ifconfig_re0="inet 10.0.0.1 netmask 255.0.0.0 up"' >> /mnt/etc/rc.conf
echo 'defaultrouter="10.0.0.1"' >> /mnt/etc/rc.conf

echo '# SSH' >> /mnt/etc/rc.conf
sshd_enable="YES"' >> /mnt/etc/rc.conf

echo '# Device        Mountpoint      FStype  Options Dump    Pass#' > /mnt/etc/fstab
echo '/dev/mirror/root        /               ufs     rw      1       1' >> /mnt/etc/fstab
echo '/dev/mirror/swap        none            swap    sw      0       0' >> /mnt/etc/fstab

echo '' > /etc/make.conf

gmirror insert boot /dev/ada1p1
gmirror insert swap /dev/ada1p2
gmirror insert root /dev/ada1p3

gmirror status
