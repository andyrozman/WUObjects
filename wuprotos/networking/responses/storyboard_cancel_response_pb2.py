# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/storyboard_cancel_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/storyboard_cancel_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n>wuprotos/networking/responses/storyboard_cancel_response.proto\x12\x1dwuprotos.networking.responses\"\xc9\x01\n\x18StoryboardCancelResponse\x12N\n\x06status\x18\x01 \x01(\x0e\x32>.wuprotos.networking.responses.StoryboardCancelResponse.Status\"]\n\x06Status\x12\x1b\n\x17STORYBOARD_SKIP_UNKNOWN\x10\x00\x12\x1b\n\x17STORYBOARD_SKIP_SUCCESS\x10\x01\x12\x19\n\x15STORYBOARD_SKIP_ERROR\x10\x02\x62\x06proto3')
)



_STORYBOARDCANCELRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='wuprotos.networking.responses.StoryboardCancelResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STORYBOARD_SKIP_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORYBOARD_SKIP_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORYBOARD_SKIP_ERROR', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=206,
  serialized_end=299,
)
_sym_db.RegisterEnumDescriptor(_STORYBOARDCANCELRESPONSE_STATUS)


_STORYBOARDCANCELRESPONSE = _descriptor.Descriptor(
  name='StoryboardCancelResponse',
  full_name='wuprotos.networking.responses.StoryboardCancelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wuprotos.networking.responses.StoryboardCancelResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STORYBOARDCANCELRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=299,
)

_STORYBOARDCANCELRESPONSE.fields_by_name['status'].enum_type = _STORYBOARDCANCELRESPONSE_STATUS
_STORYBOARDCANCELRESPONSE_STATUS.containing_type = _STORYBOARDCANCELRESPONSE
DESCRIPTOR.message_types_by_name['StoryboardCancelResponse'] = _STORYBOARDCANCELRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StoryboardCancelResponse = _reflection.GeneratedProtocolMessageType('StoryboardCancelResponse', (_message.Message,), dict(
  DESCRIPTOR = _STORYBOARDCANCELRESPONSE,
  __module__ = 'wuprotos.networking.responses.storyboard_cancel_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.StoryboardCancelResponse)
  ))
_sym_db.RegisterMessage(StoryboardCancelResponse)


# @@protoc_insertion_point(module_scope)
