# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Enums/BonusTargetReward.proto

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
  name='WUProtos/Enums/BonusTargetReward.proto',
  package='WUProtos.Enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n&WUProtos/Enums/BonusTargetReward.proto\x12\x0eWUProtos.Enums*\xd1\x01\n\x11\x42onusTargetReward\x12\x1f\n\x1b\x42ONUS_TARGET_REWARD_UNKNOWN\x10\x00\x12 \n\x1c\x43HALLENGE_COLLECTIBLE_SHARDS\x10\x01\x12\x17\n\x13\x43HALLENGE_FAMILY_XP\x10\x02\x12\x19\n\x15PROFESSION_SPELLBOOKS\x10\x03\x12#\n\x1fTRACE_FAMILY_COLLECTIBLE_SHARDS\x10\x04\x12 \n\x1c\x41\x44VERSARY_COLLECTIBLE_SHARDS\x10\x05\x62\x06proto3')
)

_BONUSTARGETREWARD = _descriptor.EnumDescriptor(
  name='BonusTargetReward',
  full_name='WUProtos.Enums.BonusTargetReward',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BONUS_TARGET_REWARD_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_COLLECTIBLE_SHARDS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHALLENGE_FAMILY_XP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROFESSION_SPELLBOOKS', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TRACE_FAMILY_COLLECTIBLE_SHARDS', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ADVERSARY_COLLECTIBLE_SHARDS', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=59,
  serialized_end=268,
)
_sym_db.RegisterEnumDescriptor(_BONUSTARGETREWARD)

BonusTargetReward = enum_type_wrapper.EnumTypeWrapper(_BONUSTARGETREWARD)
BONUS_TARGET_REWARD_UNKNOWN = 0
CHALLENGE_COLLECTIBLE_SHARDS = 1
CHALLENGE_FAMILY_XP = 2
PROFESSION_SPELLBOOKS = 3
TRACE_FAMILY_COLLECTIBLE_SHARDS = 4
ADVERSARY_COLLECTIBLE_SHARDS = 5


DESCRIPTOR.enum_types_by_name['BonusTargetReward'] = _BONUSTARGETREWARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)