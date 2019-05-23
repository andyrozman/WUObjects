# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/data/player/player_reputation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/data/player/player_reputation.proto',
  package='wuprotos.data.player',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,wuprotos/data/player/player_reputation.proto\x12\x14wuprotos.data.player\"\xd8\x01\n\x10PlayerReputation\x12\x16\n\x0e\x61\x63\x63ount_age_ms\x18\x01 \x01(\x03\x12\x14\n\x0cplayer_level\x18\x02 \x01(\x03\x12P\n\x10\x63heat_reputation\x18\x03 \x03(\x0e\x32\x36.wuprotos.data.player.PlayerReputation.CheatReputation\x12\x10\n\x08is_minor\x18\x04 \x01(\x08\"2\n\x0f\x43heatReputation\x12\t\n\x05UNSET\x10\x00\x12\x07\n\x03\x42OT\x10\x01\x12\x0b\n\x07SPOOFER\x10\x02\x62\x06proto3')
)



_PLAYERREPUTATION_CHEATREPUTATION = _descriptor.EnumDescriptor(
  name='CheatReputation',
  full_name='wuprotos.data.player.PlayerReputation.CheatReputation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPOOFER', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=237,
  serialized_end=287,
)
_sym_db.RegisterEnumDescriptor(_PLAYERREPUTATION_CHEATREPUTATION)


_PLAYERREPUTATION = _descriptor.Descriptor(
  name='PlayerReputation',
  full_name='wuprotos.data.player.PlayerReputation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_age_ms', full_name='wuprotos.data.player.PlayerReputation.account_age_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_level', full_name='wuprotos.data.player.PlayerReputation.player_level', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cheat_reputation', full_name='wuprotos.data.player.PlayerReputation.cheat_reputation', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_minor', full_name='wuprotos.data.player.PlayerReputation.is_minor', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PLAYERREPUTATION_CHEATREPUTATION,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=287,
)

_PLAYERREPUTATION.fields_by_name['cheat_reputation'].enum_type = _PLAYERREPUTATION_CHEATREPUTATION
_PLAYERREPUTATION_CHEATREPUTATION.containing_type = _PLAYERREPUTATION
DESCRIPTOR.message_types_by_name['PlayerReputation'] = _PLAYERREPUTATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerReputation = _reflection.GeneratedProtocolMessageType('PlayerReputation', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERREPUTATION,
  __module__ = 'wuprotos.data.player.player_reputation_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.data.player.PlayerReputation)
  ))
_sym_db.RegisterMessage(PlayerReputation)


# @@protoc_insertion_point(module_scope)
