# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Collection/CollectionItemReward.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Collection/CollectionItemReward.proto',
  package='WUProtos.Data.Collection',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n3WUProtos/Data/Collection/CollectionItemReward.proto\x12\x18WUProtos.Data.Collection\"<\n\x14\x43ollectionItemReward\x12\x0f\n\x07item_id\x18\x01 \x01(\t\x12\x13\n\x0bshard_count\x18\x02 \x01(\rb\x06proto3')
)




_COLLECTIONITEMREWARD = _descriptor.Descriptor(
  name='CollectionItemReward',
  full_name='WUProtos.Data.Collection.CollectionItemReward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='WUProtos.Data.Collection.CollectionItemReward.item_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='shard_count', full_name='WUProtos.Data.Collection.CollectionItemReward.shard_count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=81,
  serialized_end=141,
)

DESCRIPTOR.message_types_by_name['CollectionItemReward'] = _COLLECTIONITEMREWARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectionItemReward = _reflection.GeneratedProtocolMessageType('CollectionItemReward', (_message.Message,), dict(
  DESCRIPTOR = _COLLECTIONITEMREWARD,
  __module__ = 'WUProtos.Data.Collection.CollectionItemReward_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Collection.CollectionItemReward)
  ))
_sym_db.RegisterMessage(CollectionItemReward)


# @@protoc_insertion_point(module_scope)