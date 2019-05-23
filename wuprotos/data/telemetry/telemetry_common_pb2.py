# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/data/telemetry/telemetry_common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/data/telemetry/telemetry_common.proto',
  package='wuprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n.wuprotos/data/telemetry/telemetry_common.proto\x12\x17wuprotos.data.telemetry\"@\n\x0fTelemetryCommon\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x1a\n\x12\x63orrelation_vector\x18\x02 \x01(\tb\x06proto3')
)




_TELEMETRYCOMMON = _descriptor.Descriptor(
  name='TelemetryCommon',
  full_name='wuprotos.data.telemetry.TelemetryCommon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='wuprotos.data.telemetry.TelemetryCommon.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='correlation_vector', full_name='wuprotos.data.telemetry.TelemetryCommon.correlation_vector', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=75,
  serialized_end=139,
)

DESCRIPTOR.message_types_by_name['TelemetryCommon'] = _TELEMETRYCOMMON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TelemetryCommon = _reflection.GeneratedProtocolMessageType('TelemetryCommon', (_message.Message,), dict(
  DESCRIPTOR = _TELEMETRYCOMMON,
  __module__ = 'wuprotos.data.telemetry.telemetry_common_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.data.telemetry.TelemetryCommon)
  ))
_sym_db.RegisterMessage(TelemetryCommon)


# @@protoc_insertion_point(module_scope)
