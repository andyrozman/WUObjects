# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/get_store_pack_info_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/get_store_pack_info_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nGwuprotos/networking/requests/messages/get_store_pack_info_message.proto\x12%wuprotos.networking.requests.messages\"*\n\x17GetStorePackInfoMessage\x12\x0f\n\x07pack_id\x18\x01 \x01(\tb\x06proto3')
)




_GETSTOREPACKINFOMESSAGE = _descriptor.Descriptor(
  name='GetStorePackInfoMessage',
  full_name='wuprotos.networking.requests.messages.GetStorePackInfoMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pack_id', full_name='wuprotos.networking.requests.messages.GetStorePackInfoMessage.pack_id', index=0,
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
  serialized_start=114,
  serialized_end=156,
)

DESCRIPTOR.message_types_by_name['GetStorePackInfoMessage'] = _GETSTOREPACKINFOMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetStorePackInfoMessage = _reflection.GeneratedProtocolMessageType('GetStorePackInfoMessage', (_message.Message,), dict(
  DESCRIPTOR = _GETSTOREPACKINFOMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.get_store_pack_info_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.GetStorePackInfoMessage)
  ))
_sym_db.RegisterMessage(GetStorePackInfoMessage)


# @@protoc_insertion_point(module_scope)
