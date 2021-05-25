from importlib.util import find_spec
import ctypes

import pyusb_libusb1_backend


def test_no_missing_symbols():
    spec = find_spec('pyusb_libusb1_backend.libusb')
    assert spec is not None
    ctypes.CDLL(spec.origin)

def test_get_backend():
    backend = pyusb_libusb1_backend.get_pyusb_backend()
    assert backend is not None
