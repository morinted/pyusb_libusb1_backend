#!/usr/bin/env bash

set -e

# Install libusb if it isn't installed.
brew list libusb || brew install libusb

libusb="$(brew --prefix libusb)/lib/libusb-1.0.0.dylib"
target="pyusb_libusb1_backend/libusb-1.0.0.dylib"

cp "$libusb" "$target"
# Remove installation ID from dylib
install_name_tool -id "libusb-1.0.0.dylib" "$target"
