# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/RpgstatsBlock.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/RpgstatsBlock.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!WUProtos/Data/RpgstatsBlock.proto\x12\rWUProtos.Data\"\x1b\n\rRpgstatsBlock\x12\n\n\x02id\x18\x01 \x01(\tb\x06proto3')
)




_RPGSTATSBLOCK = _descriptor.Descriptor(
  name='RpgstatsBlock',
  full_name='WUProtos.Data.RpgstatsBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.RpgstatsBlock.id', index=0,
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
  serialized_start=52,
  serialized_end=79,
)

DESCRIPTOR.message_types_by_name['RpgstatsBlock'] = _RPGSTATSBLOCK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RpgstatsBlock = _reflection.GeneratedProtocolMessageType('RpgstatsBlock', (_message.Message,), dict(
  DESCRIPTOR = _RPGSTATSBLOCK,
  __module__ = 'WUProtos.Data.RpgstatsBlock_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.RpgstatsBlock)
  ))
_sym_db.RegisterMessage(RpgstatsBlock)


# @@protoc_insertion_point(module_scope)