# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/use_potion_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/use_potion_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n>wuprotos/networking/requests/messages/use_potion_message.proto\x12%wuprotos.networking.requests.messages\"%\n\x10UsePotionMessage\x12\x11\n\tpotion_id\x18\x01 \x01(\tb\x06proto3')
)




_USEPOTIONMESSAGE = _descriptor.Descriptor(
  name='UsePotionMessage',
  full_name='wuprotos.networking.requests.messages.UsePotionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='potion_id', full_name='wuprotos.networking.requests.messages.UsePotionMessage.potion_id', index=0,
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
  serialized_start=105,
  serialized_end=142,
)

DESCRIPTOR.message_types_by_name['UsePotionMessage'] = _USEPOTIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UsePotionMessage = _reflection.GeneratedProtocolMessageType('UsePotionMessage', (_message.Message,), dict(
  DESCRIPTOR = _USEPOTIONMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.use_potion_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.UsePotionMessage)
  ))
_sym_db.RegisterMessage(UsePotionMessage)


# @@protoc_insertion_point(module_scope)
