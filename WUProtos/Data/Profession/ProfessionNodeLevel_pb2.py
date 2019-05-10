# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Profession/ProfessionNodeLevel.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import Requirements_pb2 as WUProtos_dot_Data_dot_Requirements__pb2
from WUProtos.Data.Loot import LootCollection_pb2 as WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Profession/ProfessionNodeLevel.proto',
  package='WUProtos.Data.Profession',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n2WUProtos/Data/Profession/ProfessionNodeLevel.proto\x12\x18WUProtos.Data.Profession\x1a WUProtos/Data/Requirements.proto\x1a\'WUProtos/Data/Loot/LootCollection.proto\"\x8e\x02\n\x13ProfessionNodeLevel\x12\x13\n\x0b\x62uff_gmt_id\x18\x01 \x01(\t\x12\x31\n\x0cprerequisite\x18\x02 \x01(\x0b\x32\x1b.WUProtos.Data.Requirements\x12\x30\n\x04\x63ost\x18\x03 \x01(\x0b\x32\".WUProtos.Data.Loot.LootCollection\x12\x15\n\rmap_abilities\x18\x04 \x03(\t\x12\x13\n\x0brank_points\x18\x05 \x01(\r\"Q\n\x07Purpose\x12\x08\n\x04none\x10\x00\x12\x08\n\x04\x62uff\x10\x01\x12\x19\n\x15learn_new_map_ability\x10\x02\x12\x17\n\x13upgrade_map_ability\x10\x03\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Requirements__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2.DESCRIPTOR,])



_PROFESSIONNODELEVEL_PURPOSE = _descriptor.EnumDescriptor(
  name='Purpose',
  full_name='WUProtos.Data.Profession.ProfessionNodeLevel.Purpose',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='none', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='buff', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='learn_new_map_ability', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='upgrade_map_ability', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=345,
  serialized_end=426,
)
_sym_db.RegisterEnumDescriptor(_PROFESSIONNODELEVEL_PURPOSE)


_PROFESSIONNODELEVEL = _descriptor.Descriptor(
  name='ProfessionNodeLevel',
  full_name='WUProtos.Data.Profession.ProfessionNodeLevel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='buff_gmt_id', full_name='WUProtos.Data.Profession.ProfessionNodeLevel.buff_gmt_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prerequisite', full_name='WUProtos.Data.Profession.ProfessionNodeLevel.prerequisite', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cost', full_name='WUProtos.Data.Profession.ProfessionNodeLevel.cost', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='map_abilities', full_name='WUProtos.Data.Profession.ProfessionNodeLevel.map_abilities', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank_points', full_name='WUProtos.Data.Profession.ProfessionNodeLevel.rank_points', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROFESSIONNODELEVEL_PURPOSE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=156,
  serialized_end=426,
)

_PROFESSIONNODELEVEL.fields_by_name['prerequisite'].message_type = WUProtos_dot_Data_dot_Requirements__pb2._REQUIREMENTS
_PROFESSIONNODELEVEL.fields_by_name['cost'].message_type = WUProtos_dot_Data_dot_Loot_dot_LootCollection__pb2._LOOTCOLLECTION
_PROFESSIONNODELEVEL_PURPOSE.containing_type = _PROFESSIONNODELEVEL
DESCRIPTOR.message_types_by_name['ProfessionNodeLevel'] = _PROFESSIONNODELEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProfessionNodeLevel = _reflection.GeneratedProtocolMessageType('ProfessionNodeLevel', (_message.Message,), dict(
  DESCRIPTOR = _PROFESSIONNODELEVEL,
  __module__ = 'WUProtos.Data.Profession.ProfessionNodeLevel_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Profession.ProfessionNodeLevel)
  ))
_sym_db.RegisterMessage(ProfessionNodeLevel)


# @@protoc_insertion_point(module_scope)