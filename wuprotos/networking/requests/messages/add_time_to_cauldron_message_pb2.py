# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/add_time_to_cauldron_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/add_time_to_cauldron_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nHwuprotos/networking/requests/messages/add_time_to_cauldron_message.proto\x12%wuprotos.networking.requests.messages\"I\n\x18\x41\x64\x64TimeToCauldronMessage\x12\x13\n\x0b\x63\x61uldron_id\x18\x01 \x01(\x03\x12\x18\n\x10time_item_gmt_id\x18\x02 \x01(\tb\x06proto3')
)




_ADDTIMETOCAULDRONMESSAGE = _descriptor.Descriptor(
  name='AddTimeToCauldronMessage',
  full_name='wuprotos.networking.requests.messages.AddTimeToCauldronMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cauldron_id', full_name='wuprotos.networking.requests.messages.AddTimeToCauldronMessage.cauldron_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_item_gmt_id', full_name='wuprotos.networking.requests.messages.AddTimeToCauldronMessage.time_item_gmt_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=115,
  serialized_end=188,
)

DESCRIPTOR.message_types_by_name['AddTimeToCauldronMessage'] = _ADDTIMETOCAULDRONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddTimeToCauldronMessage = _reflection.GeneratedProtocolMessageType('AddTimeToCauldronMessage', (_message.Message,), dict(
  DESCRIPTOR = _ADDTIMETOCAULDRONMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.add_time_to_cauldron_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.AddTimeToCauldronMessage)
  ))
_sym_db.RegisterMessage(AddTimeToCauldronMessage)


# @@protoc_insertion_point(module_scope)
