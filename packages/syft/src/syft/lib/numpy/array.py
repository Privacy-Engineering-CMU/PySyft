# third party
import numpy as np
import pyarrow as pa
import torch

# relative
from ...core.common.serde.serializable import serializable
from ...experimental_flags import flags
from ...proto.lib.numpy.array_pb2 import NumpyProto
from ..torch.tensor_util import tensor_deserializer
from ..torch.tensor_util import tensor_serializer

SUPPORTED_BOOL_TYPES = [np.bool_]
SUPPORTED_INT_TYPES = [
    np.int8,
    np.int16,
    np.int32,
    np.int64,
    np.uint8,
    np.uint16,
    np.uint32,
    np.uint64,
]

SUPPORTED_FLOAT_TYPES = [
    np.float16,
    np.float32,
    np.float64,
]

SUPPORTED_DTYPES = SUPPORTED_BOOL_TYPES + SUPPORTED_INT_TYPES + SUPPORTED_FLOAT_TYPES

DTYPE_REFACTOR = {
    np.dtype("uint16"): np.int16,
    np.dtype("uint32"): np.int32,
    np.dtype("uint64"): np.int64,
}


def arrow_serialize(obj: np.ndarray) -> bytes:
    original_dtype = obj.dtype
    apache_arrow = pa.Tensor.from_numpy(obj=obj)
    sink = pa.BufferOutputStream()
    pa.ipc.write_tensor(apache_arrow, sink)
    numpy_bytes = sink.getvalue().to_pybytes()
    dtype = original_dtype.name
    return NumpyProto(arrow_data=numpy_bytes, dtype=dtype)


def arrow_deserialize(proto: NumpyProto) -> np.ndarray:
    buf: bytes = proto.arrow_data
    str_dtype = proto.dtype
    original_dtype = np.dtype(str_dtype)
    reader = pa.BufferReader(buf)
    buf = reader.read_buffer()
    result = pa.ipc.read_tensor(buf)
    np_array = result.to_numpy()
    np_array.setflags(write=True)
    return np_array.astype(original_dtype)


def protobuf_serialize(obj: np.ndarray) -> NumpyProto:
    original_dtype = obj.dtype
    if original_dtype not in SUPPORTED_DTYPES:
        raise NotImplementedError(f"{original_dtype} is not supported")

    if original_dtype in DTYPE_REFACTOR:
        # store as a signed int, the negative wrap around values convert back to the
        # same original unsigned values on the other side
        obj = obj.astype(DTYPE_REFACTOR[original_dtype])

    # Cloning seems to cause the worker to freeze if the array is larger than around
    # 800k in data and since we are serializing it immediately afterwards I don't
    # think its needed anyway
    # tensor = torch.from_numpy(obj).clone()
    tensor = torch.from_numpy(obj)
    tensor_bytes = tensor_serializer(tensor)
    dtype = original_dtype.name
    return NumpyProto(proto_data=tensor_bytes, dtype=dtype)


def protobuf_deserialize(proto: NumpyProto) -> np.ndarray:
    tensor = tensor_deserializer(proto.proto_data)
    array = tensor.to("cpu").detach().numpy().copy()
    str_dtype = proto.dtype
    original_dtype = np.dtype(str_dtype)
    obj = array.astype(original_dtype)
    return obj


def serialize_numpy_array(obj: np.ndarray) -> NumpyProto:
    if flags.APACHE_ARROW_TENSOR_SERDE:
        return arrow_serialize(obj)
    else:
        return protobuf_serialize(obj)


def deserialize_numpy_array(proto: NumpyProto) -> np.ndarray:
    if proto.HasField("arrow_data"):
        return arrow_deserialize(proto)
    else:
        return protobuf_deserialize(proto)


serializable(generate_wrapper=True)(
    wrapped_type=np.ndarray,
    import_path="numpy.ndarray",
    protobuf_scheme=NumpyProto,
    type_object2proto=serialize_numpy_array,
    type_proto2object=deserialize_numpy_array,
)
