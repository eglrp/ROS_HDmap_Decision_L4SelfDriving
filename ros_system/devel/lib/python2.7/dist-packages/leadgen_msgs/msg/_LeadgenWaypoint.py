# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from leadgen_msgs/LeadgenWaypoint.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import genpy

class LeadgenWaypoint(genpy.Message):
  _md5sum = "38a50bfbdbab44a271e46dddaf38da0a"
  _type = "leadgen_msgs/LeadgenWaypoint"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# This message is to describe a WAYPOINT in the target trajectory

# header
# std_msgs/Header header

# 3D position
geometry_msgs/Point point

# trace info
float64 theta # the heading of the trace at this point
float64 kappa # the curvature of the trace at this point

# SL info
float64 station
float64 lateral

# speed info
float32 speed # in [m/s]
float32 accel # in [m/s^2],(optional)

time time_arrival # the expected arrival time of this point



================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
"""
  __slots__ = ['point','theta','kappa','station','lateral','speed','accel','time_arrival']
  _slot_types = ['geometry_msgs/Point','float64','float64','float64','float64','float32','float32','time']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       point,theta,kappa,station,lateral,speed,accel,time_arrival

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LeadgenWaypoint, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.point is None:
        self.point = geometry_msgs.msg.Point()
      if self.theta is None:
        self.theta = 0.
      if self.kappa is None:
        self.kappa = 0.
      if self.station is None:
        self.station = 0.
      if self.lateral is None:
        self.lateral = 0.
      if self.speed is None:
        self.speed = 0.
      if self.accel is None:
        self.accel = 0.
      if self.time_arrival is None:
        self.time_arrival = genpy.Time()
    else:
      self.point = geometry_msgs.msg.Point()
      self.theta = 0.
      self.kappa = 0.
      self.station = 0.
      self.lateral = 0.
      self.speed = 0.
      self.accel = 0.
      self.time_arrival = genpy.Time()

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
      buff.write(_get_struct_7d2f2I().pack(_x.point.x, _x.point.y, _x.point.z, _x.theta, _x.kappa, _x.station, _x.lateral, _x.speed, _x.accel, _x.time_arrival.secs, _x.time_arrival.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.point is None:
        self.point = geometry_msgs.msg.Point()
      if self.time_arrival is None:
        self.time_arrival = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 72
      (_x.point.x, _x.point.y, _x.point.z, _x.theta, _x.kappa, _x.station, _x.lateral, _x.speed, _x.accel, _x.time_arrival.secs, _x.time_arrival.nsecs,) = _get_struct_7d2f2I().unpack(str[start:end])
      self.time_arrival.canon()
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
      buff.write(_get_struct_7d2f2I().pack(_x.point.x, _x.point.y, _x.point.z, _x.theta, _x.kappa, _x.station, _x.lateral, _x.speed, _x.accel, _x.time_arrival.secs, _x.time_arrival.nsecs))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.point is None:
        self.point = geometry_msgs.msg.Point()
      if self.time_arrival is None:
        self.time_arrival = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 72
      (_x.point.x, _x.point.y, _x.point.z, _x.theta, _x.kappa, _x.station, _x.lateral, _x.speed, _x.accel, _x.time_arrival.secs, _x.time_arrival.nsecs,) = _get_struct_7d2f2I().unpack(str[start:end])
      self.time_arrival.canon()
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_7d2f2I = None
def _get_struct_7d2f2I():
    global _struct_7d2f2I
    if _struct_7d2f2I is None:
        _struct_7d2f2I = struct.Struct("<7d2f2I")
    return _struct_7d2f2I
