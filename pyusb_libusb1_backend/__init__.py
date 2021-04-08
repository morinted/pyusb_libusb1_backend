
import sys
import os
import usb.backend.libusb1


def get_pyusb_backend():
    """
    pyusb supports a custom backend provided to usb.core.find.

    On macOS, we package libusb and this function will let plugins
    use the bundled dylib.

    If there is no custom dylib detected or the platform isn't Mac,
    we return None in order to use pyusb's default behavior.
    """

    if not sys.platform.startswith('darwin'):
        return None

    dylib_name = 'libusb-1.0.0.dylib'
    local_libusb1_path = os.path.join(os.path.dirname(__file__), dylib_name)

    if not os.path.exists(local_libusb1_path):
        return None

    return usb.backend.libusb1.get_backend(find_library=lambda x: local_libusb1_path)
