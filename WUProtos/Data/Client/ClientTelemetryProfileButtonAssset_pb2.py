# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientTelemetryProfileButtonAssset.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Enums import CategoryAssetType_pb2 as WUProtos_dot_Enums_dot_CategoryAssetType__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientTelemetryProfileButtonAssset.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n=WUProtos/Data/Client/ClientTelemetryProfileButtonAssset.proto\x12\x14WUProtos.Data.Client\x1a&WUProtos/Enums/CategoryAssetType.proto\"\x8b\x01\n\"ClientTelemetryProfileButtonAssset\x12\x19\n\x11pressed_button_id\x18\x01 \x01(\t\x12\x13\n\x0bsticker_add\x18\x02 \x01(\x08\x12\x35\n\nasset_type\x18\x03 \x01(\x0e\x32!.WUProtos.Enums.CategoryAssetTypeb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Enums_dot_CategoryAssetType__pb2.DESCRIPTOR,])




_CLIENTTELEMETRYPROFILEBUTTONASSSET = _descriptor.Descriptor(
  name='ClientTelemetryProfileButtonAssset',
  full_name='WUProtos.Data.Client.ClientTelemetryProfileButtonAssset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pressed_button_id', full_name='WUProtos.Data.Client.ClientTelemetryProfileButtonAssset.pressed_button_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sticker_add', full_name='WUProtos.Data.Client.ClientTelemetryProfileButtonAssset.sticker_add', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_type', full_name='WUProtos.Data.Client.ClientTelemetryProfileButtonAssset.asset_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=128,
  serialized_end=267,
)

_CLIENTTELEMETRYPROFILEBUTTONASSSET.fields_by_name['asset_type'].enum_type = WUProtos_dot_Enums_dot_CategoryAssetType__pb2._CATEGORYASSETTYPE
DESCRIPTOR.message_types_by_name['ClientTelemetryProfileButtonAssset'] = _CLIENTTELEMETRYPROFILEBUTTONASSSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientTelemetryProfileButtonAssset = _reflection.GeneratedProtocolMessageType('ClientTelemetryProfileButtonAssset', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTTELEMETRYPROFILEBUTTONASSSET,
  __module__ = 'WUProtos.Data.Client.ClientTelemetryProfileButtonAssset_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientTelemetryProfileButtonAssset)
  ))
_sym_db.RegisterMessage(ClientTelemetryProfileButtonAssset)


# @@protoc_insertion_point(module_scope)