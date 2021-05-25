#!/usr/bin/env python3

import os
import sys

from setuptools import Extension, setup


ext_modules = []


libusb_dir = 'libusb'
libusb_src_dir = os.path.join(libusb_dir, 'libusb')

libusb_deps = []
libusb_incs = ['{src}']
libusb_srcs = ('''
               {src}/core.c
               {src}/descriptor.c
               {src}/hotplug.c
               {src}/io.c
               {src}/strerror.c
               {src}/sync.c
               '''.split())
libusb_libs = []
libusb_ldflags = []

# Only build extension if libusb source tree is present.
build_libusb_extension = os.path.exists(libusb_src_dir)

# macOS.
if sys.platform.startswith('darwin'):
    libusb_deps.extend('''
                       {src}/os/events_posix.h
                       {src}/os/threads_posix.h
                       {src}/os/darwin_usb.h
                       {top}/Xcode/config.h
                       '''.split())
    libusb_incs.insert(0, '{top}/Xcode')
    libusb_srcs.extend('''
                       {src}/os/events_posix.c
                       {src}/os/threads_posix.c
                       {src}/os/darwin_usb.c
                       '''.split())
    libusb_libs.extend('''
                       objc
                       '''.split())
    libusb_ldflags.extend('''
                          -Wl,-framework,IOKit
                          -Wl,-framework,CoreFoundation
                          '''.split())
else:
    # Only build extension for supported platforms.
    build_libusb_extension = False

if build_libusb_extension:

    for var in libusb_deps, libusb_incs, libusb_srcs, libusb_ldflags:
        for n, v in enumerate(var):
            var[n] = v.format(
                top=libusb_dir,
                src=libusb_src_dir
            )

    libusb_extension = Extension(
        'pyusb_libusb1_backend.libusb',
        depends=libusb_deps,
        include_dirs=libusb_incs,
        sources=libusb_srcs,
        libraries=libusb_libs,
        extra_link_args=libusb_ldflags,
    )

    ext_modules.append(libusb_extension)


setup(ext_modules=ext_modules)
