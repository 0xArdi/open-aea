# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: unixfs.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="unixfs.proto",
    package="unixfs.pb",
    syntax="proto2",
    serialized_options=None,
    serialized_pb=_b(
        '\n\x0cunixfs.proto\x12\tunixfs.pb"\xdc\x01\n\x04\x44\x61ta\x12&\n\x04Type\x18\x01 \x02(\x0e\x32\x18.unixfs.pb.Data.DataType\x12\x0c\n\x04\x44\x61ta\x18\x02 \x01(\x0c\x12\x10\n\x08\x66ilesize\x18\x03 \x01(\x04\x12\x12\n\nblocksizes\x18\x04 \x03(\x04\x12\x10\n\x08hashType\x18\x05 \x01(\x04\x12\x0e\n\x06\x66\x61nout\x18\x06 \x01(\x04"V\n\x08\x44\x61taType\x12\x07\n\x03Raw\x10\x00\x12\r\n\tDirectory\x10\x01\x12\x08\n\x04\x46ile\x10\x02\x12\x0c\n\x08Metadata\x10\x03\x12\x0b\n\x07Symlink\x10\x04\x12\r\n\tHAMTShard\x10\x05"\x1c\n\x08Metadata\x12\x10\n\x08MimeType\x18\x01 \x01(\t'
    ),
)


_DATA_DATATYPE = _descriptor.EnumDescriptor(
    name="DataType",
    full_name="unixfs.pb.Data.DataType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="Raw", index=0, number=0, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="Directory", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="File", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="Metadata", index=3, number=3, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="Symlink", index=4, number=4, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="HAMTShard", index=5, number=5, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=162,
    serialized_end=248,
)
_sym_db.RegisterEnumDescriptor(_DATA_DATATYPE)


_DATA = _descriptor.Descriptor(
    name="Data",
    full_name="unixfs.pb.Data",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="Type",
            full_name="unixfs.pb.Data.Type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=2,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="Data",
            full_name="unixfs.pb.Data.Data",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b(""),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="filesize",
            full_name="unixfs.pb.Data.filesize",
            index=2,
            number=3,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="blocksizes",
            full_name="unixfs.pb.Data.blocksizes",
            index=3,
            number=4,
            type=4,
            cpp_type=4,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="hashType",
            full_name="unixfs.pb.Data.hashType",
            index=4,
            number=5,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="fanout",
            full_name="unixfs.pb.Data.fanout",
            index=5,
            number=6,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[
        _DATA_DATATYPE,
    ],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=28,
    serialized_end=248,
)


_METADATA = _descriptor.Descriptor(
    name="Metadata",
    full_name="unixfs.pb.Metadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="MimeType",
            full_name="unixfs.pb.Metadata.MimeType",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto2",
    extension_ranges=[],
    oneofs=[],
    serialized_start=250,
    serialized_end=278,
)

_DATA.fields_by_name["Type"].enum_type = _DATA_DATATYPE
_DATA_DATATYPE.containing_type = _DATA
DESCRIPTOR.message_types_by_name["Data"] = _DATA
DESCRIPTOR.message_types_by_name["Metadata"] = _METADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Data = _reflection.GeneratedProtocolMessageType(
    "Data",
    (_message.Message,),
    dict(
        DESCRIPTOR=_DATA,
        __module__="unixfs_pb2"
        # @@protoc_insertion_point(class_scope:unixfs.pb.Data)
    ),
)
_sym_db.RegisterMessage(Data)

Metadata = _reflection.GeneratedProtocolMessageType(
    "Metadata",
    (_message.Message,),
    dict(
        DESCRIPTOR=_METADATA,
        __module__="unixfs_pb2"
        # @@protoc_insertion_point(class_scope:unixfs.pb.Metadata)
    ),
)
_sym_db.RegisterMessage(Metadata)


# @@protoc_insertion_point(module_scope)
