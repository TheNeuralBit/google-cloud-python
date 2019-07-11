# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/tables.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.cloud.automl_v1beta1.proto import (
    classification_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    column_spec_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_column__spec__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    data_items_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_data__items__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    data_stats_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_data__stats__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    ranges_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_ranges__pb2,
)
from google.cloud.automl_v1beta1.proto import (
    temporal_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_temporal__pb2,
)
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/tables.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n\037com.google.cloud.automl.v1beta1P\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1\352\002\036Google::Cloud::AutoML::V1beta1"
    ),
    serialized_pb=_b(
        '\n.google/cloud/automl_v1beta1/proto/tables.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x36google/cloud/automl_v1beta1/proto/classification.proto\x1a\x33google/cloud/automl_v1beta1/proto/column_spec.proto\x1a\x32google/cloud/automl_v1beta1/proto/data_items.proto\x1a\x32google/cloud/automl_v1beta1/proto/data_stats.proto\x1a.google/cloud/automl_v1beta1/proto/ranges.proto\x1a\x30google/cloud/automl_v1beta1/proto/temporal.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/api/annotations.proto"\xb0\x03\n\x15TablesDatasetMetadata\x12\x1d\n\x15primary_table_spec_id\x18\x01 \x01(\t\x12\x1d\n\x15target_column_spec_id\x18\x02 \x01(\t\x12\x1d\n\x15weight_column_spec_id\x18\x03 \x01(\t\x12\x1d\n\x15ml_use_column_spec_id\x18\x04 \x01(\t\x12t\n\x1atarget_column_correlations\x18\x06 \x03(\x0b\x32P.google.cloud.automl.v1beta1.TablesDatasetMetadata.TargetColumnCorrelationsEntry\x12\x35\n\x11stats_update_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1an\n\x1dTargetColumnCorrelationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b\x32-.google.cloud.automl.v1beta1.CorrelationStats:\x02\x38\x01"\x96\x04\n\x13TablesModelMetadata\x12\x43\n\x12target_column_spec\x18\x02 \x01(\x0b\x32\'.google.cloud.automl.v1beta1.ColumnSpec\x12K\n\x1ainput_feature_column_specs\x18\x03 \x03(\x0b\x32\'.google.cloud.automl.v1beta1.ColumnSpec\x12\x1e\n\x16optimization_objective\x18\x04 \x01(\t\x12-\n#optimization_objective_recall_value\x18\x11 \x01(\x02H\x00\x12\x30\n&optimization_objective_precision_value\x18\x12 \x01(\x02H\x00\x12T\n\x18tables_model_column_info\x18\x05 \x03(\x0b\x32\x32.google.cloud.automl.v1beta1.TablesModelColumnInfo\x12%\n\x1dtrain_budget_milli_node_hours\x18\x06 \x01(\x03\x12#\n\x1btrain_cost_milli_node_hours\x18\x07 \x01(\x03\x12\x1e\n\x16\x64isable_early_stopping\x18\x0c \x01(\x08\x42*\n(additional_optimization_objective_config"\xe5\x01\n\x10TablesAnnotation\x12\r\n\x05score\x18\x01 \x01(\x02\x12\x45\n\x13prediction_interval\x18\x04 \x01(\x0b\x32(.google.cloud.automl.v1beta1.DoubleRange\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value\x12T\n\x18tables_model_column_info\x18\x03 \x03(\x0b\x32\x32.google.cloud.automl.v1beta1.TablesModelColumnInfo"j\n\x15TablesModelColumnInfo\x12\x18\n\x10\x63olumn_spec_name\x18\x01 \x01(\t\x12\x1b\n\x13\x63olumn_display_name\x18\x02 \x01(\t\x12\x1a\n\x12\x66\x65\x61ture_importance\x18\x03 \x01(\x02\x42\xa5\x01\n\x1f\x63om.google.cloud.automl.v1beta1P\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1\xea\x02\x1eGoogle::Cloud::AutoML::V1beta1b\x06proto3'
    ),
    dependencies=[
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_column__spec__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_data__items__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_data__stats__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_ranges__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_temporal__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
    ],
)


