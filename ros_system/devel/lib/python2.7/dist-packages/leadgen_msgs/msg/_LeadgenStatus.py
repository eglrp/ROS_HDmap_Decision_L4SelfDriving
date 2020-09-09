# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from leadgen_msgs/LeadgenStatus.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import leadgen_msgs.msg
import std_msgs.msg

class LeadgenStatus(genpy.Message):
  _md5sum = "56b823ded06f347e2acd96e136b79bac"
  _type = "leadgen_msgs/LeadgenStatus"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# This message is to describe the overall vehicle status
# The message includes both vehicle positioning info and Chassis info

# Header
std_msgs/Header header

# vehicle position
geometry_msgs/Pose pose
geometry_msgs/Vector3 linear_velocity
geometry_msgs/Vector3 linear_acceleration
geometry_msgs/Vector3 angular_velocity

# vehicle chassis status
LeadgenChassis chassis_status

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: leadgen_msgs/LeadgenChassis
# This message is to describe the chassis status of the vehicle
# The information usually comes from CAN bus of the vehicle interface

# Header
std_msgs/Header header

# constant definitions
# auto_mode is bit-wise marker
# +-------------------+-------------------+
# | H3 | H2 | H1 | H0 | L3 | L2 | L1 | L0 |
# +-------------------+-------------------+
# |  Steering modes   |   speed modes     |
# +-------------------+-------------------+
uint8 AUTO_MODE_OFF = 0
uint8 AUTO_MODE_SYSTEM_ON = 1 # bit L0
uint8 AUTO_MODE_BRAKE_ON = 2 # bit L1
uint8 AUTO_MODE_THROTTLE_ON = 4  # bit L2
uint8 AUTO_MODE_SPEED_ON = 8  # bit L3

uint8 AUTO_MODE_STEER_ON = 16 # bit H0, 0x10
uint8 AUTO_MODE_STEER_POS = 32 # bit H1, 0x20
uint8 AUTO_MODE_STEER_VEL = 64 # bit H2, 0x40
uint8 AUTO_MODE_STEER_TOR = 128 # bit H3, 0x80

# vehicle current mode
uint8 auto_mode

# vehicle current longitude status
float32 speed # in signed [m/s]
float32 acceleration # in signed [m/s^2]
float32 throttle # in [percentage]
float32 brake # brake pressure [MPa]

# gear control is bit-wise marker
# +-------------------+-------------------+
# | H3 | H2 | H1 | H0 | L3 | L2 | L1 | L0 |
# +-------------------+-------------------+
uint8 GEAR_INVALID = 0
uint8 GEAR_P = 1
uint8 GEAR_R = 2
uint8 GEAR_N = 4
uint8 GEAR_D = 8

int8 gear # gear position

# vehicle current steering status
float32 steer_pos # in signed [percentage], positive to left

