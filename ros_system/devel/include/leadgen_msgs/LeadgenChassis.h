// Generated by gencpp from file leadgen_msgs/LeadgenChassis.msg
// DO NOT EDIT!


#ifndef LEADGEN_MSGS_MESSAGE_LEADGENCHASSIS_H
#define LEADGEN_MSGS_MESSAGE_LEADGENCHASSIS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace leadgen_msgs
{
template <class ContainerAllocator>
struct LeadgenChassis_
{
  typedef LeadgenChassis_<ContainerAllocator> Type;

  LeadgenChassis_()
    : header()
    , auto_mode(0)
    , speed(0.0)
    , acceleration(0.0)
    , throttle(0.0)
    , brake(0.0)
    , gear(0)
    , steer_pos(0.0)
    , wheel_speed()
    , engine_rpm(0.0)
    , odometer(0.0)
    , fuel_level(0.0)  {
    }
  LeadgenChassis_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , auto_mode(0)
    , speed(0.0)
    , acceleration(0.0)
    , throttle(0.0)
    , brake(0.0)
    , gear(0)
    , steer_pos(0.0)
    , wheel_speed(_alloc)
    , engine_rpm(0.0)
    , odometer(0.0)
    , fuel_level(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef uint8_t _auto_mode_type;
  _auto_mode_type auto_mode;

   typedef float _speed_type;
  _speed_type speed;

   typedef float _acceleration_type;
  _acceleration_type acceleration;

   typedef float _throttle_type;
  _throttle_type throttle;

   typedef float _brake_type;
  _brake_type brake;

   typedef int8_t _gear_type;
  _gear_type gear;

   typedef float _steer_pos_type;
  _steer_pos_type steer_pos;

   typedef std::vector<float, typename ContainerAllocator::template rebind<float>::other >  _wheel_speed_type;
  _wheel_speed_type wheel_speed;

   typedef float _engine_rpm_type;
  _engine_rpm_type engine_rpm;

   typedef float _odometer_type;
  _odometer_type odometer;

   typedef float _fuel_level_type;
  _fuel_level_type fuel_level;



  enum {
    AUTO_MODE_OFF = 0u,
    AUTO_MODE_SYSTEM_ON = 1u,
    AUTO_MODE_BRAKE_ON = 2u,
    AUTO_MODE_THROTTLE_ON = 4u,
    AUTO_MODE_SPEED_ON = 8u,
    AUTO_MODE_STEER_ON = 16u,
    AUTO_MODE_STEER_POS = 32u,
    AUTO_MODE_STEER_VEL = 64u,
    AUTO_MODE_STEER_TOR = 128u,
    GEAR_INVALID = 0u,
    GEAR_P = 1u,
    GEAR_R = 2u,
    GEAR_N = 4u,
    GEAR_D = 8u,
  };


  typedef boost::shared_ptr< ::leadgen_msgs::LeadgenChassis_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::leadgen_msgs::LeadgenChassis_<ContainerAllocator> const> ConstPtr;

}; // struct LeadgenChassis_

typedef ::leadgen_msgs::LeadgenChassis_<std::allocator<void> > LeadgenChassis;

typedef boost::shared_ptr< ::leadgen_msgs::LeadgenChassis > LeadgenChassisPtr;
typedef boost::shared_ptr< ::leadgen_msgs::LeadgenChassis const> LeadgenChassisConstPtr;

// constants requiring out of line definition

   

   

   

   

   

   

   

   

   

   

   

   

   

   



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::leadgen_msgs::LeadgenChassis_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::leadgen_msgs::LeadgenChassis_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace leadgen_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'leadgen_msgs': ['/home/xiaotongfeng/Desktop/ROS_HDmap_Decision_L4/ros_system/src/planning/leadgen_msgs/./'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::leadgen_msgs::LeadgenChassis_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::leadgen_msgs::LeadgenChassis_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::leadgen_msgs::LeadgenChassis_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::leadgen_msgs::LeadgenChassis_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::leadgen_msgs::LeadgenChassis_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::leadgen_msgs::LeadgenChassis_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::leadgen_msgs::LeadgenChassis_<ContainerAllocator> >
{
  static const char* value()
  {
    return "6e7786948abd184365b7821561378998";
  }

  static const char* value(const ::leadgen_msgs::LeadgenChassis_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x6e7786948abd1843ULL;
  static const uint64_t static_value2 = 0x65b7821561378998ULL;
};

template<class ContainerAllocator>
struct DataType< ::leadgen_msgs::LeadgenChassis_<ContainerAllocator> >
{
  static const char* value()
  {
    return "leadgen_msgs/LeadgenChassis";
  }

  static const char* value(const ::leadgen_msgs::LeadgenChassis_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::leadgen_msgs::LeadgenChassis_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# This message is to describe the chassis status of the vehicle\n\
# The information usually comes from CAN bus of the vehicle interface\n\
\n\
# Header\n\
std_msgs/Header header\n\
\n\
# constant definitions\n\
# auto_mode is bit-wise marker\n\
# +-------------------+-------------------+\n\
# | H3 | H2 | H1 | H0 | L3 | L2 | L1 | L0 |\n\
# +-------------------+-------------------+\n\
# |  Steering modes   |   speed modes     |\n\
# +-------------------+-------------------+\n\
uint8 AUTO_MODE_OFF = 0\n\
uint8 AUTO_MODE_SYSTEM_ON = 1 # bit L0\n\
uint8 AUTO_MODE_BRAKE_ON = 2 # bit L1\n\
uint8 AUTO_MODE_THROTTLE_ON = 4  # bit L2\n\
uint8 AUTO_MODE_SPEED_ON = 8  # bit L3\n\
\n\
uint8 AUTO_MODE_STEER_ON = 16 # bit H0, 0x10\n\
uint8 AUTO_MODE_STEER_POS = 32 # bit H1, 0x20\n\
uint8 AUTO_MODE_STEER_VEL = 64 # bit H2, 0x40\n\
uint8 AUTO_MODE_STEER_TOR = 128 # bit H3, 0x80\n\
\n\
# vehicle current mode\n\
uint8 auto_mode\n\
\n\
# vehicle current longitude status\n\
float32 speed # in signed [m/s]\n\
float32 acceleration # in signed [m/s^2]\n\
float32 throttle # in [percentage]\n\
float32 brake # brake pressure [MPa]\n\
\n\
# gear control is bit-wise marker\n\
# +-------------------+-------------------+\n\
# | H3 | H2 | H1 | H0 | L3 | L2 | L1 | L0 |\n\
# +-------------------+-------------------+\n\
uint8 GEAR_INVALID = 0\n\
uint8 GEAR_P = 1\n\
uint8 GEAR_R = 2\n\
uint8 GEAR_N = 4\n\
uint8 GEAR_D = 8\n\
\n\
int8 gear # gear position\n\
\n\
# vehicle current steering status\n\
float32 steer_pos # in signed [percentage], positive to left\n\
\n\
# other operational status(optional)\n\
float32[] wheel_speed\n\
float32 engine_rpm\n\
float32 odometer\n\
float32 fuel_level\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
";
  }

  static const char* value(const ::leadgen_msgs::LeadgenChassis_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::leadgen_msgs::LeadgenChassis_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.auto_mode);
      stream.next(m.speed);
      stream.next(m.acceleration);
      stream.next(m.throttle);
      stream.next(m.brake);
      stream.next(m.gear);
      stream.next(m.steer_pos);
      stream.next(m.wheel_speed);
      stream.next(m.engine_rpm);
      stream.next(m.odometer);
      stream.next(m.fuel_level);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct LeadgenChassis_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::leadgen_msgs::LeadgenChassis_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::leadgen_msgs::LeadgenChassis_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "auto_mode: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.auto_mode);
    s << indent << "speed: ";
    Printer<float>::stream(s, indent + "  ", v.speed);
    s << indent << "acceleration: ";
    Printer<float>::stream(s, indent + "  ", v.acceleration);
    s << indent << "throttle: ";
    Printer<float>::stream(s, indent + "  ", v.throttle);
    s << indent << "brake: ";
    Printer<float>::stream(s, indent + "  ", v.brake);
    s << indent << "gear: ";
    Printer<int8_t>::stream(s, indent + "  ", v.gear);
    s << indent << "steer_pos: ";
    Printer<float>::stream(s, indent + "  ", v.steer_pos);
    s << indent << "wheel_speed[]" << std::endl;
    for (size_t i = 0; i < v.wheel_speed.size(); ++i)
    {
      s << indent << "  wheel_speed[" << i << "]: ";
      Printer<float>::stream(s, indent + "  ", v.wheel_speed[i]);
    }
    s << indent << "engine_rpm: ";
    Printer<float>::stream(s, indent + "  ", v.engine_rpm);
    s << indent << "odometer: ";
    Printer<float>::stream(s, indent + "  ", v.odometer);
    s << indent << "fuel_level: ";
    Printer<float>::stream(s, indent + "  ", v.fuel_level);
  }
};

} // namespace message_operations
} // namespace ros

#endif // LEADGEN_MSGS_MESSAGE_LEADGENCHASSIS_H
