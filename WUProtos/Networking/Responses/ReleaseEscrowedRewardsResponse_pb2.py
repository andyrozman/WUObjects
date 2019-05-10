# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Responses/ReleaseEscrowedRewardsResponse.proto

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
  name='WUProtos/Networking/Responses/ReleaseEscrowedRewardsResponse.proto',
  package='WUProtos.Networking.Responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nBWUProtos/Networking/Responses/ReleaseEscrowedRewardsResponse.proto\x12\x1dWUProtos.Networking.Responses\x1a\'WUProtos/Data/Loot/LootCollection.proto\"\xbf\x02\n\x1eReleaseEscrowedRewardsResponse\x12T\n\x06status\x18\x01 \x01(\x0e\x32\x44.WUProtos.Networking.Responses.ReleaseEscrowedRewardsResponse.Status\x12;\n\x0f\x63laimed_rewards\x18\x02 \x01(\x0b\x32\".WUProtos.Data.Loot.LootCollection\"\x89\x01\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x11\n\rCLAIM_SUCCESS\x10\x01\x12\x13\n\x0fNO_ESCROW_ERROR\x10\x02\x12\x17\n\x13\x46ULL_CAPACITY_ERROR\x10\x03\x12\x1a\n\x16\x43\x41TEGORY_UNKNOWN_ERROR\x10\x04\x12\x17\n\x13\x41\x42\x41NDON_ALL_SUCCESS\x10\x05\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2.DESCRIPTOR,])



_RELEASEESCROWEDREWARDSRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='WUProtos.Networking.Responses.ReleaseEscrowedRewardsResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLAIM_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_ESCROW_ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FULL_CAPACITY_ERROR', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CATEGORY_UNKNOWN_ERROR', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABANDON_ALL_SUCCESS', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=325,
  serialized_end=462,
)
_sym_db.RegisterEnumDescriptor(_RELEASEESCROWEDREWARDSRESPONSE_STATUS)


_RELEASEESCROWEDREWARDSRESPONSE = _descriptor.Descriptor(
  name='ReleaseEscrowedRewardsResponse',
  full_name='WUProtos.Networking.Responses.ReleaseEscrowedRewardsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='WUProtos.Networking.Responses.ReleaseEscrowedRewardsResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='claimed_rewards', full_name='WUProtos.Networking.Responses.ReleaseEscrowedRewardsResponse.claimed_rewards', index=1,
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
    _RELEASEESCROWEDREWARDSRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=462,
)

_RELEASEESCROWEDREWARDSRESPONSE.fields_by_name['status'].enum_type = _RELEASEESCROWEDREWARDSRESPONSE_STATUS
_RELEASEESCROWEDREWARDSRESPONSE.fields_by_name['claimed_rewards'].message_type = WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2._LOOTCOLLECTION
_RELEASEESCROWEDREWARDSRESPONSE_STATUS.containing_type = _RELEASEESCROWEDREWARDSRESPONSE
DESCRIPTOR.message_types_by_name['ReleaseEscrowedRewardsResponse'] = _RELEASEESCROWEDREWARDSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReleaseEscrowedRewardsResponse = _reflection.GeneratedProtocolMessageType('ReleaseEscrowedRewardsResponse', (_message.Message,), dict(
  DESCRIPTOR = _RELEASEESCROWEDREWARDSRESPONSE,
  __module__ = 'WUProtos.Networking.Responses.ReleaseEscrowedRewardsResponse_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Responses.ReleaseEscrowedRewardsResponse)
  ))
_sym_db.RegisterMessage(ReleaseEscrowedRewardsResponse)


# @@protoc_insertion_point(module_scope)