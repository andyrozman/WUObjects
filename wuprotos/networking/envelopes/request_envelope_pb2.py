# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/envelopes/request_envelope.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wuprotos.networking.requests import request_pb2 as wuprotos_dot_networking_dot_requests_dot_request__pb2
from wuprotos.networking.envelopes import auth_ticket_pb2 as wuprotos_dot_networking_dot_envelopes_dot_auth__ticket__pb2
from wuprotos.networking.platform import platform_request_type_pb2 as wuprotos_dot_networking_dot_platform_dot_platform__request__type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/envelopes/request_envelope.proto',
  package='wuprotos.networking.envelopes',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n4wuprotos/networking/envelopes/request_envelope.proto\x12\x1dwuprotos.networking.envelopes\x1a*wuprotos/networking/requests/request.proto\x1a/wuprotos/networking/envelopes/auth_ticket.proto\x1a\x38wuprotos/networking/platform/platform_request_type.proto\"\xbe\x06\n\x0fRequestEnvelope\x12\x13\n\x0bstatus_code\x18\x01 \x01(\x05\x12\x12\n\nrequest_id\x18\x03 \x01(\x04\x12\x37\n\x08requests\x18\x04 \x03(\x0b\x32%.wuprotos.networking.requests.Request\x12Y\n\x11platform_requests\x18\x06 \x03(\x0b\x32>.wuprotos.networking.envelopes.RequestEnvelope.PlatformRequest\x12\x10\n\x08latitude\x18\x07 \x01(\x01\x12\x11\n\tlongitude\x18\x08 \x01(\x01\x12\x10\n\x08\x61\x63\x63uracy\x18\t \x01(\x01\x12J\n\tauth_info\x18\n \x01(\x0b\x32\x37.wuprotos.networking.envelopes.RequestEnvelope.AuthInfo\x12>\n\x0b\x61uth_ticket\x18\x0b \x01(\x0b\x32).wuprotos.networking.envelopes.AuthTicket\x12!\n\x19ms_since_last_locationfix\x18\x0c \x01(\x03\x1a\x9a\x02\n\x08\x41uthInfo\x12\x10\n\x08provider\x18\x01 \x01(\t\x12J\n\x05token\x18\x02 \x01(\x0b\x32;.wuprotos.networking.envelopes.RequestEnvelope.AuthInfo.JWT\x12T\n\x07options\x18\x03 \x01(\x0b\x32\x43.wuprotos.networking.envelopes.RequestEnvelope.AuthInfo.AuthOptions\x1a)\n\x03JWT\x12\x10\n\x08\x63ontents\x18\x01 \x01(\t\x12\x10\n\x08unknown2\x18\x02 \x01(\x05\x1a/\n\x0b\x41uthOptions\x12 \n\x18prevent_account_creation\x18\x01 \x01(\x08\x1ak\n\x0fPlatformRequest\x12?\n\x04type\x18\x01 \x01(\x0e\x32\x31.wuprotos.networking.platform.PlatformRequestType\x12\x17\n\x0frequest_message\x18\x02 \x01(\x0c\x62\x06proto3')
  ,
  dependencies=[wuprotos_dot_networking_dot_requests_dot_request__pb2.DESCRIPTOR,wuprotos_dot_networking_dot_envelopes_dot_auth__ticket__pb2.DESCRIPTOR,wuprotos_dot_networking_dot_platform_dot_platform__request__type__pb2.DESCRIPTOR,])




_REQUESTENVELOPE_AUTHINFO_JWT = _descriptor.Descriptor(
  name='JWT',
  full_name='wuprotos.networking.envelopes.RequestEnvelope.AuthInfo.JWT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contents', full_name='wuprotos.networking.envelopes.RequestEnvelope.AuthInfo.JWT.contents', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='wuprotos.networking.envelopes.RequestEnvelope.AuthInfo.JWT.unknown2', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=870,
  serialized_end=911,
)

_REQUESTENVELOPE_AUTHINFO_AUTHOPTIONS = _descriptor.Descriptor(
  name='AuthOptions',
  full_name='wuprotos.networking.envelopes.RequestEnvelope.AuthInfo.AuthOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prevent_account_creation', full_name='wuprotos.networking.envelopes.RequestEnvelope.AuthInfo.AuthOptions.prevent_account_creation', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=913,
  serialized_end=960,
)

_REQUESTENVELOPE_AUTHINFO = _descriptor.Descriptor(
  name='AuthInfo',
  full_name='wuprotos.networking.envelopes.RequestEnvelope.AuthInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider', full_name='wuprotos.networking.envelopes.RequestEnvelope.AuthInfo.provider', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='wuprotos.networking.envelopes.RequestEnvelope.AuthInfo.token', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='options', full_name='wuprotos.networking.envelopes.RequestEnvelope.AuthInfo.options', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOPE_AUTHINFO_JWT, _REQUESTENVELOPE_AUTHINFO_AUTHOPTIONS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=678,
  serialized_end=960,
)

_REQUESTENVELOPE_PLATFORMREQUEST = _descriptor.Descriptor(
  name='PlatformRequest',
  full_name='wuprotos.networking.envelopes.RequestEnvelope.PlatformRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='wuprotos.networking.envelopes.RequestEnvelope.PlatformRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_message', full_name='wuprotos.networking.envelopes.RequestEnvelope.PlatformRequest.request_message', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=962,
  serialized_end=1069,
)

