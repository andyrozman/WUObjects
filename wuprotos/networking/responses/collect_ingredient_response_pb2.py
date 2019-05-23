# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/collect_ingredient_response.proto

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
  name='wuprotos/networking/responses/collect_ingredient_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n?wuprotos/networking/responses/collect_ingredient_response.proto\x12\x1dwuprotos.networking.responses\x1a$wuprotos/data/loot/loot_reward.proto\"\xbe\x02\n\x19\x43ollectIngredientResponse\x12`\n\x06result\x18\x01 \x01(\x0e\x32P.wuprotos.networking.responses.CollectIngredientResponse.CollectIngredientResult\x12>\n\x07rewards\x18\x02 \x01(\x0b\x32-.wuprotos.data.loot.LootReward.LootCollection\"\x7f\n\x17\x43ollectIngredientResult\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0e\n\nBAD_TICKET\x10\x02\x12\x10\n\x0cNOT_IN_RANGE\x10\x03\x12\x15\n\x11\x41LREADY_COLLECTED\x10\x04\x12\x11\n\rFULL_CAPACITY\x10\x05\x62\x06proto3')
  ,
  dependencies=[wuprotos_dot_data_dot_loot_dot_loot__reward__pb2.DESCRIPTOR,])



_COLLECTINGREDIENTRESPONSE_COLLECTINGREDIENTRESULT = _descriptor.EnumDescriptor(
  name='CollectIngredientResult',
  full_name='wuprotos.networking.responses.CollectIngredientResponse.CollectIngredientResult',
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
      name='BAD_TICKET', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NOT_IN_RANGE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALREADY_COLLECTED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL_CAPACITY', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=328,
  serialized_end=455,
)
_sym_db.RegisterEnumDescriptor(_COLLECTINGREDIENTRESPONSE_COLLECTINGREDIENTRESULT)


_COLLECTINGREDIENTRESPONSE = _descriptor.Descriptor(
  name='CollectIngredientResponse',
  full_name='wuprotos.networking.responses.CollectIngredientResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='wuprotos.networking.responses.CollectIngredientResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rewards', full_name='wuprotos.networking.responses.CollectIngredientResponse.rewards', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COLLECTINGREDIENTRESPONSE_COLLECTINGREDIENTRESULT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=455,
)

_COLLECTINGREDIENTRESPONSE.fields_by_name['result'].enum_type = _COLLECTINGREDIENTRESPONSE_COLLECTINGREDIENTRESULT
_COLLECTINGREDIENTRESPONSE.fields_by_name['rewards'].message_type = wuprotos_dot_data_dot_loot_dot_loot__reward__pb2._LOOTREWARD_LOOTCOLLECTION
_COLLECTINGREDIENTRESPONSE_COLLECTINGREDIENTRESULT.containing_type = _COLLECTINGREDIENTRESPONSE
DESCRIPTOR.message_types_by_name['CollectIngredientResponse'] = _COLLECTINGREDIENTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectIngredientResponse = _reflection.GeneratedProtocolMessageType('CollectIngredientResponse', (_message.Message,), dict(
  DESCRIPTOR = _COLLECTINGREDIENTRESPONSE,
  __module__ = 'wuprotos.networking.responses.collect_ingredient_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.CollectIngredientResponse)
  ))
_sym_db.RegisterMessage(CollectIngredientResponse)


# @@protoc_insertion_point(module_scope)
