# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/use_portkey_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wuprotos.data.loot import loot_reward_pb2 as wuprotos_dot_data_dot_loot_dot_loot__reward__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/use_portkey_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n8wuprotos/networking/responses/use_portkey_response.proto\x12\x1dwuprotos.networking.responses\x1a$wuprotos/data/loot/loot_reward.proto\"\xf4\x04\n\x12UsePortkeyResponse\x12H\n\x06status\x18\x01 \x01(\x0e\x32\x38.wuprotos.networking.responses.UsePortkeyResponse.Status\x12\x46\n\x0fportkey_rewards\x18\x02 \x01(\x0b\x32-.wuprotos.data.loot.LootReward.LootCollection\x12n\n\x17\x61ll_bonus_nodes_rewards\x18\x04 \x03(\x0b\x32M.wuprotos.networking.responses.UsePortkeyResponse.PortkeyBonusGameNodeRewards\x1a\x97\x02\n\x1bPortkeyBonusGameNodeRewards\x12z\n\x07rewards\x18\x01 \x03(\x0b\x32i.wuprotos.networking.responses.UsePortkeyResponse.PortkeyBonusGameNodeRewards.PortkeyBonusGameRewardTuple\x1a|\n\x1bPortkeyBonusGameRewardTuple\x12.\n\x06reward\x18\x01 \x01(\x0b\x32\x1e.wuprotos.data.loot.LootReward\x12\x12\n\nmultiplier\x18\x02 \x01(\x02\x12\x19\n\x11\x63\x61tegory_proto_id\x18\x03 \x01(\t\"B\n\x06Status\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\x13\n\x0fINVALID_PORTKEY\x10\x03\x62\x06proto3')
  ,
  dependencies=[wuprotos_dot_data_dot_loot_dot_loot__reward__pb2.DESCRIPTOR,])



_USEPORTKEYRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='wuprotos.networking.responses.UsePortkeyResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PORTKEY', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=692,
  serialized_end=758,
)
_sym_db.RegisterEnumDescriptor(_USEPORTKEYRESPONSE_STATUS)


_USEPORTKEYRESPONSE_PORTKEYBONUSGAMENODEREWARDS_PORTKEYBONUSGAMEREWARDTUPLE = _descriptor.Descriptor(
  name='PortkeyBonusGameRewardTuple',
  full_name='wuprotos.networking.responses.UsePortkeyResponse.PortkeyBonusGameNodeRewards.PortkeyBonusGameRewardTuple',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reward', full_name='wuprotos.networking.responses.UsePortkeyResponse.PortkeyBonusGameNodeRewards.PortkeyBonusGameRewardTuple.reward', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multiplier', full_name='wuprotos.networking.responses.UsePortkeyResponse.PortkeyBonusGameNodeRewards.PortkeyBonusGameRewardTuple.multiplier', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category_proto_id', full_name='wuprotos.networking.responses.UsePortkeyResponse.PortkeyBonusGameNodeRewards.PortkeyBonusGameRewardTuple.category_proto_id', index=2,
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
  serialized_start=566,
  serialized_end=690,
)

_USEPORTKEYRESPONSE_PORTKEYBONUSGAMENODEREWARDS = _descriptor.Descriptor(
  name='PortkeyBonusGameNodeRewards',
  full_name='wuprotos.networking.responses.UsePortkeyResponse.PortkeyBonusGameNodeRewards',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rewards', full_name='wuprotos.networking.responses.UsePortkeyResponse.PortkeyBonusGameNodeRewards.rewards', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_USEPORTKEYRESPONSE_PORTKEYBONUSGAMENODEREWARDS_PORTKEYBONUSGAMEREWARDTUPLE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=690,
)

