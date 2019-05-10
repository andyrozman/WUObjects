# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WUProtos/Networking/Responses/GetOutpostDetailsResponse.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from WUProtos.Data import OutpostMenu_pb2 as WUProtos_dot_Data_dot_OutpostMenu__pb2
from WUProtos.Data import PoiDetails_pb2 as WUProtos_dot_Data_dot_PoiDetails__pb2
from WUProtos.Enums import PoiAccessibility_pb2 as WUProtos_dot_Enums_dot_PoiAccessibility__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='WUProtos/Networking/Responses/GetOutpostDetailsResponse.proto',
  package='WUProtos.Networking.Responses',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n=WUProtos/Networking/Responses/GetOutpostDetailsResponse.proto\x12\x1dWUProtos.Networking.Responses\x1a\x1fWUProtos/Data/OutpostMenu.proto\x1a\x1eWUProtos/Data/PoiDetails.proto\x1a%WUProtos/Enums/PoiAccessibility.proto\"\xe2\x01\n\x19GetOutpostDetailsResponse\x12\x12\n\nimage_urls\x18\x01 \x03(\t\x12\x30\n\x0c\x63urrent_menu\x18\x02 \x01(\x0b\x32\x1a.WUProtos.Data.OutpostMenu\x12\x12\n\npartner_id\x18\x03 \x01(\t\x12.\n\x0bpoi_details\x18\x04 \x01(\x0b\x32\x19.WUProtos.Data.PoiDetails\x12;\n\x11poi_accessibility\x18\x05 \x01(\x0e\x32 .WUProtos.Enums.PoiAccessibilityb\x06proto3')
  ,
  dependencies=[WUProtos_dot_Data_dot_OutpostMenu__pb2.DESCRIPTOR,WUProtos_dot_Data_dot_PoiDetails__pb2.DESCRIPTOR,WUProtos_dot_Enums_dot_PoiAccessibility__pb2.DESCRIPTOR,])




_GETOUTPOSTDETAILSRESPONSE = _descriptor.Descriptor(
  name='GetOutpostDetailsResponse',
  full_name='WUProtos.Networking.Responses.GetOutpostDetailsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_urls', full_name='WUProtos.Networking.Responses.GetOutpostDetailsResponse.image_urls', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_menu', full_name='WUProtos.Networking.Responses.GetOutpostDetailsResponse.current_menu', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='partner_id', full_name='WUProtos.Networking.Responses.GetOutpostDetailsResponse.partner_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poi_details', full_name='WUProtos.Networking.Responses.GetOutpostDetailsResponse.poi_details', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poi_accessibility', full_name='WUProtos.Networking.Responses.GetOutpostDetailsResponse.poi_accessibility', index=4,
      number=5, type=14, cpp_type=8, label=1,
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
  serialized_start=201,
  serialized_end=427,
)

_GETOUTPOSTDETAILSRESPONSE.fields_by_name['current_menu'].message_type = WUProtos_dot_Data_dot_OutpostMenu__pb2._OUTPOSTMENU
_GETOUTPOSTDETAILSRESPONSE.fields_by_name['poi_details'].message_type = WUProtos_dot_Data_dot_PoiDetails__pb2._POIDETAILS
_GETOUTPOSTDETAILSRESPONSE.fields_by_name['poi_accessibility'].enum_type = WUProtos_dot_Enums_dot_PoiAccessibility__pb2._POIACCESSIBILITY
DESCRIPTOR.message_types_by_name['GetOutpostDetailsResponse'] = _GETOUTPOSTDETAILSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetOutpostDetailsResponse = _reflection.GeneratedProtocolMessageType('GetOutpostDetailsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETOUTPOSTDETAILSRESPONSE,
  __module__ = 'WUProtos.Networking.Responses.GetOutpostDetailsResponse_pb2'
  # @@protoc_insertion_point(class_scope:WUProtos.Networking.Responses.GetOutpostDetailsResponse)
  ))
_sym_db.RegisterMessage(GetOutpostDetailsResponse)


# @@protoc_insertion_point(module_scope)