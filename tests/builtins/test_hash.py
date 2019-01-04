from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class HashTests(TranspileTestCase):
    pass


class BuiltinHashFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["hash"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_dict',
        'test_frozenset',
        'test_list',
        'test_None',
        'test_NotImplemented',
        'test_range',
        'test_set',
        'test_slice',
        'test_str',
        'test_tuple',
        'test_obj',
    ]
