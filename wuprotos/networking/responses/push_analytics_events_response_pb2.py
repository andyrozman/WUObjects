# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/push_analytics_events_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/push_analytics_events_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nBwuprotos/networking/responses/push_analytics_events_response.proto\x12\x1dwuprotos.networking.responses\"\x1d\n\x1bPushAnalyticsEventsResponseb\x06proto3')
)




_PUSHANALYTICSEVENTSRESPONSE = _descriptor.Descriptor(
  name='PushAnalyticsEventsResponse',
  full_name='wuprotos.networking.responses.PushAnalyticsEventsResponse',
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
  serialized_start=101,
  serialized_end=130,
)

DESCRIPTOR.message_types_by_name['PushAnalyticsEventsResponse'] = _PUSHANALYTICSEVENTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PushAnalyticsEventsResponse = _reflection.GeneratedProtocolMessageType('PushAnalyticsEventsResponse', (_message.Message,), dict(
  DESCRIPTOR = _PUSHANALYTICSEVENTSRESPONSE,
  __module__ = 'wuprotos.networking.responses.push_analytics_events_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.PushAnalyticsEventsResponse)
  ))
_sym_db.RegisterMessage(PushAnalyticsEventsResponse)


# @@protoc_insertion_point(module_scope)
