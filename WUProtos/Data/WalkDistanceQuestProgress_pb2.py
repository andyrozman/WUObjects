# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/WalkDistanceQuestProgress.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/WalkDistanceQuestProgress.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n-WUProtos/Data/WalkDistanceQuestProgress.proto\x12\rWUProtos.Data\"?\n\x19WalkDistanceQuestProgress\x12\"\n\x1a\x63urrent_micrometers_walked\x18\x01 \x01(\x03\x62\x06proto3')
)




_WALKDISTANCEQUESTPROGRESS = _descriptor.Descriptor(
  name='WalkDistanceQuestProgress',
  full_name='WUProtos.Data.WalkDistanceQuestProgress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_micrometers_walked', full_name='WUProtos.Data.WalkDistanceQuestProgress.current_micrometers_walked', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=64,
  serialized_end=127,
)

DESCRIPTOR.message_types_by_name['WalkDistanceQuestProgress'] = _WALKDISTANCEQUESTPROGRESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WalkDistanceQuestProgress = _reflection.GeneratedProtocolMessageType('WalkDistanceQuestProgress', (_message.Message,), dict(
  DESCRIPTOR = _WALKDISTANCEQUESTPROGRESS,
  __module__ = 'WUProtos.Data.WalkDistanceQuestProgress_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.WalkDistanceQuestProgress)
  ))
_sym_db.RegisterMessage(WalkDistanceQuestProgress)


# @@protoc_insertion_point(module_scope)