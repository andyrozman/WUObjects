# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Platform/Requests/ClientTelemetryMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Platform/Requests/ClientTelemetryMessage.proto',
  package='WUProtos.Networking.Platform.Requests',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nBWUProtos/Networking/Platform/Requests/ClientTelemetryMessage.proto\x12%WUProtos.Networking.Platform.Requests\"\x18\n\x16\x43lientTelemetryMessageb\x06proto3')
)




_CLIENTTELEMETRYMESSAGE = _descriptor.Descriptor(
  name='ClientTelemetryMessage',
  full_name='WUProtos.Networking.Platform.Requests.ClientTelemetryMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=109,
  serialized_end=133,
)

DESCRIPTOR.message_types_by_name['ClientTelemetryMessage'] = _CLIENTTELEMETRYMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientTelemetryMessage = _reflection.GeneratedProtocolMessageType('ClientTelemetryMessage', (_message.Message,), dict(
  DESCRIPTOR = _CLIENTTELEMETRYMESSAGE,
  __module__ = 'WUProtos.Networking.Platform.Requests.ClientTelemetryMessage_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Platform.Requests.ClientTelemetryMessage)
  ))
_sym_db.RegisterMessage(ClientTelemetryMessage)


# @@protoc_insertion_point(module_scope)