# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/quest_acquire_dailies_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/quest_acquire_dailies_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nIwuprotos/networking/requests/messages/quest_acquire_dailies_message.proto\x12%wuprotos.networking.requests.messages\"\x1c\n\x1aQuestAcquireDailiesMessageb\x06proto3')
)




_QUESTACQUIREDAILIESMESSAGE = _descriptor.Descriptor(
  name='QuestAcquireDailiesMessage',
  full_name='wuprotos.networking.requests.messages.QuestAcquireDailiesMessage',
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
  serialized_start=116,
  serialized_end=144,
)

DESCRIPTOR.message_types_by_name['QuestAcquireDailiesMessage'] = _QUESTACQUIREDAILIESMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

QuestAcquireDailiesMessage = _reflection.GeneratedProtocolMessageType('QuestAcquireDailiesMessage', (_message.Message,), dict(
  DESCRIPTOR = _QUESTACQUIREDAILIESMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.quest_acquire_dailies_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.QuestAcquireDailiesMessage)
  ))
_sym_db.RegisterMessage(QuestAcquireDailiesMessage)


# @@protoc_insertion_point(module_scope)
