# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/data/token/fb_token.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/data/token/fb_token.proto',
  package='wuprotos.data.token',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\"wuprotos/data/token/fb_token.proto\x12\x13wuprotos.data.token\"\x18\n\x07\x46\x62Token\x12\r\n\x05token\x18\x01 \x01(\tb\x06proto3')
)




_FBTOKEN = _descriptor.Descriptor(
  name='FbToken',
  full_name='wuprotos.data.token.FbToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='wuprotos.data.token.FbToken.token', index=0,
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
  serialized_start=59,
  serialized_end=83,
)

DESCRIPTOR.message_types_by_name['FbToken'] = _FBTOKEN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FbToken = _reflection.GeneratedProtocolMessageType('FbToken', (_message.Message,), dict(
  DESCRIPTOR = _FBTOKEN,
  __module__ = 'wuprotos.data.token.fb_token_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.data.token.FbToken)
  ))
_sym_db.RegisterMessage(FbToken)


# @@protoc_insertion_point(module_scope)
