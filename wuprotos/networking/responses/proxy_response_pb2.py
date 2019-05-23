# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/proxy_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/proxy_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n2wuprotos/networking/responses/proxy_response.proto\x12\x1dwuprotos.networking.responses\"\xd4\x02\n\rProxyResponse\x12\x43\n\x06status\x18\x01 \x01(\x0e\x32\x33.wuprotos.networking.responses.ProxyResponse.Status\x12\x15\n\rassigned_host\x18\x02 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\"\xd5\x01\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\r\n\tCOMPLETED\x10\x01\x12\x1c\n\x18\x43OMPLETED_AND_REASSIGNED\x10\x02\x12\x14\n\x10\x41\x43TION_NOT_FOUND\x10\x03\x12\x14\n\x10\x41SSIGNMENT_ERROR\x10\x04\x12\x1c\n\x18PROXY_UNAUTHORIZED_ERROR\x10\x05\x12\x12\n\x0eINTERNAL_ERROR\x10\x06\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\x07\x12\x11\n\rACCESS_DENIED\x10\x08\x12\x11\n\rTIMEOUT_ERROR\x10\tb\x06proto3')
)



_PROXYRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='wuprotos.networking.responses.ProxyResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COMPLETED_AND_REASSIGNED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_NOT_FOUND', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ASSIGNMENT_ERROR', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROXY_UNAUTHORIZED_ERROR', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BAD_REQUEST', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACCESS_DENIED', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIMEOUT_ERROR', index=9, number=9,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=213,
  serialized_end=426,
)
_sym_db.RegisterEnumDescriptor(_PROXYRESPONSE_STATUS)


_PROXYRESPONSE = _descriptor.Descriptor(
  name='ProxyResponse',
  full_name='wuprotos.networking.responses.ProxyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wuprotos.networking.responses.ProxyResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assigned_host', full_name='wuprotos.networking.responses.ProxyResponse.assigned_host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='wuprotos.networking.responses.ProxyResponse.payload', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PROXYRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=426,
)

_PROXYRESPONSE.fields_by_name['status'].enum_type = _PROXYRESPONSE_STATUS
_PROXYRESPONSE_STATUS.containing_type = _PROXYRESPONSE
DESCRIPTOR.message_types_by_name['ProxyResponse'] = _PROXYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProxyResponse = _reflection.GeneratedProtocolMessageType('ProxyResponse', (_message.Message,), dict(
  DESCRIPTOR = _PROXYRESPONSE,
  __module__ = 'wuprotos.networking.responses.proxy_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.ProxyResponse)
  ))
_sym_db.RegisterMessage(ProxyResponse)


# @@protoc_insertion_point(module_scope)
