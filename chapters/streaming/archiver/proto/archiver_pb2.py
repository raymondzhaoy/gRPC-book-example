# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/archiver.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/archiver.proto',
  package='practical.grpc.v1',
  syntax='proto3',
  serialized_pb=_b('\n\x14proto/archiver.proto\x12\x11practical.grpc.v1\"1\n\nZipRequest\x12\x11\n\tfile_name\x18\x01 \x01(\t\x12\x10\n\x08\x63ontents\x18\x02 \x01(\x0c\"&\n\x0bZipResponse\x12\x17\n\x0fzipped_contents\x18\x01 \x01(\x0c\x32R\n\x08\x41rchiver\x12\x46\n\x03Zip\x12\x1d.practical.grpc.v1.ZipRequest\x1a\x1e.practical.grpc.v1.ZipResponse(\x01\x62\x06proto3')
)




_ZIPREQUEST = _descriptor.Descriptor(
  name='ZipRequest',
  full_name='practical.grpc.v1.ZipRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='file_name', full_name='practical.grpc.v1.ZipRequest.file_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contents', full_name='practical.grpc.v1.ZipRequest.contents', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=92,
)


_ZIPRESPONSE = _descriptor.Descriptor(
  name='ZipResponse',
  full_name='practical.grpc.v1.ZipResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='zipped_contents', full_name='practical.grpc.v1.ZipResponse.zipped_contents', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=132,
)

DESCRIPTOR.message_types_by_name['ZipRequest'] = _ZIPREQUEST
DESCRIPTOR.message_types_by_name['ZipResponse'] = _ZIPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ZipRequest = _reflection.GeneratedProtocolMessageType('ZipRequest', (_message.Message,), dict(
  DESCRIPTOR = _ZIPREQUEST,
  __module__ = 'proto.archiver_pb2'
  # @@protoc_insertion_point(class_scope:practical.grpc.v1.ZipRequest)
  ))
_sym_db.RegisterMessage(ZipRequest)

ZipResponse = _reflection.GeneratedProtocolMessageType('ZipResponse', (_message.Message,), dict(
  DESCRIPTOR = _ZIPRESPONSE,
  __module__ = 'proto.archiver_pb2'
  # @@protoc_insertion_point(class_scope:practical.grpc.v1.ZipResponse)
  ))
_sym_db.RegisterMessage(ZipResponse)



_ARCHIVER = _descriptor.ServiceDescriptor(
  name='Archiver',
  full_name='practical.grpc.v1.Archiver',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=134,
  serialized_end=216,
  methods=[
  _descriptor.MethodDescriptor(
    name='Zip',
    full_name='practical.grpc.v1.Archiver.Zip',
    index=0,
    containing_service=None,
    input_type=_ZIPREQUEST,
    output_type=_ZIPRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ARCHIVER)

DESCRIPTOR.services_by_name['Archiver'] = _ARCHIVER

# @@protoc_insertion_point(module_scope)
