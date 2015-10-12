#!/bin/bash

# RemiZOffAlex 12-10-2015

mirror="http://mirror.yandex.ru"
arch="amd64"
dir="gentoo-distfiles/releases/$arch/autobuilds/current-install-$arch-minimal"
ver="20150924"
iso="install-$arch-minimal-$ver.iso"

rm gentoo-${ver}.igz gentoo-${ver}.kernel gentoo.igz

# Скачиваем образ
mkdir -p iso
pushd iso
    if [ ! -f ${iso} ]
    then
        wget ${mirror}/${dir}/${iso}
    fi
popd

# Монтируем образ и распаковываем необходимые файлы
mkdir -p mnt
mount -o loop iso/${iso} mnt/

cp mnt/isolinux/gentoo ./gentoo-$ver.kernel
cp mnt/isolinux/gentoo.igz ./
cp mnt/image.squashfs ./

umount mnt

# Применяем патч для init и собираем образ
mkdir igz
pushd igz
    xzcat ../gentoo.igz | cpio -idv &>/dev/null

    cp init init.orig
    patch < ../init-$ver.patch

    mkdir -p mnt/cdrom
    mv ../image.squashfs mnt/cdrom/

    find | cpio -o -H newc | xz -v --check=crc32 --x86 --lzma2 > ../gentoo-${ver}.igz
popd

# Удаляем мусор
rm -rf igz mnt gentoo.igz
