# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/data/client/client_telemetry_partner_poi_leaving.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/data/client/client_telemetry_partner_poi_leaving.proto',
  package='wuprotos.data.client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n?wuprotos/data/client/client_telemetry_partner_poi_leaving.proto\x12\x14wuprotos.data.client\"r\n ClientTelemetryPartnerPoiLeaving\x12\x0e\n\x06poi_id\x18\x01 \x01(\t\x12\x12\n\npartner_id\x18\x02 \x01(\t\x12\x13\n\x0btime_in_poi\x18\x03 \x01(\x03\x12\x15\n\rtime_in_range\x18\x04 \x01(\x03\x62\x06proto3')
)




_CLIENTTELEMETRYPARTNERPOILEAVING = _descriptor.Descriptor(
  name='ClientTelemetryPartnerPoiLeaving',
  full_name='wuprotos.data.client.ClientTelemetryPartnerPoiLeaving',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='poi_id', full_name='wuprotos.data.client.ClientTelemetryPartnerPoiLeaving.poi_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner_id', full_name='wuprotos.data.client.ClientTelemetryPartnerPoiLeaving.partner_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_in_poi', full_name='wuprotos.data.client.ClientTelemetryPartnerPoiLeaving.time_in_poi', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_in_range', full_name='wuprotos.data.client.ClientTelemetryPartnerPoiLeaving.time_in_range', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=89,
  serialized_end=203,
)

DESCRIPTOR.message_types_by_name['ClientTelemetryPartnerPoiLeaving'] = _CLIENTTELEMETRYPARTNERPOILEAVING
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientTelemetryPartnerPoiLeaving = _reflection.GeneratedProtocolMessageType('ClientTelemetryPartnerPoiLeaving', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTTELEMETRYPARTNERPOILEAVING,
  __module__ = 'wuprotos.data.client.client_telemetry_partner_poi_leaving_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.data.client.ClientTelemetryPartnerPoiLeaving)
  ))
_sym_db.RegisterMessage(ClientTelemetryPartnerPoiLeaving)


# @@protoc_insertion_point(module_scope)
