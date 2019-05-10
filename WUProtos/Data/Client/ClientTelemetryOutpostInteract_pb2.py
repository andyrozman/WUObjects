# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Data/Client/ClientTelemetryOutpostInteract.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import POIInteract_pb2 as WUProtos_dot_Data_dot_POIInteract__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Data/Client/ClientTelemetryOutpostInteract.proto',
  package='WUProtos.Data.Client',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n9WUProtos/Data/Client/ClientTelemetryOutpostInteract.proto\x12\x14WUProtos.Data.Client\x1a\x1fWUProtos/Data/POIInteract.proto\"g\n\x1e\x43lientTelemetryOutpostInteract\x12\x14\n\x0coutpost_type\x18\x01 \x01(\t\x12/\n\x0b\x63ommon_data\x18\x02 \x01(\x0b\x32\x1a.WUProtos.Data.POIInteractb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_POIInteract__pb2.DESCRIPTOR,])




_CLIENTTELEMETRYOUTPOSTINTERACT = _descriptor.Descriptor(
  name='ClientTelemetryOutpostInteract',
  full_name='WUProtos.Data.Client.ClientTelemetryOutpostInteract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outpost_type', full_name='WUProtos.Data.Client.ClientTelemetryOutpostInteract.outpost_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='common_data', full_name='WUProtos.Data.Client.ClientTelemetryOutpostInteract.common_data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=116,
  serialized_end=219,
)

_CLIENTTELEMETRYOUTPOSTINTERACT.fields_by_name['common_data'].message_type = WUProtos_dot_Data_dot_POIInteract__pb2._POIINTERACT
DESCRIPTOR.message_types_by_name['ClientTelemetryOutpostInteract'] = _CLIENTTELEMETRYOUTPOSTINTERACT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientTelemetryOutpostInteract = _reflection.GeneratedProtocolMessageType('ClientTelemetryOutpostInteract', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTTELEMETRYOUTPOSTINTERACT,
  __module__ = 'WUProtos.Data.Client.ClientTelemetryOutpostInteract_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Data.Client.ClientTelemetryOutpostInteract)
  ))
_sym_db.RegisterMessage(ClientTelemetryOutpostInteract)


# @@protoc_insertion_point(module_scope)