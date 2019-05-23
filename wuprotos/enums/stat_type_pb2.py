# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/enums/stat_type.proto

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
  name='wuprotos/enums/stat_type.proto',
  package='wuprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1ewuprotos/enums/stat_type.proto\x12\x0ewuprotos.enums*\xf4\x05\n\x08StatType\x12\x10\n\x0cSTAT_UNKNOWN\x10\x00\x12\x12\n\x0eSTAT_COMBAT_HP\x10\x01\x12\x16\n\x12STAT_COMBAT_ATTACK\x10\x02\x12\x1d\n\x19PLAYER_STAT_XP_MULTIPLIER\x10\x03\x12\"\n\x1ePLAYER_STAT_COMBAT_CRIT_CHANCE\x10\x04\x12\"\n\x1ePLAYER_STAT_COMBAT_CRIT_DAMAGE\x10\x05\x12#\n\x1fPLAYER_STAT_COMBAT_BLOCK_AMOUNT\x10\x06\x12.\n*PLAYER_STAT_SPELLCAST_SUCCESS_CHANCE_BOOST\x10\x07\x12#\n\x1fPLAYER_STAT_FLEE_CHANCE_DEBOOST\x10\x08\x12 \n\x1cMAP_ABILITY_COOLDOWN_TIME_MS\x10\t\x12\x1f\n\x1bSTAT_COMBAT_HP_HEAL_PERCENT\x10\n\x12!\n\x1dSTAT_COMBAT_ATTACK_MULTIPLIER\x10\x0b\x12\x1e\n\x1aSTAT_COMBAT_HP_HEAL_AMOUNT\x10\x0c\x12\x1e\n\x1aSTAT_COMBAT_AFFINITY_POWER\x10\r\x12\x1f\n\x1bSTAT_COMBAT_AFFINITY_RESIST\x10\x0e\x12\x1a\n\x16STAT_COMBAT_MITIGATION\x10\x0f\x12\x16\n\x12STAT_COMBAT_SUNDER\x10\x10\x12\x15\n\x11STAT_COMBAT_DODGE\x10\x11\x12\x19\n\x15STAT_COMBAT_PRECISION\x10\x12\x12(\n$STAT_COMBAT_REVIVE_WITH_HEAL_PERCENT\x10\x13\x12\x15\n\x11STAT_COMBAT_FOCUS\x10\x14\x12\x1e\n\x1aSTAT_COMBAT_STARTING_FOCUS\x10\x15\x12\x1b\n\x17STAT_COMBAT_FOCUS_BONUS\x10\x16\x12\x1e\n\x1aSTAT_COMBAT_FOCUS_TRANSFER\x10\x17\x62\x06proto3')
)

_STATTYPE = _descriptor.EnumDescriptor(
  name='StatType',
  full_name='wuprotos.enums.StatType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STAT_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAT_COMBAT_HP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAT_COMBAT_ATTACK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_STAT_XP_MULTIPLIER', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_STAT_COMBAT_CRIT_CHANCE', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_STAT_COMBAT_CRIT_DAMAGE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_STAT_COMBAT_BLOCK_AMOUNT', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_STAT_SPELLCAST_SUCCESS_CHANCE_BOOST', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PLAYER_STAT_FLEE_CHANCE_DEBOOST', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAP_ABILITY_COOLDOWN_TIME_MS', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAT_COMBAT_HP_HEAL_PERCENT', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAT_COMBAT_ATTACK_MULTIPLIER', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAT_COMBAT_HP_HEAL_AMOUNT', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAT_COMBAT_AFFINITY_POWER', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAT_COMBAT_AFFINITY_RESIST', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAT_COMBAT_MITIGATION', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAT_COMBAT_SUNDER', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAT_COMBAT_DODGE', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAT_COMBAT_PRECISION', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAT_COMBAT_REVIVE_WITH_HEAL_PERCENT', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAT_COMBAT_FOCUS', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAT_COMBAT_STARTING_FOCUS', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAT_COMBAT_FOCUS_BONUS', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAT_COMBAT_FOCUS_TRANSFER', index=23, number=23,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=51,
  serialized_end=807,
)
_sym_db.RegisterEnumDescriptor(_STATTYPE)

StatType = enum_type_wrapper.EnumTypeWrapper(_STATTYPE)
STAT_UNKNOWN = 0
STAT_COMBAT_HP = 1
STAT_COMBAT_ATTACK = 2
PLAYER_STAT_XP_MULTIPLIER = 3
PLAYER_STAT_COMBAT_CRIT_CHANCE = 4
PLAYER_STAT_COMBAT_CRIT_DAMAGE = 5
PLAYER_STAT_COMBAT_BLOCK_AMOUNT = 6
PLAYER_STAT_SPELLCAST_SUCCESS_CHANCE_BOOST = 7
PLAYER_STAT_FLEE_CHANCE_DEBOOST = 8
MAP_ABILITY_COOLDOWN_TIME_MS = 9
STAT_COMBAT_HP_HEAL_PERCENT = 10
STAT_COMBAT_ATTACK_MULTIPLIER = 11
STAT_COMBAT_HP_HEAL_AMOUNT = 12
STAT_COMBAT_AFFINITY_POWER = 13
STAT_COMBAT_AFFINITY_RESIST = 14
STAT_COMBAT_MITIGATION = 15
STAT_COMBAT_SUNDER = 16
STAT_COMBAT_DODGE = 17
STAT_COMBAT_PRECISION = 18
STAT_COMBAT_REVIVE_WITH_HEAL_PERCENT = 19
STAT_COMBAT_FOCUS = 20
STAT_COMBAT_STARTING_FOCUS = 21
STAT_COMBAT_FOCUS_BONUS = 22
STAT_COMBAT_FOCUS_TRANSFER = 23


DESCRIPTOR.enum_types_by_name['StatType'] = _STATTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
