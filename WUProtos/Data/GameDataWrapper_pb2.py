# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/GameDataWrapper.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import GmTemplate_pb2 as WUProtos_dot_Data_dot_GmTemplate__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/GameDataWrapper.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n#WUProtos/Data/GameDataWrapper.proto\x12\rWUProtos.Data\x1a\x1eWUProtos/Data/GmTemplate.proto\"k\n\x0fGameDataWrapper\x12+\n\x08messages\x18\x01 \x03(\x0b\x32\x19.WUProtos.Data.GmTemplate\x12\x16\n\x0e\x62\x61sis_batch_id\x18\x02 \x01(\x03\x12\x13\n\x0b\x65nvironment\x18\x03 \x01(\x03\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_GmTemplate__pb2.DESCRIPTOR,])




_GAMEDATAWRAPPER = _descriptor.Descriptor(
  name='GameDataWrapper',
  full_name='WUProtos.Data.GameDataWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='WUProtos.Data.GameDataWrapper.messages', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='basis_batch_id', full_name='WUProtos.Data.GameDataWrapper.basis_batch_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='environment', full_name='WUProtos.Data.GameDataWrapper.environment', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=86,
  serialized_end=193,
)

_GAMEDATAWRAPPER.fields_by_name['messages'].message_type = WUProtos_dot_Data_dot_GmTemplate__pb2._GMTEMPLATE
DESCRIPTOR.message_types_by_name['GameDataWrapper'] = _GAMEDATAWRAPPER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameDataWrapper = _reflection.GeneratedProtocolMessageType('GameDataWrapper', (_message.Message,), dict(
  DESCRIPTOR = _GAMEDATAWRAPPER,
  __module__ = 'WUProtos.Data.GameDataWrapper_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.GameDataWrapper)
  ))
_sym_db.RegisterMessage(GameDataWrapper)


# @@protoc_insertion_point(module_scope)