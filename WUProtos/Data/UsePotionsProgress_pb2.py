# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/UsePotionsProgress.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/UsePotionsProgress.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&WUProtos/Data/UsePotionsProgress.proto\x12\rWUProtos.Data\"/\n\x12UsePotionsProgress\x12\x19\n\x11\x63urrent_use_count\x18\x01 \x01(\x03\x62\x06proto3')
)




_USEPOTIONSPROGRESS = _descriptor.Descriptor(
  name='UsePotionsProgress',
  full_name='WUProtos.Data.UsePotionsProgress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_use_count', full_name='WUProtos.Data.UsePotionsProgress.current_use_count', index=0,
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
  serialized_start=57,
  serialized_end=104,
)

DESCRIPTOR.message_types_by_name['UsePotionsProgress'] = _USEPOTIONSPROGRESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UsePotionsProgress = _reflection.GeneratedProtocolMessageType('UsePotionsProgress', (_message.Message,), dict(
  DESCRIPTOR = _USEPOTIONSPROGRESS,
  __module__ = 'WUProtos.Data.UsePotionsProgress_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.UsePotionsProgress)
  ))
_sym_db.RegisterMessage(UsePotionsProgress)


# @@protoc_insertion_point(module_scope)