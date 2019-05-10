# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientStoreConfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import StoreCategory_pb2 as WUProtos_dot_Data_dot_StoreCategory__pb2
from WUProtos.Data import StoreRarity_pb2 as WUProtos_dot_Data_dot_StoreRarity__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientStoreConfig.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n,WUProtos/Data/Client/ClientStoreConfig.proto\x12\x14WUProtos.Data.Client\x1a!WUProtos/Data/StoreCategory.proto\x1a\x1fWUProtos/Data/StoreRarity.proto\"\xb1\x01\n\x11\x43lientStoreConfig\x12\n\n\x02id\x18\x01 \x01(\t\x12\x36\n\x10store_categories\x18\x02 \x03(\x0b\x32\x1c.WUProtos.Data.StoreCategory\x12\x32\n\x0estore_rarities\x18\x03 \x03(\x0b\x32\x1a.WUProtos.Data.StoreRarity\x12$\n\x1c\x64\x65\x66\x61ult_store_pack_icon_path\x18\x04 \x01(\tb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_StoreCategory__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_StoreRarity__pb2.DESCRIPTOR,])




_CLIENTSTORECONFIG = _descriptor.Descriptor(
  name='ClientStoreConfig',
  full_name='WUProtos.Data.Client.ClientStoreConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='WUProtos.Data.Client.ClientStoreConfig.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='store_categories', full_name='WUProtos.Data.Client.ClientStoreConfig.store_categories', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='store_rarities', full_name='WUProtos.Data.Client.ClientStoreConfig.store_rarities', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='default_store_pack_icon_path', full_name='WUProtos.Data.Client.ClientStoreConfig.default_store_pack_icon_path', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=139,
  serialized_end=316,
)

_CLIENTSTORECONFIG.fields_by_name['store_categories'].message_type = WUProtos_dot_Data_dot_StoreCategory__pb2._STORECATEGORY
_CLIENTSTORECONFIG.fields_by_name['store_rarities'].message_type = WUProtos_dot_Data_dot_StoreRarity__pb2._STORERARITY
DESCRIPTOR.message_types_by_name['ClientStoreConfig'] = _CLIENTSTORECONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientStoreConfig = _reflection.GeneratedProtocolMessageType('ClientStoreConfig', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTSTORECONFIG,
  __module__ = 'WUProtos.Data.Client.ClientStoreConfig_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientStoreConfig)
  ))
_sym_db.RegisterMessage(ClientStoreConfig)


# @@protoc_insertion_point(module_scope)