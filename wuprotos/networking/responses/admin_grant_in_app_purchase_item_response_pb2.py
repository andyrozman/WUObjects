# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wuprotos/networking/responses/admin_grant_in_app_purchase_item_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='wuprotos/networking/responses/admin_grant_in_app_purchase_item_response.proto',
  package='wuprotos.networking.responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\nMwuprotos/networking/responses/admin_grant_in_app_purchase_item_response.proto\x12\x1dwuprotos.networking.responses\"\xaf\x01\n#AdminGrantInAppPurchaseItemResponse\x12Y\n\x06status\x18\x01 \x01(\x0e\x32I.wuprotos.networking.responses.AdminGrantInAppPurchaseItemResponse.Status\"-\n\x06Status\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x0b\n\x07\x46\x41ILURE\x10\x02\x62\x06proto3')
)



_ADMINGRANTINAPPPURCHASEITEMRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='wuprotos.networking.responses.AdminGrantInAppPurchaseItemResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=243,
  serialized_end=288,
)
_sym_db.RegisterEnumDescriptor(_ADMINGRANTINAPPPURCHASEITEMRESPONSE_STATUS)


_ADMINGRANTINAPPPURCHASEITEMRESPONSE = _descriptor.Descriptor(
  name='AdminGrantInAppPurchaseItemResponse',
  full_name='wuprotos.networking.responses.AdminGrantInAppPurchaseItemResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='wuprotos.networking.responses.AdminGrantInAppPurchaseItemResponse.status', index=0,
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
    _ADMINGRANTINAPPPURCHASEITEMRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=113,
  serialized_end=288,
)

_ADMINGRANTINAPPPURCHASEITEMRESPONSE.fields_by_name['status'].enum_type = _ADMINGRANTINAPPPURCHASEITEMRESPONSE_STATUS
_ADMINGRANTINAPPPURCHASEITEMRESPONSE_STATUS.containing_type = _ADMINGRANTINAPPPURCHASEITEMRESPONSE
DESCRIPTOR.message_types_by_name['AdminGrantInAppPurchaseItemResponse'] = _ADMINGRANTINAPPPURCHASEITEMRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AdminGrantInAppPurchaseItemResponse = _reflection.GeneratedProtocolMessageType('AdminGrantInAppPurchaseItemResponse', (_message.Message,), dict(
  DESCRIPTOR = _ADMINGRANTINAPPPURCHASEITEMRESPONSE,
  __module__ = 'wuprotos.networking.responses.admin_grant_in_app_purchase_item_response_pb2'
  # @@protoc_insertion_point(class_scope:wuprotos.networking.responses.AdminGrantInAppPurchaseItemResponse)
  ))
_sym_db.RegisterMessage(AdminGrantInAppPurchaseItemResponse)


# @@protoc_insertion_point(module_scope)
