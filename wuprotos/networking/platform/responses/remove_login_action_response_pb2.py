# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/platform/responses/remove_login_action_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wuprotos.data import login_detail_pb2 as wuprotos_dot_data_dot_login__detail__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/platform/responses/remove_login_action_response.proto',
  package='wuprotos.networking.platform.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nIwuprotos/networking/platform/responses/remove_login_action_response.proto\x12&wuprotos.networking.platform.responses\x1a wuprotos/data/login_detail.proto\"^\n\x19RemoveLoginActionResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x30\n\x0clogin_detail\x18\x02 \x03(\x0b\x32\x1a.wuprotos.data.LoginDetailb\x06proto3')
  ,
  dependencies=[wuprotos_dot_data_dot_login__detail__pb2.DESCRIPTOR,])




_REMOVELOGINACTIONRESPONSE = _descriptor.Descriptor(
  name='RemoveLoginActionResponse',
  full_name='wuprotos.networking.platform.responses.RemoveLoginActionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='wuprotos.networking.platform.responses.RemoveLoginActionResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='login_detail', full_name='wuprotos.networking.platform.responses.RemoveLoginActionResponse.login_detail', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=151,
  serialized_end=245,
)

_REMOVELOGINACTIONRESPONSE.fields_by_name['login_detail'].message_type = wuprotos_dot_data_dot_login__detail__pb2._LOGINDETAIL
DESCRIPTOR.message_types_by_name['RemoveLoginActionResponse'] = _REMOVELOGINACTIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RemoveLoginActionResponse = _reflection.GeneratedProtocolMessageType('RemoveLoginActionResponse', (_message.Message,), dict(
  DESCRIPTOR = _REMOVELOGINACTIONRESPONSE,
  __module__ = 'wuprotos.networking.platform.responses.remove_login_action_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.platform.responses.RemoveLoginActionResponse)
  ))
_sym_db.RegisterMessage(RemoveLoginActionResponse)


# @@protoc_insertion_point(module_scope)
