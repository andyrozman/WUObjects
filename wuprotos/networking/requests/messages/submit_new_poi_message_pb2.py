# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/requests/messages/submit_new_poi_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/requests/messages/submit_new_poi_message.proto',
  package='wuprotos.networking.requests.messages',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nBwuprotos/networking/requests/messages/submit_new_poi_message.proto\x12%wuprotos.networking.requests.messages\"\x80\x02\n\x13SubmitNewPoiMessage\x12\r\n\x05title\x18\x01 \x01(\t\x12\x18\n\x10long_description\x18\x02 \x01(\t\x12\x1a\n\x12image_gs_file_path\x18\x03 \x01(\t\x12\x0e\n\x06lat_e6\x18\x04 \x01(\x05\x12\x0e\n\x06lng_e6\x18\x05 \x01(\x05\x12\x19\n\x11image_serving_url\x18\x06 \x01(\t\x12%\n\x1dsupporting_image_gs_file_path\x18\x0c \x01(\t\x12$\n\x1csupporting_image_serving_url\x18\r \x01(\t\x12\x1c\n\x14supporting_statement\x18\x0e \x01(\tb\x06proto3')
)




_SUBMITNEWPOIMESSAGE = _descriptor.Descriptor(
  name='SubmitNewPoiMessage',
  full_name='wuprotos.networking.requests.messages.SubmitNewPoiMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='title', full_name='wuprotos.networking.requests.messages.SubmitNewPoiMessage.title', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_description', full_name='wuprotos.networking.requests.messages.SubmitNewPoiMessage.long_description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_gs_file_path', full_name='wuprotos.networking.requests.messages.SubmitNewPoiMessage.image_gs_file_path', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lat_e6', full_name='wuprotos.networking.requests.messages.SubmitNewPoiMessage.lat_e6', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lng_e6', full_name='wuprotos.networking.requests.messages.SubmitNewPoiMessage.lng_e6', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image_serving_url', full_name='wuprotos.networking.requests.messages.SubmitNewPoiMessage.image_serving_url', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supporting_image_gs_file_path', full_name='wuprotos.networking.requests.messages.SubmitNewPoiMessage.supporting_image_gs_file_path', index=6,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supporting_image_serving_url', full_name='wuprotos.networking.requests.messages.SubmitNewPoiMessage.supporting_image_serving_url', index=7,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='supporting_statement', full_name='wuprotos.networking.requests.messages.SubmitNewPoiMessage.supporting_statement', index=8,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=110,
  serialized_end=366,
)

DESCRIPTOR.message_types_by_name['SubmitNewPoiMessage'] = _SUBMITNEWPOIMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubmitNewPoiMessage = _reflection.GeneratedProtocolMessageType('SubmitNewPoiMessage', (_message.Message,), dict(
  DESCRIPTOR = _SUBMITNEWPOIMESSAGE,
  __module__ = 'wuprotos.networking.requests.messages.submit_new_poi_message_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.requests.messages.SubmitNewPoiMessage)
  ))
_sym_db.RegisterMessage(SubmitNewPoiMessage)


# @@protoc_insertion_point(module_scope)