# other operational status(optional)
float32[] wheel_speed
float32 engine_rpm
float32 odometer
float32 fuel_level
"""
  __slots__ = ['header','pose','linear_velocity','linear_acceleration','angular_velocity','chassis_status']
  _slot_types = ['std_msgs/Header','geometry_msgs/Pose','geometry_msgs/Vector3','geometry_msgs/Vector3','geometry_msgs/Vector3','leadgen_msgs/LeadgenChassis']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,pose,linear_velocity,linear_acceleration,angular_velocity,chassis_status

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LeadgenStatus, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.linear_velocity is None:
        self.linear_velocity = geometry_msgs.msg.Vector3()
      if self.linear_acceleration is None:
        self.linear_acceleration = geometry_msgs.msg.Vector3()
      if self.angular_velocity is None:
        self.angular_velocity = geometry_msgs.msg.Vector3()
      if self.chassis_status is None:
        self.chassis_status = leadgen_msgs.msg.LeadgenChassis()
    else:
      self.header = std_msgs.msg.Header()
      self.pose = geometry_msgs.msg.Pose()
      self.linear_velocity = geometry_msgs.msg.Vector3()
      self.linear_acceleration = geometry_msgs.msg.Vector3()
      self.angular_velocity = geometry_msgs.msg.Vector3()
      self.chassis_status = leadgen_msgs.msg.LeadgenChassis()

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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_16d3I().pack(_x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w, _x.linear_velocity.x, _x.linear_velocity.y, _x.linear_velocity.z, _x.linear_acceleration.x, _x.linear_acceleration.y, _x.linear_acceleration.z, _x.angular_velocity.x, _x.angular_velocity.y, _x.angular_velocity.z, _x.chassis_status.header.seq, _x.chassis_status.header.stamp.secs, _x.chassis_status.header.stamp.nsecs))
      _x = self.chassis_status.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_B4fbf().pack(_x.chassis_status.auto_mode, _x.chassis_status.speed, _x.chassis_status.acceleration, _x.chassis_status.throttle, _x.chassis_status.brake, _x.chassis_status.gear, _x.chassis_status.steer_pos))
      length = len(self.chassis_status.wheel_speed)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.chassis_status.wheel_speed))
      _x = self
      buff.write(_get_struct_3f().pack(_x.chassis_status.engine_rpm, _x.chassis_status.odometer, _x.chassis_status.fuel_level))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.linear_velocity is None:
        self.linear_velocity = geometry_msgs.msg.Vector3()
      if self.linear_acceleration is None:
        self.linear_acceleration = geometry_msgs.msg.Vector3()
      if self.angular_velocity is None:
        self.angular_velocity = geometry_msgs.msg.Vector3()
      if self.chassis_status is None:
        self.chassis_status = leadgen_msgs.msg.LeadgenChassis()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 140
      (_x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w, _x.linear_velocity.x, _x.linear_velocity.y, _x.linear_velocity.z, _x.linear_acceleration.x, _x.linear_acceleration.y, _x.linear_acceleration.z, _x.angular_velocity.x, _x.angular_velocity.y, _x.angular_velocity.z, _x.chassis_status.header.seq, _x.chassis_status.header.stamp.secs, _x.chassis_status.header.stamp.nsecs,) = _get_struct_16d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.chassis_status.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.chassis_status.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 22
      (_x.chassis_status.auto_mode, _x.chassis_status.speed, _x.chassis_status.acceleration, _x.chassis_status.throttle, _x.chassis_status.brake, _x.chassis_status.gear, _x.chassis_status.steer_pos,) = _get_struct_B4fbf().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.chassis_status.wheel_speed = struct.unpack(pattern, str[start:end])
      _x = self
      start = end
      end += 12
      (_x.chassis_status.engine_rpm, _x.chassis_status.odometer, _x.chassis_status.fuel_level,) = _get_struct_3f().unpack(str[start:end])
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
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_16d3I().pack(_x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w, _x.linear_velocity.x, _x.linear_velocity.y, _x.linear_velocity.z, _x.linear_acceleration.x, _x.linear_acceleration.y, _x.linear_acceleration.z, _x.angular_velocity.x, _x.angular_velocity.y, _x.angular_velocity.z, _x.chassis_status.header.seq, _x.chassis_status.header.stamp.secs, _x.chassis_status.header.stamp.nsecs))
      _x = self.chassis_status.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_B4fbf().pack(_x.chassis_status.auto_mode, _x.chassis_status.speed, _x.chassis_status.acceleration, _x.chassis_status.throttle, _x.chassis_status.brake, _x.chassis_status.gear, _x.chassis_status.steer_pos))
      length = len(self.chassis_status.wheel_speed)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.chassis_status.wheel_speed.tostring())
      _x = self
      buff.write(_get_struct_3f().pack(_x.chassis_status.engine_rpm, _x.chassis_status.odometer, _x.chassis_status.fuel_level))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.pose is None:
        self.pose = geometry_msgs.msg.Pose()
      if self.linear_velocity is None:
        self.linear_velocity = geometry_msgs.msg.Vector3()
      if self.linear_acceleration is None:
        self.linear_acceleration = geometry_msgs.msg.Vector3()
      if self.angular_velocity is None:
        self.angular_velocity = geometry_msgs.msg.Vector3()
      if self.chassis_status is None:
        self.chassis_status = leadgen_msgs.msg.LeadgenChassis()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 140
      (_x.pose.position.x, _x.pose.position.y, _x.pose.position.z, _x.pose.orientation.x, _x.pose.orientation.y, _x.pose.orientation.z, _x.pose.orientation.w, _x.linear_velocity.x, _x.linear_velocity.y, _x.linear_velocity.z, _x.linear_acceleration.x, _x.linear_acceleration.y, _x.linear_acceleration.z, _x.angular_velocity.x, _x.angular_velocity.y, _x.angular_velocity.z, _x.chassis_status.header.seq, _x.chassis_status.header.stamp.secs, _x.chassis_status.header.stamp.nsecs,) = _get_struct_16d3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.chassis_status.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.chassis_status.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 22
      (_x.chassis_status.auto_mode, _x.chassis_status.speed, _x.chassis_status.acceleration, _x.chassis_status.throttle, _x.chassis_status.brake, _x.chassis_status.gear, _x.chassis_status.steer_pos,) = _get_struct_B4fbf().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.chassis_status.wheel_speed = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      _x = self
      start = end
      end += 12
      (_x.chassis_status.engine_rpm, _x.chassis_status.odometer, _x.chassis_status.fuel_level,) = _get_struct_3f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_16d3I = None
def _get_struct_16d3I():
    global _struct_16d3I
    if _struct_16d3I is None:
        _struct_16d3I = struct.Struct("<16d3I")
    return _struct_16d3I
_struct_B4fbf = None
def _get_struct_B4fbf():
    global _struct_B4fbf
    if _struct_B4fbf is None:
        _struct_B4fbf = struct.Struct("<B4fbf")
    return _struct_B4fbf