# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/push_performance_metrics_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/push_performance_metrics_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nEwuprotos/networking/responses/push_performance_metrics_response.proto\x12\x1dwuprotos.networking.responses\" \n\x1ePushPerformanceMetricsResponseb\x06proto3')
)




_PUSHPERFORMANCEMETRICSRESPONSE = _descriptor.Descriptor(
  name='PushPerformanceMetricsResponse',
  full_name='wuprotos.networking.responses.PushPerformanceMetricsResponse',
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
  serialized_start=104,
  serialized_end=136,
)

DESCRIPTOR.message_types_by_name['PushPerformanceMetricsResponse'] = _PUSHPERFORMANCEMETRICSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PushPerformanceMetricsResponse = _reflection.GeneratedProtocolMessageType('PushPerformanceMetricsResponse', (_message.Message,), dict(
  DESCRIPTOR = _PUSHPERFORMANCEMETRICSRESPONSE,
  __module__ = 'wuprotos.networking.responses.push_performance_metrics_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.PushPerformanceMetricsResponse)
  ))
_sym_db.RegisterMessage(PushPerformanceMetricsResponse)


# @@protoc_insertion_point(module_scope)
