# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/dbg_start_encounter_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/dbg_start_encounter_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nGwuprotos/networking/requests/messages/dbg_start_encounter_message.proto\x12%wuprotos.networking.requests.messages\"a\n\x18\x44\x62gStartEncounterMessage\x12\x18\n\x10\x65ncounter_gmt_id\x18\x01 \x01(\t\x12\x1c\n\x14starting_stage_index\x18\x02 \x01(\x05\x12\r\n\x05level\x18\x03 \x01(\x05\x62\x06proto3')
)




_DBGSTARTENCOUNTERMESSAGE = _descriptor.Descriptor(
  name='DbgStartEncounterMessage',
  full_name='wuprotos.networking.requests.messages.DbgStartEncounterMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encounter_gmt_id', full_name='wuprotos.networking.requests.messages.DbgStartEncounterMessage.encounter_gmt_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='starting_stage_index', full_name='wuprotos.networking.requests.messages.DbgStartEncounterMessage.starting_stage_index', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='wuprotos.networking.requests.messages.DbgStartEncounterMessage.level', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_end=211,
)

DESCRIPTOR.message_types_by_name['DbgStartEncounterMessage'] = _DBGSTARTENCOUNTERMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DbgStartEncounterMessage = _reflection.GeneratedProtocolMessageType('DbgStartEncounterMessage', (_message.Message,), dict(
  DESCRIPTOR = _DBGSTARTENCOUNTERMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.dbg_start_encounter_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.DbgStartEncounterMessage)
  ))
_sym_db.RegisterMessage(DbgStartEncounterMessage)


# @@protoc_insertion_point(module_scope)
