"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nmain.proto\x12\x07streams\x1a\x1bgoogle/protobuf/empty.proto"\'\n\nSimpleMsg1\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12\t\n\x01s\x18\x02 \x01(\t"\'\n\nSimpleMsg2\x12\x0e\n\x06number\x18\x01 \x03(\x05\x12\t\n\x01s\x18\x02 \x03(\t"Q\n\nSimpleMsg3\x12#\n\x06number\x18\x01 \x03(\x0b2\x13.streams.SimpleMsg2\x12\x1e\n\x01s\x18\x02 \x03(\x0b2\x13.streams.SimpleMsg22\xb7\x04\n\x07Example\x12;\n\nGetStream1\x12\x13.streams.SimpleMsg1\x1a\x16.google.protobuf.Empty(\x01\x12>\n\rReturnStream1\x12\x16.google.protobuf.Empty\x1a\x13.streams.SimpleMsg10\x01\x12;\n\x0bBothStream1\x12\x13.streams.SimpleMsg1\x1a\x13.streams.SimpleMsg1(\x010\x01\x12;\n\nGetStream2\x12\x13.streams.SimpleMsg2\x1a\x16.google.protobuf.Empty(\x01\x12>\n\rReturnStream2\x12\x16.google.protobuf.Empty\x1a\x13.streams.SimpleMsg20\x01\x12;\n\x0bBothStream2\x12\x13.streams.SimpleMsg2\x1a\x13.streams.SimpleMsg2(\x010\x01\x12;\n\nGetStream3\x12\x13.streams.SimpleMsg3\x1a\x16.google.protobuf.Empty(\x01\x12>\n\rReturnStream3\x12\x16.google.protobuf.Empty\x1a\x13.streams.SimpleMsg30\x01\x12;\n\x0bBothStream3\x12\x13.streams.SimpleMsg3\x1a\x13.streams.SimpleMsg3(\x010\x01B3Z1git.gendocu.com/gendocu/StreamsExample.git/sdk/gob\x06proto3')
_SIMPLEMSG1 = DESCRIPTOR.message_types_by_name['SimpleMsg1']
_SIMPLEMSG2 = DESCRIPTOR.message_types_by_name['SimpleMsg2']
_SIMPLEMSG3 = DESCRIPTOR.message_types_by_name['SimpleMsg3']
SimpleMsg1 = _reflection.GeneratedProtocolMessageType('SimpleMsg1', (_message.Message,), {'DESCRIPTOR': _SIMPLEMSG1, '__module__': 'main_pb2'})
_sym_db.RegisterMessage(SimpleMsg1)
SimpleMsg2 = _reflection.GeneratedProtocolMessageType('SimpleMsg2', (_message.Message,), {'DESCRIPTOR': _SIMPLEMSG2, '__module__': 'main_pb2'})
_sym_db.RegisterMessage(SimpleMsg2)
SimpleMsg3 = _reflection.GeneratedProtocolMessageType('SimpleMsg3', (_message.Message,), {'DESCRIPTOR': _SIMPLEMSG3, '__module__': 'main_pb2'})
_sym_db.RegisterMessage(SimpleMsg3)
_EXAMPLE = DESCRIPTOR.services_by_name['Example']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z1git.gendocu.com/gendocu/StreamsExample.git/sdk/go'
    _SIMPLEMSG1._serialized_start = 52
    _SIMPLEMSG1._serialized_end = 91
    _SIMPLEMSG2._serialized_start = 93
    _SIMPLEMSG2._serialized_end = 132
    _SIMPLEMSG3._serialized_start = 134
    _SIMPLEMSG3._serialized_end = 215
    _EXAMPLE._serialized_start = 218
    _EXAMPLE._serialized_end = 785