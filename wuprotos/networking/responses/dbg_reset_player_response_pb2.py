# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/dbg_reset_player_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/dbg_reset_player_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n=wuprotos/networking/responses/dbg_reset_player_response.proto\x12\x1dwuprotos.networking.responses\")\n\x16\x44\x62gResetPlayerResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x62\x06proto3')
)




_DBGRESETPLAYERRESPONSE = _descriptor.Descriptor(
  name='DbgResetPlayerResponse',
  full_name='wuprotos.networking.responses.DbgResetPlayerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='wuprotos.networking.responses.DbgResetPlayerResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=96,
  serialized_end=137,
)

DESCRIPTOR.message_types_by_name['DbgResetPlayerResponse'] = _DBGRESETPLAYERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DbgResetPlayerResponse = _reflection.GeneratedProtocolMessageType('DbgResetPlayerResponse', (_message.Message,), dict(
  DESCRIPTOR = _DBGRESETPLAYERRESPONSE,
  __module__ = 'wuprotos.networking.responses.dbg_reset_player_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.DbgResetPlayerResponse)
  ))
_sym_db.RegisterMessage(DbgResetPlayerResponse)


# @@protoc_insertion_point(module_scope)
