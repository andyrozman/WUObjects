# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientTelemetryFamilyDetails.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientTelemetryFamilyDetails.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n7WUProtos/Data/Client/ClientTelemetryFamilyDetails.proto\x12\x14WUProtos.Data.Client\"1\n\x1c\x43lientTelemetryFamilyDetails\x12\x11\n\tfamily_id\x18\x01 \x01(\tb\x06proto3')
)




_CLIENTTELEMETRYFAMILYDETAILS = _descriptor.Descriptor(
  name='ClientTelemetryFamilyDetails',
  full_name='WUProtos.Data.Client.ClientTelemetryFamilyDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='family_id', full_name='WUProtos.Data.Client.ClientTelemetryFamilyDetails.family_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=81,
  serialized_end=130,
)

DESCRIPTOR.message_types_by_name['ClientTelemetryFamilyDetails'] = _CLIENTTELEMETRYFAMILYDETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientTelemetryFamilyDetails = _reflection.GeneratedProtocolMessageType('ClientTelemetryFamilyDetails', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTTELEMETRYFAMILYDETAILS,
  __module__ = 'WUProtos.Data.Client.ClientTelemetryFamilyDetails_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientTelemetryFamilyDetails)
  ))
_sym_db.RegisterMessage(ClientTelemetryFamilyDetails)


# @@protoc_insertion_point(module_scope)