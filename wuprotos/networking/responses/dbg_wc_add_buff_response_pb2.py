# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/dbg_wc_add_buff_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/dbg_wc_add_buff_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n<wuprotos/networking/responses/dbg_wc_add_buff_response.proto\x12\x1dwuprotos.networking.responses\"\x16\n\x14\x44\x62gWcAddBuffResponseb\x06proto3')
)




_DBGWCADDBUFFRESPONSE = _descriptor.Descriptor(
  name='DbgWcAddBuffResponse',
  full_name='wuprotos.networking.responses.DbgWcAddBuffResponse',
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
  serialized_start=95,
  serialized_end=117,
)

DESCRIPTOR.message_types_by_name['DbgWcAddBuffResponse'] = _DBGWCADDBUFFRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DbgWcAddBuffResponse = _reflection.GeneratedProtocolMessageType('DbgWcAddBuffResponse', (_message.Message,), dict(
  DESCRIPTOR = _DBGWCADDBUFFRESPONSE,
  __module__ = 'wuprotos.networking.responses.dbg_wc_add_buff_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.DbgWcAddBuffResponse)
  ))
_sym_db.RegisterMessage(DbgWcAddBuffResponse)


# @@protoc_insertion_point(module_scope)