_REQUESTENVELOPE = _descriptor.Descriptor(
  name='RequestEnvelope',
  full_name='wuprotos.networking.envelopes.RequestEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_code', full_name='wuprotos.networking.envelopes.RequestEnvelope.status_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='wuprotos.networking.envelopes.RequestEnvelope.request_id', index=1,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='requests', full_name='wuprotos.networking.envelopes.RequestEnvelope.requests', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='platform_requests', full_name='wuprotos.networking.envelopes.RequestEnvelope.platform_requests', index=3,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='wuprotos.networking.envelopes.RequestEnvelope.latitude', index=4,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='wuprotos.networking.envelopes.RequestEnvelope.longitude', index=5,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accuracy', full_name='wuprotos.networking.envelopes.RequestEnvelope.accuracy', index=6,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_info', full_name='wuprotos.networking.envelopes.RequestEnvelope.auth_info', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='auth_ticket', full_name='wuprotos.networking.envelopes.RequestEnvelope.auth_ticket', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ms_since_last_locationfix', full_name='wuprotos.networking.envelopes.RequestEnvelope.ms_since_last_locationfix', index=9,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOPE_AUTHINFO, _REQUESTENVELOPE_PLATFORMREQUEST, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=239,
  serialized_end=1069,
)

_REQUESTENVELOPE_AUTHINFO_JWT.containing_type = _REQUESTENVELOPE_AUTHINFO
_REQUESTENVELOPE_AUTHINFO_AUTHOPTIONS.containing_type = _REQUESTENVELOPE_AUTHINFO
_REQUESTENVELOPE_AUTHINFO.fields_by_name['token'].message_type = _REQUESTENVELOPE_AUTHINFO_JWT
_REQUESTENVELOPE_AUTHINFO.fields_by_name['options'].message_type = _REQUESTENVELOPE_AUTHINFO_AUTHOPTIONS
_REQUESTENVELOPE_AUTHINFO.containing_type = _REQUESTENVELOPE
_REQUESTENVELOPE_PLATFORMREQUEST.fields_by_name['type'].enum_type = wuprotos_dot_networking_dot_platform_dot_platform__request__type__pb2._PLATFORMREQUESTTYPE
_REQUESTENVELOPE_PLATFORMREQUEST.containing_type = _REQUESTENVELOPE
_REQUESTENVELOPE.fields_by_name['requests'].message_type = wuprotos_dot_networking_dot_requests_dot_request__pb2._REQUEST
_REQUESTENVELOPE.fields_by_name['platform_requests'].message_type = _REQUESTENVELOPE_PLATFORMREQUEST
_REQUESTENVELOPE.fields_by_name['auth_info'].message_type = _REQUESTENVELOPE_AUTHINFO
_REQUESTENVELOPE.fields_by_name['auth_ticket'].message_type = wuprotos_dot_networking_dot_envelopes_dot_auth__ticket__pb2._AUTHTICKET
DESCRIPTOR.message_types_by_name['RequestEnvelope'] = _REQUESTENVELOPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestEnvelope = _reflection.GeneratedProtocolMessageType('RequestEnvelope', (_message.Message,), dict(

  AuthInfo = _reflection.GeneratedProtocolMessageType('AuthInfo', (_message.Message,), dict(

    JWT = _reflection.GeneratedProtocolMessageType('JWT', (_message.Message,), dict(
      DESCRIPTOR = _REQUESTENVELOPE_AUTHINFO_JWT,
      __module__ = 'wuprotos.networking.envelopes.request_envelope_pb2'
      # @@protoc_insertion_point(class_scope:wuprotos.networking.envelopes.RequestEnvelope.AuthInfo.JWT)
      ))
    ,

    AuthOptions = _reflection.GeneratedProtocolMessageType('AuthOptions', (_message.Message,), dict(
      DESCRIPTOR = _REQUESTENVELOPE_AUTHINFO_AUTHOPTIONS,
      __module__ = 'wuprotos.networking.envelopes.request_envelope_pb2'
      # @@protoc_insertion_point(class_scope:wuprotos.networking.envelopes.RequestEnvelope.AuthInfo.AuthOptions)
      ))
    ,
    DESCRIPTOR = _REQUESTENVELOPE_AUTHINFO,
    __module__ = 'wuprotos.networking.envelopes.request_envelope_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.networking.envelopes.RequestEnvelope.AuthInfo)
    ))
  ,

  PlatformRequest = _reflection.GeneratedProtocolMessageType('PlatformRequest', (_message.Message,), dict(
    DESCRIPTOR = _REQUESTENVELOPE_PLATFORMREQUEST,
    __module__ = 'wuprotos.networking.envelopes.request_envelope_pb2'
    # @@protoc_insertion_point(class_scope:wuprotos.networking.envelopes.RequestEnvelope.PlatformRequest)
    ))
  ,
  DESCRIPTOR = _REQUESTENVELOPE,
  __module__ = 'wuprotos.networking.envelopes.request_envelope_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.envelopes.RequestEnvelope)
  ))
_sym_db.RegisterMessage(RequestEnvelope)
_sym_db.RegisterMessage(RequestEnvelope.AuthInfo)
_sym_db.RegisterMessage(RequestEnvelope.AuthInfo.JWT)
_sym_db.RegisterMessage(RequestEnvelope.AuthInfo.AuthOptions)
_sym_db.RegisterMessage(RequestEnvelope.PlatformRequest)


# @@protoc_insertion_point(module_scope)
