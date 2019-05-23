# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/proxy_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/proxy_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n9wuprotos/networking/requests/messages/proxy_message.proto\x12%wuprotos.networking.requests.messages\"=\n\x0cProxyMessage\x12\x0e\n\x06\x61\x63tion\x18\x01 \x01(\r\x12\x0c\n\x04host\x18\x02 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x62\x06proto3')
)




_PROXYMESSAGE = _descriptor.Descriptor(
  name='ProxyMessage',
  full_name='wuprotos.networking.requests.messages.ProxyMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='action', full_name='wuprotos.networking.requests.messages.ProxyMessage.action', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='wuprotos.networking.requests.messages.ProxyMessage.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='wuprotos.networking.requests.messages.ProxyMessage.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=100,
  serialized_end=161,
)

DESCRIPTOR.message_types_by_name['ProxyMessage'] = _PROXYMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProxyMessage = _reflection.GeneratedProtocolMessageType('ProxyMessage', (_message.Message,), dict(
  DESCRIPTOR = _PROXYMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.proxy_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.ProxyMessage)
  ))
_sym_db.RegisterMessage(ProxyMessage)


# @@protoc_insertion_point(module_scope)
