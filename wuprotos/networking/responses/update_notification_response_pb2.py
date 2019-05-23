# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/update_notification_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from wuprotos.enums import notification_state_pb2 as wuprotos_dot_enums_dot_notification__state__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/update_notification_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n@wuprotos/networking/responses/update_notification_response.proto\x12\x1dwuprotos.networking.responses\x1a\'wuprotos/enums/notification_state.proto\"\x85\x01\n\x1aUpdateNotificationResponse\x12\x18\n\x10notification_ids\x18\x01 \x03(\t\x12\x1b\n\x13\x63reate_timestamp_ms\x18\x02 \x03(\x03\x12\x30\n\x05state\x18\x03 \x01(\x0e\x32!.wuprotos.enums.NotificationStateb\x06proto3')
  ,
  dependencies=[wuprotos_dot_enums_dot_notification__state__pb2.DESCRIPTOR,])




_UPDATENOTIFICATIONRESPONSE = _descriptor.Descriptor(
  name='UpdateNotificationResponse',
  full_name='wuprotos.networking.responses.UpdateNotificationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='notification_ids', full_name='wuprotos.networking.responses.UpdateNotificationResponse.notification_ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_timestamp_ms', full_name='wuprotos.networking.responses.UpdateNotificationResponse.create_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='state', full_name='wuprotos.networking.responses.UpdateNotificationResponse.state', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=141,
  serialized_end=274,
)

_UPDATENOTIFICATIONRESPONSE.fields_by_name['state'].enum_type = wuprotos_dot_enums_dot_notification__state__pb2._NOTIFICATIONSTATE
DESCRIPTOR.message_types_by_name['UpdateNotificationResponse'] = _UPDATENOTIFICATIONRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UpdateNotificationResponse = _reflection.GeneratedProtocolMessageType('UpdateNotificationResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATENOTIFICATIONRESPONSE,
  __module__ = 'wuprotos.networking.responses.update_notification_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.UpdateNotificationResponse)
  ))
_sym_db.RegisterMessage(UpdateNotificationResponse)


# @@protoc_insertion_point(module_scope)
