# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/craft_potion_message.proto

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
  name='wuprotos/networking/requests/messages/craft_potion_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n@wuprotos/networking/requests/messages/craft_potion_message.proto\x12%wuprotos.networking.requests.messages\x1a$wuprotos/data/loot/loot_reward.proto\"\x90\x01\n\x12\x43raftPotionMessage\x12\x15\n\rrecipe_gmt_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63\x61uldron_id\x18\x02 \x01(\x03\x12N\n\x17ingredients_to_purchase\x18\x03 \x01(\x0b\x32-.wuprotos.data.loot.LootReward.LootCollectionb\x06proto3')
  ,
  dependencies=[wuprotos_dot_data_dot_loot_dot_loot__reward__pb2.DESCRIPTOR,])




_CRAFTPOTIONMESSAGE = _descriptor.Descriptor(
  name='CraftPotionMessage',
  full_name='wuprotos.networking.requests.messages.CraftPotionMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='recipe_gmt_id', full_name='wuprotos.networking.requests.messages.CraftPotionMessage.recipe_gmt_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cauldron_id', full_name='wuprotos.networking.requests.messages.CraftPotionMessage.cauldron_id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ingredients_to_purchase', full_name='wuprotos.networking.requests.messages.CraftPotionMessage.ingredients_to_purchase', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=146,
  serialized_end=290,
)

_CRAFTPOTIONMESSAGE.fields_by_name['ingredients_to_purchase'].message_type = wuprotos_dot_data_dot_loot_dot_loot__reward__pb2._LOOTREWARD_LOOTCOLLECTION
DESCRIPTOR.message_types_by_name['CraftPotionMessage'] = _CRAFTPOTIONMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CraftPotionMessage = _reflection.GeneratedProtocolMessageType('CraftPotionMessage', (_message.Message,), dict(
  DESCRIPTOR = _CRAFTPOTIONMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.craft_potion_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.CraftPotionMessage)
  ))
_sym_db.RegisterMessage(CraftPotionMessage)


# @@protoc_insertion_point(module_scope)
