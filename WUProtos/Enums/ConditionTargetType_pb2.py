# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Enums/ConditionTargetType.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Enums/ConditionTargetType.proto',
  package='WUProtos.Enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(WUProtos/Enums/ConditionTargetType.proto\x12\x0eWUProtos.Enums*N\n\x13\x43onditionTargetType\x12\x1f\n\x1b\x43ONDITION_TARGET_TYPE_UNSET\x10\x00\x12\x08\n\x04SELF\x10\x01\x12\x0c\n\x08OPPONENT\x10\x02\x62\x06proto3')
)

_CONDITIONTARGETTYPE = _descriptor.EnumDescriptor(
  name='ConditionTargetType',
  full_name='WUProtos.Enums.ConditionTargetType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CONDITION_TARGET_TYPE_UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SELF', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OPPONENT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=60,
  serialized_end=138,
)
_sym_db.RegisterEnumDescriptor(_CONDITIONTARGETTYPE)

ConditionTargetType = enum_type_wrapper.EnumTypeWrapper(_CONDITIONTARGETTYPE)
CONDITION_TARGET_TYPE_UNSET = 0
SELF = 1
OPPONENT = 2


DESCRIPTOR.enum_types_by_name['ConditionTargetType'] = _CONDITIONTARGETTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)