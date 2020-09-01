// Generated by gencpp from file ytthdmap_msgs/HdmapYtt.msg
// DO NOT EDIT!


#ifndef YTTHDMAP_MSGS_MESSAGE_HDMAPYTT_H
#define YTTHDMAP_MSGS_MESSAGE_HDMAPYTT_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <ytthdmap_msgs/S_LANEINFO.h>
#include <ytthdmap_msgs/S_STATIONLOCATION.h>
#include <ytthdmap_msgs/S_STOPLINE.h>

namespace ytthdmap_msgs
{
template <class ContainerAllocator>
struct HdmapYtt_
{
  typedef HdmapYtt_<ContainerAllocator> Type;

  HdmapYtt_()
    : header()
    , time(0)
    , isvalidlane(0)
    , curlane(0)
    , laneinfo()
    , speedlim(0.0)
    , stationlocation()
    , stopline()
    , istunnel(false)
    , nextlaneCH(0)
    , traffic(0)  {
    }
  HdmapYtt_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , time(0)
    , isvalidlane(0)
    , curlane(0)
    , laneinfo(_alloc)
    , speedlim(0.0)
    , stationlocation(_alloc)
    , stopline(_alloc)
    , istunnel(false)
    , nextlaneCH(0)
    , traffic(0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int16_t _time_type;
  _time_type time;

   typedef int16_t _isvalidlane_type;
  _isvalidlane_type isvalidlane;

   typedef int16_t _curlane_type;
  _curlane_type curlane;

   typedef  ::ytthdmap_msgs::S_LANEINFO_<ContainerAllocator>  _laneinfo_type;
  _laneinfo_type laneinfo;

   typedef float _speedlim_type;
  _speedlim_type speedlim;

   typedef  ::ytthdmap_msgs::S_STATIONLOCATION_<ContainerAllocator>  _stationlocation_type;
  _stationlocation_type stationlocation;

   typedef  ::ytthdmap_msgs::S_STOPLINE_<ContainerAllocator>  _stopline_type;
  _stopline_type stopline;

   typedef uint8_t _istunnel_type;
  _istunnel_type istunnel;

   typedef int16_t _nextlaneCH_type;
  _nextlaneCH_type nextlaneCH;

   typedef int16_t _traffic_type;
  _traffic_type traffic;





  typedef boost::shared_ptr< ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator> const> ConstPtr;

}; // struct HdmapYtt_

typedef ::ytthdmap_msgs::HdmapYtt_<std::allocator<void> > HdmapYtt;

typedef boost::shared_ptr< ::ytthdmap_msgs::HdmapYtt > HdmapYttPtr;
typedef boost::shared_ptr< ::ytthdmap_msgs::HdmapYtt const> HdmapYttConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace ytthdmap_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'ytthdmap_msgs': ['/home/xiaotongfeng/ros_test/src/ytthdmap/ytthdmap_msgs/./']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator> >
{
  static const char* value()
  {
    return "06136882eb0000675a95c6a59756dfc6";
  }

  static const char* value(const ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x06136882eb000067ULL;
  static const uint64_t static_value2 = 0x5a95c6a59756dfc6ULL;
};

template<class ContainerAllocator>
struct DataType< ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator> >
{
  static const char* value()
  {
    return "ytthdmap_msgs/HdmapYtt";
  }

  static const char* value(const ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator> >
{
  static const char* value()
  {
    return "std_msgs/Header header\n\
int16 time\n\
int16 isvalidlane\n\
int16 curlane\n\
S_LANEINFO laneinfo \n\
float32 speedlim\n\
S_STATIONLOCATION stationlocation\n\
S_STOPLINE stopline\n\
bool istunnel\n\
int16 nextlaneCH\n\
int16 traffic\n\
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
\n\
================================================================================\n\
MSG: ytthdmap_msgs/S_LANEINFO\n\
S_LINE centerline\n\
S_LINE leftboundry\n\
S_LINE rightboundry\n\
float64 width\n\
bool IsPartofRouting\n\
int16 type\n\
int16 direction\n\
int16 id\n\
float64 length\n\
================================================================================\n\
MSG: ytthdmap_msgs/S_LINE\n\
int16 type\n\
int16 linetype\n\
S_POINT[100] point\n\
int16 pointnum\n\
================================================================================\n\
MSG: ytthdmap_msgs/S_POINT\n\
float64 x\n\
float64 y\n\
float64 z\n\
================================================================================\n\
MSG: ytthdmap_msgs/S_STATIONLOCATION\n\
float64 x\n\
float64 y\n\
float64 z\n\
================================================================================\n\
MSG: ytthdmap_msgs/S_STOPLINE\n\
int16 offset\n\
int16 latOffset\n\
int16 type\n\
int16 validnum\n\
S_POINT[100] point\n\
";
  }

  static const char* value(const ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.time);
      stream.next(m.isvalidlane);
      stream.next(m.curlane);
      stream.next(m.laneinfo);
      stream.next(m.speedlim);
      stream.next(m.stationlocation);
      stream.next(m.stopline);
      stream.next(m.istunnel);
      stream.next(m.nextlaneCH);
      stream.next(m.traffic);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct HdmapYtt_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::ytthdmap_msgs::HdmapYtt_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "time: ";
    Printer<int16_t>::stream(s, indent + "  ", v.time);
    s << indent << "isvalidlane: ";
    Printer<int16_t>::stream(s, indent + "  ", v.isvalidlane);
    s << indent << "curlane: ";
    Printer<int16_t>::stream(s, indent + "  ", v.curlane);
    s << indent << "laneinfo: ";
    s << std::endl;
    Printer< ::ytthdmap_msgs::S_LANEINFO_<ContainerAllocator> >::stream(s, indent + "  ", v.laneinfo);
    s << indent << "speedlim: ";
    Printer<float>::stream(s, indent + "  ", v.speedlim);
    s << indent << "stationlocation: ";
    s << std::endl;
    Printer< ::ytthdmap_msgs::S_STATIONLOCATION_<ContainerAllocator> >::stream(s, indent + "  ", v.stationlocation);
    s << indent << "stopline: ";
    s << std::endl;
    Printer< ::ytthdmap_msgs::S_STOPLINE_<ContainerAllocator> >::stream(s, indent + "  ", v.stopline);
    s << indent << "istunnel: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.istunnel);
    s << indent << "nextlaneCH: ";
    Printer<int16_t>::stream(s, indent + "  ", v.nextlaneCH);
    s << indent << "traffic: ";
    Printer<int16_t>::stream(s, indent + "  ", v.traffic);
  }
};

} // namespace message_operations
} // namespace ros

#endif // YTTHDMAP_MSGS_MESSAGE_HDMAPYTT_H