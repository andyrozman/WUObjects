# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/data/client/client_telemetry_partner_poi_interact.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/data/client/client_telemetry_partner_poi_interact.proto',
  package='wuprotos.data.client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n@wuprotos/data/client/client_telemetry_partner_poi_interact.proto\x12\x14wuprotos.data.client\"[\n!ClientTelemetryPartnerPoiInteract\x12\x0e\n\x06poi_id\x18\x01 \x01(\t\x12\x12\n\npartner_id\x18\x02 \x01(\t\x12\x12\n\nis_preview\x18\x03 \x01(\x08\x62\x06proto3')
)




_CLIENTTELEMETRYPARTNERPOIINTERACT = _descriptor.Descriptor(
  name='ClientTelemetryPartnerPoiInteract',
  full_name='wuprotos.data.client.ClientTelemetryPartnerPoiInteract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='poi_id', full_name='wuprotos.data.client.ClientTelemetryPartnerPoiInteract.poi_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner_id', full_name='wuprotos.data.client.ClientTelemetryPartnerPoiInteract.partner_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_preview', full_name='wuprotos.data.client.ClientTelemetryPartnerPoiInteract.is_preview', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=90,
  serialized_end=181,
)

DESCRIPTOR.message_types_by_name['ClientTelemetryPartnerPoiInteract'] = _CLIENTTELEMETRYPARTNERPOIINTERACT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientTelemetryPartnerPoiInteract = _reflection.GeneratedProtocolMessageType('ClientTelemetryPartnerPoiInteract', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTTELEMETRYPARTNERPOIINTERACT,
  __module__ = 'wuprotos.data.client.client_telemetry_partner_poi_interact_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.data.client.ClientTelemetryPartnerPoiInteract)
  ))
_sym_db.RegisterMessage(ClientTelemetryPartnerPoiInteract)


# @@protoc_insertion_point(module_scope)
