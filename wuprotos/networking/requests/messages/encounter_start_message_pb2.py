# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/encounter_start_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/encounter_start_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nCwuprotos/networking/requests/messages/encounter_start_message.proto\x12%wuprotos.networking.requests.messages\"1\n\x15\x45ncounterStartMessage\x12\x18\n\x10\x65ncounter_ticket\x18\x01 \x01(\x0c\x62\x06proto3')
)




_ENCOUNTERSTARTMESSAGE = _descriptor.Descriptor(
  name='EncounterStartMessage',
  full_name='wuprotos.networking.requests.messages.EncounterStartMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encounter_ticket', full_name='wuprotos.networking.requests.messages.EncounterStartMessage.encounter_ticket', index=0,
      number=1, type=12, cpp_type=9, label=1,
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
  serialized_start=110,
  serialized_end=159,
)

DESCRIPTOR.message_types_by_name['EncounterStartMessage'] = _ENCOUNTERSTARTMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EncounterStartMessage = _reflection.GeneratedProtocolMessageType('EncounterStartMessage', (_message.Message,), dict(
  DESCRIPTOR = _ENCOUNTERSTARTMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.encounter_start_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.EncounterStartMessage)
  ))
_sym_db.RegisterMessage(EncounterStartMessage)


# @@protoc_insertion_point(module_scope)
