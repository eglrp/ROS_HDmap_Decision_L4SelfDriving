# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from planning_msgs/DecisionDebug.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import planning_msgs.msg

class DecisionDebug(genpy.Message):
  _md5sum = "da2ec6dc8e24bc6e33c0fa04fe1dfa3b"
  _type = "planning_msgs/DecisionDebug"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """  ObstacleIn[50] obstacle
  int8 lanechange_id
  int8 lane_id
  float32[3] ego_cost
  int8[3] onlane_obs_num
  int8 lanechange_process

================================================================================
MSG: planning_msgs/ObstacleIn
int8 id
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
  __slots__ = ['obstacle','lanechange_id','lane_id','ego_cost','onlane_obs_num','lanechange_process']
  _slot_types = ['planning_msgs/ObstacleIn[50]','int8','int8','float32[3]','int8[3]','int8']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       obstacle,lanechange_id,lane_id,ego_cost,onlane_obs_num,lanechange_process

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(DecisionDebug, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.obstacle is None:
        self.obstacle = [planning_msgs.msg.ObstacleIn() for _ in range(50)]
      if self.lanechange_id is None:
        self.lanechange_id = 0
      if self.lane_id is None:
        self.lane_id = 0
      if self.ego_cost is None:
        self.ego_cost = [0.] * 3
      if self.onlane_obs_num is None:
        self.onlane_obs_num = [0] * 3
      if self.lanechange_process is None:
        self.lanechange_process = 0
    else:
      self.obstacle = [planning_msgs.msg.ObstacleIn() for _ in range(50)]
      self.lanechange_id = 0
      self.lane_id = 0
      self.ego_cost = [0.] * 3
      self.onlane_obs_num = [0] * 3
      self.lanechange_process = 0

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
      for val1 in self.obstacle:
        _x = val1
        buff.write(_get_struct_b6fb3fb().pack(_x.id, _x.s, _x.l, _x.vs, _x.as_, _x.vl, _x.al, _x.lane_no, _x.time_cost, _x.des_cost, _x.decision_cost, _x.decision_tag))
      _x = self
      buff.write(_get_struct_2b().pack(_x.lanechange_id, _x.lane_id))
      buff.write(_get_struct_3f().pack(*self.ego_cost))
      buff.write(_get_struct_3b().pack(*self.onlane_obs_num))
      buff.write(_get_struct_b().pack(self.lanechange_process))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.obstacle is None:
        self.obstacle = None
      end = 0
      self.obstacle = []
      for i in range(0, 50):
        val1 = planning_msgs.msg.ObstacleIn()
        _x = val1
        start = end
        end += 39
        (_x.id, _x.s, _x.l, _x.vs, _x.as_, _x.vl, _x.al, _x.lane_no, _x.time_cost, _x.des_cost, _x.decision_cost, _x.decision_tag,) = _get_struct_b6fb3fb().unpack(str[start:end])
        self.obstacle.append(val1)
      _x = self
      start = end
      end += 2
      (_x.lanechange_id, _x.lane_id,) = _get_struct_2b().unpack(str[start:end])
      start = end
      end += 12
      self.ego_cost = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 3
      self.onlane_obs_num = _get_struct_3b().unpack(str[start:end])
      start = end
      end += 1
      (self.lanechange_process,) = _get_struct_b().unpack(str[start:end])
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
      for val1 in self.obstacle:
        _x = val1
        buff.write(_get_struct_b6fb3fb().pack(_x.id, _x.s, _x.l, _x.vs, _x.as_, _x.vl, _x.al, _x.lane_no, _x.time_cost, _x.des_cost, _x.decision_cost, _x.decision_tag))
      _x = self
      buff.write(_get_struct_2b().pack(_x.lanechange_id, _x.lane_id))
      buff.write(self.ego_cost.tostring())
      buff.write(self.onlane_obs_num.tostring())
      buff.write(_get_struct_b().pack(self.lanechange_process))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.obstacle is None:
        self.obstacle = None
      end = 0
      self.obstacle = []
      for i in range(0, 50):
        val1 = planning_msgs.msg.ObstacleIn()
        _x = val1
        start = end
        end += 39
        (_x.id, _x.s, _x.l, _x.vs, _x.as_, _x.vl, _x.al, _x.lane_no, _x.time_cost, _x.des_cost, _x.decision_cost, _x.decision_tag,) = _get_struct_b6fb3fb().unpack(str[start:end])
        self.obstacle.append(val1)
      _x = self
      start = end
      end += 2
      (_x.lanechange_id, _x.lane_id,) = _get_struct_2b().unpack(str[start:end])
      start = end
      end += 12
      self.ego_cost = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 3
      self.onlane_obs_num = numpy.frombuffer(str[start:end], dtype=numpy.int8, count=3)
      start = end
      end += 1
      (self.lanechange_process,) = _get_struct_b().unpack(str[start:end])
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
_struct_3b = None
def _get_struct_3b():
    global _struct_3b
    if _struct_3b is None:
        _struct_3b = struct.Struct("<3b")
    return _struct_3b
_struct_b = None
def _get_struct_b():
    global _struct_b
    if _struct_b is None:
        _struct_b = struct.Struct("<b")
    return _struct_b
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_2b = None
def _get_struct_2b():
    global _struct_2b
    if _struct_2b is None:
        _struct_2b = struct.Struct("<2b")
    return _struct_2b