_TABLESDATASETMETADATA_TARGETCOLUMNCORRELATIONSENTRY = _descriptor.Descriptor(
    name="TargetColumnCorrelationsEntry",
    full_name="google.cloud.automl.v1beta1.TablesDatasetMetadata.TargetColumnCorrelationsEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="google.cloud.automl.v1beta1.TablesDatasetMetadata.TargetColumnCorrelationsEntry.key",
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
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.automl.v1beta1.TablesDatasetMetadata.TargetColumnCorrelationsEntry.value",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    serialized_options=_b("8\001"),
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=806,
    serialized_end=916,
)

_TABLESDATASETMETADATA = _descriptor.Descriptor(
    name="TablesDatasetMetadata",
    full_name="google.cloud.automl.v1beta1.TablesDatasetMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="primary_table_spec_id",
            full_name="google.cloud.automl.v1beta1.TablesDatasetMetadata.primary_table_spec_id",
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
        _descriptor.FieldDescriptor(
            name="target_column_spec_id",
            full_name="google.cloud.automl.v1beta1.TablesDatasetMetadata.target_column_spec_id",
            index=1,
            number=2,
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
        _descriptor.FieldDescriptor(
            name="weight_column_spec_id",
            full_name="google.cloud.automl.v1beta1.TablesDatasetMetadata.weight_column_spec_id",
            index=2,
            number=3,
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
        _descriptor.FieldDescriptor(
            name="ml_use_column_spec_id",
            full_name="google.cloud.automl.v1beta1.TablesDatasetMetadata.ml_use_column_spec_id",
            index=3,
            number=4,
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
        _descriptor.FieldDescriptor(
            name="target_column_correlations",
            full_name="google.cloud.automl.v1beta1.TablesDatasetMetadata.target_column_correlations",
            index=4,
            number=6,
            type=11,
            cpp_type=10,
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
            name="stats_update_time",
            full_name="google.cloud.automl.v1beta1.TablesDatasetMetadata.stats_update_time",
            index=5,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    nested_types=[_TABLESDATASETMETADATA_TARGETCOLUMNCORRELATIONSENTRY],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=484,
    serialized_end=916,
)


_TABLESMODELMETADATA = _descriptor.Descriptor(
    name="TablesModelMetadata",
    full_name="google.cloud.automl.v1beta1.TablesModelMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="target_column_spec",
            full_name="google.cloud.automl.v1beta1.TablesModelMetadata.target_column_spec",
            index=0,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="input_feature_column_specs",
            full_name="google.cloud.automl.v1beta1.TablesModelMetadata.input_feature_column_specs",
            index=1,
            number=3,
            type=11,
            cpp_type=10,
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
            name="optimization_objective",
            full_name="google.cloud.automl.v1beta1.TablesModelMetadata.optimization_objective",
            index=2,
            number=4,
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
        _descriptor.FieldDescriptor(
            name="optimization_objective_recall_value",
            full_name="google.cloud.automl.v1beta1.TablesModelMetadata.optimization_objective_recall_value",
            index=3,
            number=17,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="optimization_objective_precision_value",
            full_name="google.cloud.automl.v1beta1.TablesModelMetadata.optimization_objective_precision_value",
            index=4,
            number=18,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="tables_model_column_info",
            full_name="google.cloud.automl.v1beta1.TablesModelMetadata.tables_model_column_info",
            index=5,
            number=5,
            type=11,
            cpp_type=10,
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
            name="train_budget_milli_node_hours",
            full_name="google.cloud.automl.v1beta1.TablesModelMetadata.train_budget_milli_node_hours",
            index=6,
            number=6,
            type=3,
            cpp_type=2,
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
            name="train_cost_milli_node_hours",
            full_name="google.cloud.automl.v1beta1.TablesModelMetadata.train_cost_milli_node_hours",
            index=7,
            number=7,
            type=3,
            cpp_type=2,
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
            name="disable_early_stopping",
            full_name="google.cloud.automl.v1beta1.TablesModelMetadata.disable_early_stopping",
            index=8,
            number=12,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
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
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="additional_optimization_objective_config",
            full_name="google.cloud.automl.v1beta1.TablesModelMetadata.additional_optimization_objective_config",
            index=0,
            containing_type=None,
            fields=[],
        )
    ],
    serialized_start=919,
    serialized_end=1453,
)


_TABLESANNOTATION = _descriptor.Descriptor(
    name="TablesAnnotation",
    full_name="google.cloud.automl.v1beta1.TablesAnnotation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="score",
            full_name="google.cloud.automl.v1beta1.TablesAnnotation.score",
            index=0,
            number=1,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="prediction_interval",
            full_name="google.cloud.automl.v1beta1.TablesAnnotation.prediction_interval",
            index=1,
            number=4,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="google.cloud.automl.v1beta1.TablesAnnotation.value",
            index=2,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="tables_model_column_info",
            full_name="google.cloud.automl.v1beta1.TablesAnnotation.tables_model_column_info",
            index=3,
            number=3,
            type=11,
            cpp_type=10,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1456,
    serialized_end=1685,
)


_TABLESMODELCOLUMNINFO = _descriptor.Descriptor(
    name="TablesModelColumnInfo",
    full_name="google.cloud.automl.v1beta1.TablesModelColumnInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="column_spec_name",
            full_name="google.cloud.automl.v1beta1.TablesModelColumnInfo.column_spec_name",
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
        _descriptor.FieldDescriptor(
            name="column_display_name",
            full_name="google.cloud.automl.v1beta1.TablesModelColumnInfo.column_display_name",
            index=1,
            number=2,
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
        _descriptor.FieldDescriptor(
            name="feature_importance",
            full_name="google.cloud.automl.v1beta1.TablesModelColumnInfo.feature_importance",
            index=2,
            number=3,
            type=2,
            cpp_type=6,
            label=1,
            has_default_value=False,
            default_value=float(0),
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
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1687,
    serialized_end=1793,
)

_TABLESDATASETMETADATA_TARGETCOLUMNCORRELATIONSENTRY.fields_by_name[
    "value"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_data__stats__pb2._CORRELATIONSTATS
)
_TABLESDATASETMETADATA_TARGETCOLUMNCORRELATIONSENTRY.containing_type = (
    _TABLESDATASETMETADATA
)
_TABLESDATASETMETADATA.fields_by_name[
    "target_column_correlations"
].message_type = _TABLESDATASETMETADATA_TARGETCOLUMNCORRELATIONSENTRY
_TABLESDATASETMETADATA.fields_by_name[
    "stats_update_time"
].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_TABLESMODELMETADATA.fields_by_name[
    "target_column_spec"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_column__spec__pb2._COLUMNSPEC
)
_TABLESMODELMETADATA.fields_by_name[
    "input_feature_column_specs"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_column__spec__pb2._COLUMNSPEC
)
_TABLESMODELMETADATA.fields_by_name[
    "tables_model_column_info"
].message_type = _TABLESMODELCOLUMNINFO
_TABLESMODELMETADATA.oneofs_by_name[
    "additional_optimization_objective_config"
].fields.append(
    _TABLESMODELMETADATA.fields_by_name["optimization_objective_recall_value"]
)
_TABLESMODELMETADATA.fields_by_name[
    "optimization_objective_recall_value"
].containing_oneof = _TABLESMODELMETADATA.oneofs_by_name[
    "additional_optimization_objective_config"
]
_TABLESMODELMETADATA.oneofs_by_name[
    "additional_optimization_objective_config"
].fields.append(
    _TABLESMODELMETADATA.fields_by_name["optimization_objective_precision_value"]
)
_TABLESMODELMETADATA.fields_by_name[
    "optimization_objective_precision_value"
].containing_oneof = _TABLESMODELMETADATA.oneofs_by_name[
    "additional_optimization_objective_config"
]
_TABLESANNOTATION.fields_by_name[
    "prediction_interval"
].message_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_ranges__pb2._DOUBLERANGE
)
_TABLESANNOTATION.fields_by_name[
    "value"
].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_TABLESANNOTATION.fields_by_name[
    "tables_model_column_info"
].message_type = _TABLESMODELCOLUMNINFO
DESCRIPTOR.message_types_by_name["TablesDatasetMetadata"] = _TABLESDATASETMETADATA
DESCRIPTOR.message_types_by_name["TablesModelMetadata"] = _TABLESMODELMETADATA
DESCRIPTOR.message_types_by_name["TablesAnnotation"] = _TABLESANNOTATION
DESCRIPTOR.message_types_by_name["TablesModelColumnInfo"] = _TABLESMODELCOLUMNINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TablesDatasetMetadata = _reflection.GeneratedProtocolMessageType(
    "TablesDatasetMetadata",
    (_message.Message,),
    dict(
        TargetColumnCorrelationsEntry=_reflection.GeneratedProtocolMessageType(
            "TargetColumnCorrelationsEntry",
            (_message.Message,),
            dict(
                DESCRIPTOR=_TABLESDATASETMETADATA_TARGETCOLUMNCORRELATIONSENTRY,
                __module__="google.cloud.automl_v1beta1.proto.tables_pb2"
                # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TablesDatasetMetadata.TargetColumnCorrelationsEntry)
            ),
        ),
        DESCRIPTOR=_TABLESDATASETMETADATA,
        __module__="google.cloud.automl_v1beta1.proto.tables_pb2",
        __doc__="""Metadata for a dataset used for AutoML Tables.
  
  
  Attributes:
      primary_table_spec_id:
          Output only. The table\_spec\_id of the primary table of this
          dataset.
      target_column_spec_id:
          column\_spec\_id of the primary table's column that should be
          used as the training & prediction target. This column must be
          non-nullable and have one of following data types (otherwise
          model creation will error): \* CATEGORY \* FLOAT64
          Furthermore, if the type is CATEGORY , then only up to 100
          unique values may exist in that column across all rows.  NOTE:
          Updates of this field will instantly affect any other users
          concurrently working with the dataset.
      weight_column_spec_id:
          column\_spec\_id of the primary table's column that should be
          used as the weight column, i.e. the higher the value the more
          important the row will be during model training. Required
          type: FLOAT64. Allowed values: 0 to 10000, inclusive on both
          ends; 0 means the row is ignored for training. If not set all
          rows are assumed to have equal weight of 1. NOTE: Updates of
          this field will instantly affect any other users concurrently
          working with the dataset.
      ml_use_column_spec_id:
          column\_spec\_id of the primary table column which specifies a
          possible ML use of the row, i.e. the column will be used to
          split the rows into TRAIN, VALIDATE and TEST sets. Required
          type: STRING. This column, if set, must either have all of
          ``TRAIN``, ``VALIDATE``, ``TEST`` among its values, or only
          have ``TEST``, ``UNASSIGNED`` values. In the latter case the
          rows with ``UNASSIGNED`` value will be assigned by AutoML.
          Note that if a given ml use distribution makes it impossible
          to create a "good" model, that call will error describing the
          issue. If both this column\_spec\_id and primary table's
          time\_column\_spec\_id are not set, then all rows are treated
          as ``UNASSIGNED``. NOTE: Updates of this field will instantly
          affect any other users concurrently working with the dataset.
      target_column_correlations:
          Output only. Correlations between  [TablesDatasetMetadata.targ
          et\_column\_spec\_id][google.cloud.automl.v1beta1.TablesDatase
          tMetadata.target\_column\_spec\_id], and other columns of the
          [TablesDatasetMetadataprimary\_table][google.cloud.automl.v1be
          ta1.TablesDatasetMetadata.primary\_table\_spec\_id]. Only set
          if the target column is set. Mapping from other column spec id
          to its CorrelationStats with the target column. This field may
          be stale, see the stats\_update\_time field for for the
          timestamp at which these stats were last updated.
      stats_update_time:
          The most recent timestamp when target\_column\_correlations
          field and all descendant ColumnSpec.data\_stats and
          ColumnSpec.top\_correlated\_columns fields were last
          (re-)generated. Any changes that happened to the dataset
          afterwards are not reflected in these fields values. The
          regeneration happens in the background on a best effort basis.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TablesDatasetMetadata)
    ),
)
_sym_db.RegisterMessage(TablesDatasetMetadata)
_sym_db.RegisterMessage(TablesDatasetMetadata.TargetColumnCorrelationsEntry)

TablesModelMetadata = _reflection.GeneratedProtocolMessageType(
    "TablesModelMetadata",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TABLESMODELMETADATA,
        __module__="google.cloud.automl_v1beta1.proto.tables_pb2",
        __doc__="""Model metadata specific to AutoML Tables.
  
  
  Attributes:
      target_column_spec:
          Column spec of the dataset's primary table's column the model
          is predicting. Snapshotted when model creation started. Only 3
          fields are used: name - May be set on CreateModel, if it's not
          then the ColumnSpec corresponding to the current
          target\_column\_spec\_id of the dataset the model is trained
          from is used. If neither is set, CreateModel will error.
          display\_name - Output only. data\_type - Output only.
      input_feature_column_specs:
          Column specs of the dataset's primary table's columns, on
          which the model is trained and which are used as the input for
          predictions. The  [target\_column][google.cloud.automl.v1beta1
          .TablesModelMetadata.target\_column\_spec] as well as,
          according to dataset's state upon model creation,  [weight\_co
          lumn][google.cloud.automl.v1beta1.TablesDatasetMetadata.weight
          \_column\_spec\_id], and  [ml\_use\_column][google.cloud.autom
          l.v1beta1.TablesDatasetMetadata.ml\_use\_column\_spec\_id]
          must never be included here. Only 3 fields are used: name -
          May be set on CreateModel, if set only the columns specified
          are used, otherwise all primary table's columns (except the
          ones listed above) are used for the training and prediction
          input. display\_name - Output only. data\_type - Output only.
      optimization_objective:
          Objective function the model is optimizing towards. The
          training process creates a model that maximizes/minimizes the
          value of the objective function over the validation set.  The
          supported optimization objectives depend on the prediction
          type. If the field is not set, a default objective function is
          used.  CLASSIFICATION\_BINARY: "MAXIMIZE\_AU\_ROC" (default) -
          Maximize the area under the receiver operating characteristic
          (ROC) curve. "MINIMIZE\_LOG\_LOSS" - Minimize log loss.
          "MAXIMIZE\_AU\_PRC" - Maximize the area under the precision-
          recall curve. "MAXIMIZE\_PRECISION\_AT\_RECALL" - Maximize
          precision for a specified recall value.
          "MAXIMIZE\_RECALL\_AT\_PRECISION" - Maximize recall for a
          specified precision value.  CLASSIFICATION\_MULTI\_CLASS :
          "MINIMIZE\_LOG\_LOSS" (default) - Minimize log loss.
          REGRESSION: "MINIMIZE\_RMSE" (default) - Minimize root-mean-
          squared error (RMSE). "MINIMIZE\_MAE" - Minimize mean-absolute
          error (MAE). "MINIMIZE\_RMSLE" - Minimize root-mean-squared
          log error (RMSLE).  FORECASTING: "MINIMIZE\_RMSE" (default) -
          Minimize root-mean-squared error (RMSE). "MINIMIZE\_MAE" -
          Minimize mean-absolute error (MAE).
      additional_optimization_objective_config:
          Additional optimization objective configuration. Required for
          ``MAXIMIZE_PRECISION_AT_RECALL`` and
          ``MAXIMIZE_RECALL_AT_PRECISION``, otherwise unused.
      optimization_objective_recall_value:
          Required when optimization\_objective is
          "MAXIMIZE\_PRECISION\_AT\_RECALL". Must be between 0 and 1,
          inclusive.
      optimization_objective_precision_value:
          Required when optimization\_objective is
          "MAXIMIZE\_RECALL\_AT\_PRECISION". Must be between 0 and 1,
          inclusive.
      tables_model_column_info:
          Output only. Auxiliary information for each of the
          input\_feature\_column\_specs with respect to this particular
          model.
      train_budget_milli_node_hours:
          Required. The train budget of creating this model, expressed
          in milli node hours i.e. 1,000 value in this field means 1
          node hour.  The training cost of the model will not exceed
          this budget. The final cost will be attempted to be close to
          the budget, though may end up being (even) noticeably smaller
          - at the backend's discretion. This especially may happen when
          further model training ceases to provide any improvements.  If
          the budget is set to a value known to be insufficient to train
          a model for the given dataset, the training won't be attempted
          and will error.  The train budget must be between 1,000 and
          72,000 milli node hours, inclusive.
      train_cost_milli_node_hours:
          Output only. The actual training cost of the model, expressed
          in milli node hours, i.e. 1,000 value in this field means 1
          node hour. Guaranteed to not exceed the train budget.
      disable_early_stopping:
          Use the entire training budget. This disables the early
          stopping feature. By default, the early stopping feature is
          enabled, which means that AutoML Tables might stop training
          before the entire training budget has been used.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TablesModelMetadata)
    ),
)
_sym_db.RegisterMessage(TablesModelMetadata)

TablesAnnotation = _reflection.GeneratedProtocolMessageType(
    "TablesAnnotation",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TABLESANNOTATION,
        __module__="google.cloud.automl_v1beta1.proto.tables_pb2",
        __doc__="""Contains annotation details specific to Tables.
  
  
  Attributes:
      score:
          Output only. A confidence estimate between 0.0 and 1.0,
          inclusive. A higher value means greater confidence in the
          returned value. For  [target\_column\_spec][google.cloud.autom
          l.v1beta1.TablesModelMetadata.target\_column\_spec] of FLOAT64
          data type the score is not populated.
      prediction_interval:
          Output only. Only populated when  [target\_column\_spec][googl
          e.cloud.automl.v1beta1.TablesModelMetadata.target\_column\_spe
          c] has FLOAT64 data type. An interval in which the exactly
          correct target value has 95% chance to be in.
      value:
          The predicted value of the row's  [target\_column][google.clou
          d.automl.v1beta1.TablesModelMetadata.target\_column\_spec].
          The value depends on the column's DataType: CATEGORY - the
          predicted (with the above confidence ``score``) CATEGORY
          value. FLOAT64 - the predicted (with above
          ``prediction_interval``) FLOAT64 value.
      tables_model_column_info:
          Output only. Auxiliary information for each of the model's  [i
          nput\_feature\_column\_specs][google.cloud.automl.v1beta1.Tabl
          esModelMetadata.input\_feature\_column\_specs] with respect to
          this particular prediction. If no other fields than  [column\_
          spec\_name][google.cloud.automl.v1beta1.TablesModelColumnInfo.
          column\_spec\_name] and  [column\_display\_name][google.cloud.
          automl.v1beta1.TablesModelColumnInfo.column\_display\_name]
          would be populated, then this whole field is not.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TablesAnnotation)
    ),
)
_sym_db.RegisterMessage(TablesAnnotation)

TablesModelColumnInfo = _reflection.GeneratedProtocolMessageType(
    "TablesModelColumnInfo",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TABLESMODELCOLUMNINFO,
        __module__="google.cloud.automl_v1beta1.proto.tables_pb2",
        __doc__="""An information specific to given column and Tables Model, in context of
  the Model and the predictions created by it.
  
  
  Attributes:
      column_spec_name:
          Output only. The name of the ColumnSpec describing the column.
          Not populated when this proto is outputted to BigQuery.
      column_display_name:
          Output only. The display name of the column (same as the
          display\_name of its ColumnSpec).
      feature_importance:
          Output only.  When given as part of a Model (always
          populated): Measurement of how much model predictions
          correctness on the TEST data depend on values in this column.
          A value between 0 and 1, higher means higher influence. These
          values are normalized - for all input feature columns of a
          given model they add to 1.  When given back by Predict
          (populated iff [feature\_importance
          param][google.cloud.automl.v1beta1.PredictRequest.params] is
          set) or Batch Predict (populated iff [feature\_importance][goo
          gle.cloud.automl.v1beta1.PredictRequest.params] param is set):
          Measurement of how impactful for the prediction returned for
          the given row the value in this column was. A value between 0
          and 1, higher means larger impact. These values are normalized
          - for all input feature columns of a single predicted row they
          add to 1.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TablesModelColumnInfo)
    ),
)
_sym_db.RegisterMessage(TablesModelColumnInfo)


DESCRIPTOR._options = None
_TABLESDATASETMETADATA_TARGETCOLUMNCORRELATIONSENTRY._options = None
# @@protoc_insertion_point(module_scope)