_USEPORTKEYRESPONSE = _descriptor.Descriptor(
  name='UsePortkeyResponse',
  full_name='wuprotos.networking.responses.UsePortkeyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wuprotos.networking.responses.UsePortkeyResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portkey_rewards', full_name='wuprotos.networking.responses.UsePortkeyResponse.portkey_rewards', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='all_bonus_nodes_rewards', full_name='wuprotos.networking.responses.UsePortkeyResponse.all_bonus_nodes_rewards', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_USEPORTKEYRESPONSE_PORTKEYBONUSGAMENODEREWARDS, ],
  enum_types=[
    _USEPORTKEYRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=758,
)

_USEPORTKEYRESPONSE_PORTKEYBONUSGAMENODEREWARDS_PORTKEYBONUSGAMEREWARDTUPLE.fields_by_name['reward'].message_type = wuprotos_dot_data_dot_loot_dot_loot__reward__pb2._LOOTREWARD
_USEPORTKEYRESPONSE_PORTKEYBONUSGAMENODEREWARDS_PORTKEYBONUSGAMEREWARDTUPLE.containing_type = _USEPORTKEYRESPONSE_PORTKEYBONUSGAMENODEREWARDS
_USEPORTKEYRESPONSE_PORTKEYBONUSGAMENODEREWARDS.fields_by_name['rewards'].message_type = _USEPORTKEYRESPONSE_PORTKEYBONUSGAMENODEREWARDS_PORTKEYBONUSGAMEREWARDTUPLE
_USEPORTKEYRESPONSE_PORTKEYBONUSGAMENODEREWARDS.containing_type = _USEPORTKEYRESPONSE
_USEPORTKEYRESPONSE.fields_by_name['status'].enum_type = _USEPORTKEYRESPONSE_STATUS
_USEPORTKEYRESPONSE.fields_by_name['portkey_rewards'].message_type = wuprotos_dot_data_dot_loot_dot_loot__reward__pb2._LOOTREWARD_LOOTCOLLECTION
_USEPORTKEYRESPONSE.fields_by_name['all_bonus_nodes_rewards'].message_type = _USEPORTKEYRESPONSE_PORTKEYBONUSGAMENODEREWARDS
_USEPORTKEYRESPONSE_STATUS.containing_type = _USEPORTKEYRESPONSE
DESCRIPTOR.message_types_by_name['UsePortkeyResponse'] = _USEPORTKEYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UsePortkeyResponse = _reflection.GeneratedProtocolMessageType('UsePortkeyResponse', (_message.Message,), dict(

  PortkeyBonusGameNodeRewards = _reflection.GeneratedProtocolMessageType('PortkeyBonusGameNodeRewards', (_message.Message,), dict(

    PortkeyBonusGameRewardTuple = _reflection.GeneratedProtocolMessageType('PortkeyBonusGameRewardTuple', (_message.Message,), dict(
      DESCRIPTOR = _USEPORTKEYRESPONSE_PORTKEYBONUSGAMENODEREWARDS_PORTKEYBONUSGAMEREWARDTUPLE,
      __module__ = 'wuprotos.networking.responses.use_portkey_response_pb2'
      # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.UsePortkeyResponse.PortkeyBonusGameNodeRewards.PortkeyBonusGameRewardTuple)
      ))
    ,
    DESCRIPTOR = _USEPORTKEYRESPONSE_PORTKEYBONUSGAMENODEREWARDS,
    __module__ = 'wuprotos.networking.responses.use_portkey_response_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.UsePortkeyResponse.PortkeyBonusGameNodeRewards)
    ))
  ,
  DESCRIPTOR = _USEPORTKEYRESPONSE,
  __module__ = 'wuprotos.networking.responses.use_portkey_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.UsePortkeyResponse)
  ))
_sym_db.RegisterMessage(UsePortkeyResponse)
_sym_db.RegisterMessage(UsePortkeyResponse.PortkeyBonusGameNodeRewards)
_sym_db.RegisterMessage(UsePortkeyResponse.PortkeyBonusGameNodeRewards.PortkeyBonusGameRewardTuple)


# @@protoc_insertion_point(module_scope)
