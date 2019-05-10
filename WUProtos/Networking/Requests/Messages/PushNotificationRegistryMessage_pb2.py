# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Requests/Messages/PushNotificationRegistryMessage.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data.Token import ApnToken_pb2 as WUProtos_dot_Data_dot_Token_dot_ApnToken__pb2
from WUProtos.Data.Token import GcmToken_pb2 as WUProtos_dot_Data_dot_Token_dot_GcmToken__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Requests/Messages/PushNotificationRegistryMessage.proto',
  package='WUProtos.Networking.Requests.Messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nKWUProtos/Networking/Requests/Messages/PushNotificationRegistryMessage.proto\x12%WUProtos.Networking.Requests.Messages\x1a\"WUProtos/Data/Token/ApnToken.proto\x1a\"WUProtos/Data/Token/GcmToken.proto\"\x85\x01\n\x1fPushNotificationRegistryMessage\x12\x30\n\tapn_token\x18\x01 \x01(\x0b\x32\x1d.WUProtos.Data.Token.ApnToken\x12\x30\n\tgcm_token\x18\x02 \x01(\x0b\x32\x1d.WUProtos.Data.Token.GcmTokenb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_Token_dot_ApnToken__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_Token_dot_GcmToken__pb2.DESCRIPTOR,])




_PUSHNOTIFICATIONREGISTRYMESSAGE = _descriptor.Descriptor(
  name='PushNotificationRegistryMessage',
  full_name='WUProtos.Networking.Requests.Messages.PushNotificationRegistryMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apn_token', full_name='WUProtos.Networking.Requests.Messages.PushNotificationRegistryMessage.apn_token', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gcm_token', full_name='WUProtos.Networking.Requests.Messages.PushNotificationRegistryMessage.gcm_token', index=1,
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
  serialized_start=191,
  serialized_end=324,
)

_PUSHNOTIFICATIONREGISTRYMESSAGE.fields_by_name['apn_token'].message_type = WUProtos_dot_Data_dot_Token_dot_ApnToken__pb2._APNTOKEN
_PUSHNOTIFICATIONREGISTRYMESSAGE.fields_by_name['gcm_token'].message_type = WUProtos_dot_Data_dot_Token_dot_GcmToken__pb2._GCMTOKEN
DESCRIPTOR.message_types_by_name['PushNotificationRegistryMessage'] = _PUSHNOTIFICATIONREGISTRYMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PushNotificationRegistryMessage = _reflection.GeneratedProtocolMessageType('PushNotificationRegistryMessage', (_message.Message,), dict(
  DESCRIPTOR = _PUSHNOTIFICATIONREGISTRYMESSAGE,
  __module__ = 'WUProtos.Networking.Requests.Messages.PushNotificationRegistryMessage_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Requests.Messages.PushNotificationRegistryMessage)
  ))
_sym_db.RegisterMessage(PushNotificationRegistryMessage)


# @@protoc_insertion_point(module_scope)