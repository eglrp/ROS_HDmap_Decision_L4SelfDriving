# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from planning_msgs/ObstacleIn.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class ObstacleIn(genpy.Message):
  _md5sum = "839da740b46a1232ec0479df07f94f66"
  _type = "planning_msgs/ObstacleIn"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """int8 id
float32 s
float32 l
float32 vs
float32 as
float32 vl
float32 al
int8 lane_no
float32 time_cost
float32 des_cost
float32 decision_cost
int8 decision_tag
"""
  __slots__ = ['id','s','l','vs','as_','vl','al','lane_no','time_cost','des_cost','decision_cost','decision_tag']
  _slot_types = ['int8','float32','float32','float32','float32','float32','float32','int8','float32','float32','float32','int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       id,s,l,vs,as_,vl,al,lane_no,time_cost,des_cost,decision_cost,decision_tag

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ObstacleIn, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.id is None:
        self.id = 0
      if self.s is None:
        self.s = 0.
      if self.l is None:
        self.l = 0.
      if self.vs is None:
        self.vs = 0.
      if self.as_ is None:
        self.as_ = 0.
      if self.vl is None:
        self.vl = 0.
      if self.al is None:
        self.al = 0.
      if self.lane_no is None:
        self.lane_no = 0
      if self.time_cost is None:
        self.time_cost = 0.
      if self.des_cost is None:
        self.des_cost = 0.
      if self.decision_cost is None:
        self.decision_cost = 0.
      if self.decision_tag is None:
        self.decision_tag = 0
    else:
      self.id = 0
      self.s = 0.
      self.l = 0.
      self.vs = 0.
      self.as_ = 0.
      self.vl = 0.
      self.al = 0.
      self.lane_no = 0
      self.time_cost = 0.
      self.des_cost = 0.
      self.decision_cost = 0.
      self.decision_tag = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_b6fb3fb().pack(_x.id, _x.s, _x.l, _x.vs, _x.as_, _x.vl, _x.al, _x.lane_no, _x.time_cost, _x.des_cost, _x.decision_cost, _x.decision_tag))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 39
      (_x.id, _x.s, _x.l, _x.vs, _x.as_, _x.vl, _x.al, _x.lane_no, _x.time_cost, _x.des_cost, _x.decision_cost, _x.decision_tag,) = _get_struct_b6fb3fb().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_b6fb3fb().pack(_x.id, _x.s, _x.l, _x.vs, _x.as_, _x.vl, _x.al, _x.lane_no, _x.time_cost, _x.des_cost, _x.decision_cost, _x.decision_tag))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 39
      (_x.id, _x.s, _x.l, _x.vs, _x.as_, _x.vl, _x.al, _x.lane_no, _x.time_cost, _x.des_cost, _x.decision_cost, _x.decision_tag,) = _get_struct_b6fb3fb().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_b6fb3fb = None
def _get_struct_b6fb3fb():
    global _struct_b6fb3fb
    if _struct_b6fb3fb is None:
        _struct_b6fb3fb = struct.Struct("<b6fb3fb")
    return _struct_b6fb3fb
