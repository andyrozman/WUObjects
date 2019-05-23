# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/data/client/client_collection_family.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wuprotos.data import color_pb2 as wuprotos_dot_data_dot_color__pb2
from wuprotos.data import sound_config_pb2 as wuprotos_dot_data_dot_sound__config__pb2
from wuprotos.data import requirements_pb2 as wuprotos_dot_data_dot_requirements__pb2
from wuprotos.data.collection import collection_prestige_level_pb2 as wuprotos_dot_data_dot_collection_dot_collection__prestige__level__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/data/client/client_collection_family.proto',
  package='wuprotos.data.client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n3wuprotos/data/client/client_collection_family.proto\x12\x14wuprotos.data.client\x1a\x19wuprotos/data/color.proto\x1a wuprotos/data/sound_config.proto\x1a wuprotos/data/requirements.proto\x1a\x38wuprotos/data/collection/collection_prestige_level.proto\"\xee\x04\n\x16\x43lientCollectionFamily\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0c\n\x04icon\x18\x05 \x01(\t\x12\x18\n\x10landmark_texture\x18\x06 \x01(\t\x12\x17\n\x0flandmark_prefab\x18\x07 \x01(\t\x12\x1c\n\x14landmark_description\x18\x08 \x01(\t\x12\x12\n\nshow_in_ui\x18\t \x01(\x08\x12\x15\n\rlandmark_icon\x18\x0b \x01(\t\x12#\n\x05\x63olor\x18\x0c \x01(\x0b\x32\x14.wuprotos.data.Color\x12-\n\x0f\x63olor_highlight\x18\r \x01(\x0b\x32\x14.wuprotos.data.Color\x12\x14\n\x0ctrace_prefab\x18\x0e \x01(\t\x12\x15\n\rborder_images\x18\x0f \x03(\t\x12\x1d\n\x15\x66\x61mily_runestone_icon\x18\x10 \x01(\t\x12)\n\x05sound\x18\x11 \x01(\x0b\x32\x1a.wuprotos.data.SoundConfig\x12;\n\x16unarchive_requirements\x18\x12 \x01(\x0b\x32\x1b.wuprotos.data.Requirements\x12!\n\x19trace_rarity_vfx_override\x18\x13 \x01(\t\x12L\n\x11prestige_override\x18\x14 \x03(\x0b\x32\x31.wuprotos.data.collection.CollectionPrestigeLevel\x12\"\n\x1ahide_landmark_info_details\x18\x15 \x01(\x08\x62\x06proto3')
  ,
  dependencies=[wuprotos_dot_data_dot_color__pb2.DESCRIPTOR,wuprotos_dot_data_dot_sound__config__pb2.DESCRIPTOR,wuprotos_dot_data_dot_requirements__pb2.DESCRIPTOR,wuprotos_dot_data_dot_collection_dot_collection__prestige__level__pb2.DESCRIPTOR,])




_CLIENTCOLLECTIONFAMILY = _descriptor.Descriptor(
  name='ClientCollectionFamily',
  full_name='wuprotos.data.client.ClientCollectionFamily',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='wuprotos.data.client.ClientCollectionFamily.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='wuprotos.data.client.ClientCollectionFamily.name', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='wuprotos.data.client.ClientCollectionFamily.description', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='wuprotos.data.client.ClientCollectionFamily.icon', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='landmark_texture', full_name='wuprotos.data.client.ClientCollectionFamily.landmark_texture', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='landmark_prefab', full_name='wuprotos.data.client.ClientCollectionFamily.landmark_prefab', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='landmark_description', full_name='wuprotos.data.client.ClientCollectionFamily.landmark_description', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_in_ui', full_name='wuprotos.data.client.ClientCollectionFamily.show_in_ui', index=7,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='landmark_icon', full_name='wuprotos.data.client.ClientCollectionFamily.landmark_icon', index=8,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='wuprotos.data.client.ClientCollectionFamily.color', index=9,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color_highlight', full_name='wuprotos.data.client.ClientCollectionFamily.color_highlight', index=10,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_prefab', full_name='wuprotos.data.client.ClientCollectionFamily.trace_prefab', index=11,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='border_images', full_name='wuprotos.data.client.ClientCollectionFamily.border_images', index=12,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='family_runestone_icon', full_name='wuprotos.data.client.ClientCollectionFamily.family_runestone_icon', index=13,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sound', full_name='wuprotos.data.client.ClientCollectionFamily.sound', index=14,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unarchive_requirements', full_name='wuprotos.data.client.ClientCollectionFamily.unarchive_requirements', index=15,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trace_rarity_vfx_override', full_name='wuprotos.data.client.ClientCollectionFamily.trace_rarity_vfx_override', index=16,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='prestige_override', full_name='wuprotos.data.client.ClientCollectionFamily.prestige_override', index=17,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hide_landmark_info_details', full_name='wuprotos.data.client.ClientCollectionFamily.hide_landmark_info_details', index=18,
      number=21, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=231,
  serialized_end=853,
)

_CLIENTCOLLECTIONFAMILY.fields_by_name['color'].message_type = wuprotos_dot_data_dot_color__pb2._COLOR
_CLIENTCOLLECTIONFAMILY.fields_by_name['color_highlight'].message_type = wuprotos_dot_data_dot_color__pb2._COLOR
_CLIENTCOLLECTIONFAMILY.fields_by_name['sound'].message_type = wuprotos_dot_data_dot_sound__config__pb2._SOUNDCONFIG
_CLIENTCOLLECTIONFAMILY.fields_by_name['unarchive_requirements'].message_type = wuprotos_dot_data_dot_requirements__pb2._REQUIREMENTS
_CLIENTCOLLECTIONFAMILY.fields_by_name['prestige_override'].message_type = wuprotos_dot_data_dot_collection_dot_collection__prestige__level__pb2._COLLECTIONPRESTIGELEVEL
DESCRIPTOR.message_types_by_name['ClientCollectionFamily'] = _CLIENTCOLLECTIONFAMILY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientCollectionFamily = _reflection.GeneratedProtocolMessageType('ClientCollectionFamily', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTCOLLECTIONFAMILY,
  __module__ = 'wuprotos.data.client.client_collection_family_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.data.client.ClientCollectionFamily)
  ))
_sym_db.RegisterMessage(ClientCollectionFamily)


# @@protoc_insertion_point(module_scope)
