# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/RunestoneVaultItem.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/RunestoneVaultItem.proto',
  package='WUProtos.Data',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&WUProtos/Data/RunestoneVaultItem.proto\x12\rWUProtos.Data\"X\n\x12RunestoneVaultItem\x12\x0f\n\x07quality\x18\x01 \x01(\x05\x12\x0f\n\x07is_boss\x18\x02 \x01(\x08\x12 \n\x18\x63ollection_family_gmt_id\x18\x03 \x01(\tb\x06proto3')
)




_RUNESTONEVAULTITEM = _descriptor.Descriptor(
  name='RunestoneVaultItem',
  full_name='WUProtos.Data.RunestoneVaultItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='quality', full_name='WUProtos.Data.RunestoneVaultItem.quality', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_boss', full_name='WUProtos.Data.RunestoneVaultItem.is_boss', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='collection_family_gmt_id', full_name='WUProtos.Data.RunestoneVaultItem.collection_family_gmt_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=57,
  serialized_end=145,
)

DESCRIPTOR.message_types_by_name['RunestoneVaultItem'] = _RUNESTONEVAULTITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RunestoneVaultItem = _reflection.GeneratedProtocolMessageType('RunestoneVaultItem', (_message.Message,), dict(
  DESCRIPTOR = _RUNESTONEVAULTITEM,
  __module__ = 'WUProtos.Data.RunestoneVaultItem_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.RunestoneVaultItem)
  ))
_sym_db.RegisterMessage(RunestoneVaultItem)


# @@protoc_insertion_point(module_scope)