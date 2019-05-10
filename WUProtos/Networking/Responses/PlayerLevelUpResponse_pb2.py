# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Responses/PlayerLevelUpResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Loot import LootCollection_pb2 as WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Responses/PlayerLevelUpResponse.proto',
  package='WUProtos.Networking.Responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n9WUProtos/Networking/Responses/PlayerLevelUpResponse.proto\x12\x1dWUProtos.Networking.Responses\x1a\'WUProtos/Data/Loot/LootCollection.proto\"}\n\x15PlayerLevelUpResponse\x12\x14\n\x0c\x64id_level_up\x18\x01 \x01(\x08\x12\x11\n\tnew_level\x18\x02 \x01(\x05\x12;\n\x0fgranted_rewards\x18\x03 \x01(\x0b\x32\".WUProtos.Data.Loot.LootCollectionb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2.DESCRIPTOR,])




_PLAYERLEVELUPRESPONSE = _descriptor.Descriptor(
  name='PlayerLevelUpResponse',
  full_name='WUProtos.Networking.Responses.PlayerLevelUpResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='did_level_up', full_name='WUProtos.Networking.Responses.PlayerLevelUpResponse.did_level_up', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_level', full_name='WUProtos.Networking.Responses.PlayerLevelUpResponse.new_level', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='granted_rewards', full_name='WUProtos.Networking.Responses.PlayerLevelUpResponse.granted_rewards', index=2,
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
  serialized_start=133,
  serialized_end=258,
)

_PLAYERLEVELUPRESPONSE.fields_by_name['granted_rewards'].message_type = WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2._LOOTCOLLECTION
DESCRIPTOR.message_types_by_name['PlayerLevelUpResponse'] = _PLAYERLEVELUPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlayerLevelUpResponse = _reflection.GeneratedProtocolMessageType('PlayerLevelUpResponse', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERLEVELUPRESPONSE,
  __module__ = 'WUProtos.Networking.Responses.PlayerLevelUpResponse_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Responses.PlayerLevelUpResponse)
  ))
_sym_db.RegisterMessage(PlayerLevelUpResponse)


# @@protoc_insertion_point(module_scope)