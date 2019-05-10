# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Combat/CombatGrowth.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Enums import GrowthType_pb2 as WUProtos_dot_Enums_dot_GrowthType__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Combat/CombatGrowth.proto',
  package='WUProtos.Data.Combat',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\'WUProtos/Data/Combat/CombatGrowth.proto\x12\x14WUProtos.Data.Combat\x1a\x1fWUProtos/Enums/GrowthType.proto\"X\n\x0c\x43ombatGrowth\x12-\n\tgrow_type\x18\x01 \x01(\x0e\x32\x1a.WUProtos.Enums.GrowthType\x12\x19\n\x11growth_adjustment\x18\x02 \x01(\x02\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Enums_dot_GrowthType__pb2.DESCRIPTOR,])




_COMBATGROWTH = _descriptor.Descriptor(
  name='CombatGrowth',
  full_name='WUProtos.Data.Combat.CombatGrowth',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='grow_type', full_name='WUProtos.Data.Combat.CombatGrowth.grow_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='growth_adjustment', full_name='WUProtos.Data.Combat.CombatGrowth.growth_adjustment', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=98,
  serialized_end=186,
)

_COMBATGROWTH.fields_by_name['grow_type'].enum_type = WUProtos_dot_Enums_dot_GrowthType__pb2._GROWTHTYPE
DESCRIPTOR.message_types_by_name['CombatGrowth'] = _COMBATGROWTH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatGrowth = _reflection.GeneratedProtocolMessageType('CombatGrowth', (_message.Message,), dict(
  DESCRIPTOR = _COMBATGROWTH,
  __module__ = 'WUProtos.Data.Combat.CombatGrowth_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Combat.CombatGrowth)
  ))
_sym_db.RegisterMessage(CombatGrowth)


# @@protoc_insertion_point(module_scope)