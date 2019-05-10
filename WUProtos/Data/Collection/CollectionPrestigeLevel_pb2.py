# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Collection/CollectionPrestigeLevel.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import Color_pb2 as WUProtos_dot_Data_dot_Color__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Collection/CollectionPrestigeLevel.proto',
  package='WUProtos.Data.Collection',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n6WUProtos/Data/Collection/CollectionPrestigeLevel.proto\x12\x18WUProtos.Data.Collection\x1a\x19WUProtos/Data/Color.proto\"\xc6\x01\n\x17\x43ollectionPrestigeLevel\x12\x14\n\x0c\x62order_image\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12#\n\x05\x63olor\x18\x03 \x01(\x0b\x32\x14.WUProtos.Data.Color\x12\x13\n\x0bis_metallic\x18\x04 \x01(\x08\x12\x12\n\nframe_mesh\x18\x05 \x01(\t\x12\x12\n\nnormal_map\x18\x06 \x01(\t\x12\x12\n\nalbedo_map\x18\x07 \x01(\t\x12\x11\n\troughness\x18\x08 \x01(\x02\x62\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Color__pb2.DESCRIPTOR,])




_COLLECTIONPRESTIGELEVEL = _descriptor.Descriptor(
  name='CollectionPrestigeLevel',
  full_name='WUProtos.Data.Collection.CollectionPrestigeLevel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='border_image', full_name='WUProtos.Data.Collection.CollectionPrestigeLevel.border_image', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='WUProtos.Data.Collection.CollectionPrestigeLevel.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='WUProtos.Data.Collection.CollectionPrestigeLevel.color', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_metallic', full_name='WUProtos.Data.Collection.CollectionPrestigeLevel.is_metallic', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='frame_mesh', full_name='WUProtos.Data.Collection.CollectionPrestigeLevel.frame_mesh', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='normal_map', full_name='WUProtos.Data.Collection.CollectionPrestigeLevel.normal_map', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='albedo_map', full_name='WUProtos.Data.Collection.CollectionPrestigeLevel.albedo_map', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='roughness', full_name='WUProtos.Data.Collection.CollectionPrestigeLevel.roughness', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=112,
  serialized_end=310,
)

_COLLECTIONPRESTIGELEVEL.fields_by_name['color'].message_type = WUProtos_dot_Data_dot_Color__pb2._COLOR
DESCRIPTOR.message_types_by_name['CollectionPrestigeLevel'] = _COLLECTIONPRESTIGELEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CollectionPrestigeLevel = _reflection.GeneratedProtocolMessageType('CollectionPrestigeLevel', (_message.Message,), dict(
  DESCRIPTOR = _COLLECTIONPRESTIGELEVEL,
  __module__ = 'WUProtos.Data.Collection.CollectionPrestigeLevel_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Collection.CollectionPrestigeLevel)
  ))
_sym_db.RegisterMessage(CollectionPrestigeLevel)


# @@protoc_insertion_point(module_scope)