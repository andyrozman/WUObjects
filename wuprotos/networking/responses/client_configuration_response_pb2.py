# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/client_configuration_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wuprotos.data import quality_level_pb2 as wuprotos_dot_data_dot_quality__level__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/client_configuration_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nAwuprotos/networking/responses/client_configuration_response.proto\x12\x1dwuprotos.networking.responses\x1a!wuprotos/data/quality_level.proto\"\xd9\x01\n\x1b\x43lientConfigurationResponse\x12\x14\n\x0c\x66orce_update\x18\x01 \x01(\x08\x12\x12\n\nserver_uri\x18\x02 \x01(\t\x12\x15\n\ractual_env_id\x18\x03 \x01(\t\x12\x18\n\x10manifest_version\x18\x04 \x01(\t\x12\x45\n\rquality_level\x18\x05 \x01(\x0b\x32..wuprotos.data.QualityLevel.SharedQualityLevel\x12\x18\n\x10\x66orce_update_url\x18\x06 \x01(\tb\x06proto3')
  ,
  dependencies=[wuprotos_dot_data_dot_quality__level__pb2.DESCRIPTOR,])




_CLIENTCONFIGURATIONRESPONSE = _descriptor.Descriptor(
  name='ClientConfigurationResponse',
  full_name='wuprotos.networking.responses.ClientConfigurationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='force_update', full_name='wuprotos.networking.responses.ClientConfigurationResponse.force_update', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_uri', full_name='wuprotos.networking.responses.ClientConfigurationResponse.server_uri', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actual_env_id', full_name='wuprotos.networking.responses.ClientConfigurationResponse.actual_env_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='manifest_version', full_name='wuprotos.networking.responses.ClientConfigurationResponse.manifest_version', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quality_level', full_name='wuprotos.networking.responses.ClientConfigurationResponse.quality_level', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='force_update_url', full_name='wuprotos.networking.responses.ClientConfigurationResponse.force_update_url', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=136,
  serialized_end=353,
)

_CLIENTCONFIGURATIONRESPONSE.fields_by_name['quality_level'].message_type = wuprotos_dot_data_dot_quality__level__pb2._QUALITYLEVEL_SHAREDQUALITYLEVEL
DESCRIPTOR.message_types_by_name['ClientConfigurationResponse'] = _CLIENTCONFIGURATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientConfigurationResponse = _reflection.GeneratedProtocolMessageType('ClientConfigurationResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTCONFIGURATIONRESPONSE,
  __module__ = 'wuprotos.networking.responses.client_configuration_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.ClientConfigurationResponse)
  ))
_sym_db.RegisterMessage(ClientConfigurationResponse)


# @@protoc_insertion_point(module_scope)
