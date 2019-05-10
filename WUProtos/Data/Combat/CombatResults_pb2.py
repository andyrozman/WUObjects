# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Combat/CombatResults.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import TempClientStatsHelper_pb2 as WUProtos_dot_Data_dot_TempClientStatsHelper__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Combat/CombatResults.proto',
  package='WUProtos.Data.Combat',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(WUProtos/Data/Combat/CombatResults.proto\x12\x14WUProtos.Data.Combat\x1a)WUProtos/Data/TempClientStatsHelper.proto\"\xa8\x02\n\rCombatResults\x12\x1b\n\x13\x63urrent_state_index\x18\x01 \x01(\x03\x12\x14\n\x0c\x63urrent_crit\x18\x02 \x01(\x08\x12\x18\n\x10next_state_index\x18\x03 \x01(\x03\x12\x11\n\tnext_crit\x18\x04 \x01(\x08\x12\x18\n\x10hp_current_enemy\x18\x05 \x01(\x03\x12\x19\n\x11hp_current_player\x18\x06 \x01(\x03\x12\r\n\x05level\x18\x07 \x01(\x05\x12\x14\n\x0c\x65nemy_dodges\x18\x08 \x01(\x08\x12\x15\n\rplayer_dodges\x18\t \x01(\x08\x12\x46\n\x18temp_client_stats_helper\x18\x64 \x01(\x0b\x32$.WUProtos.Data.TempClientStatsHelperb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_TempClientStatsHelper__pb2.DESCRIPTOR,])




_COMBATRESULTS = _descriptor.Descriptor(
  name='CombatResults',
  full_name='WUProtos.Data.Combat.CombatResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_state_index', full_name='WUProtos.Data.Combat.CombatResults.current_state_index', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_crit', full_name='WUProtos.Data.Combat.CombatResults.current_crit', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_state_index', full_name='WUProtos.Data.Combat.CombatResults.next_state_index', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='next_crit', full_name='WUProtos.Data.Combat.CombatResults.next_crit', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hp_current_enemy', full_name='WUProtos.Data.Combat.CombatResults.hp_current_enemy', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hp_current_player', full_name='WUProtos.Data.Combat.CombatResults.hp_current_player', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level', full_name='WUProtos.Data.Combat.CombatResults.level', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enemy_dodges', full_name='WUProtos.Data.Combat.CombatResults.enemy_dodges', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_dodges', full_name='WUProtos.Data.Combat.CombatResults.player_dodges', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='temp_client_stats_helper', full_name='WUProtos.Data.Combat.CombatResults.temp_client_stats_helper', index=9,
      number=100, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=110,
  serialized_end=406,
)

_COMBATRESULTS.fields_by_name['temp_client_stats_helper'].message_type = WUProtos_dot_Data_dot_TempClientStatsHelper__pb2._TEMPCLIENTSTATSHELPER
DESCRIPTOR.message_types_by_name['CombatResults'] = _COMBATRESULTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CombatResults = _reflection.GeneratedProtocolMessageType('CombatResults', (_message.Message,), dict(
  DESCRIPTOR = _COMBATRESULTS,
  __module__ = 'WUProtos.Data.Combat.CombatResults_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Combat.CombatResults)
  ))
_sym_db.RegisterMessage(CombatResults)


# @@protoc_insertion_point(module_scope)