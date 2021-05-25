from importlib.util import find_spec

import usb.backend.libusb1


def get_pyusb_backend():
    """
    pyusb supports a custom backend provided to usb.core.find.

    On macOS, we package libusb and this function will let plugins
    use the bundled dylib.

    If there is no custom dylib detected or the platform isn't Mac,
    we return None in order to use pyusb's default behavior.
    """
    spec = find_spec('pyusb_libusb1_backend.libusb')
    if spec is None:
        return None
    return usb.backend.libusb1.get_backend(find_library=lambda x: spec.origin)
