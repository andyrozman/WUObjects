# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientFtueVideoFromUrl.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientFtueVideoFromUrl.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n1WUProtos/Data/Client/ClientFtueVideoFromUrl.proto\x12\x14WUProtos.Data.Client\",\n\x16\x43lientFtueVideoFromUrl\x12\x12\n\nurl_format\x18\x01 \x01(\tb\x06proto3')
)




_CLIENTFTUEVIDEOFROMURL = _descriptor.Descriptor(
  name='ClientFtueVideoFromUrl',
  full_name='WUProtos.Data.Client.ClientFtueVideoFromUrl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='url_format', full_name='WUProtos.Data.Client.ClientFtueVideoFromUrl.url_format', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=75,
  serialized_end=119,
)

DESCRIPTOR.message_types_by_name['ClientFtueVideoFromUrl'] = _CLIENTFTUEVIDEOFROMURL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientFtueVideoFromUrl = _reflection.GeneratedProtocolMessageType('ClientFtueVideoFromUrl', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTFTUEVIDEOFROMURL,
  __module__ = 'WUProtos.Data.Client.ClientFtueVideoFromUrl_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientFtueVideoFromUrl)
  ))
_sym_db.RegisterMessage(ClientFtueVideoFromUrl)


# @@protoc_insertion_point(module_scope)