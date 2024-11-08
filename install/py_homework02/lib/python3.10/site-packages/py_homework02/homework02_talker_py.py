"""  
    步骤：
        1.导包；
        2.初始化 ROS2 客户端；
        3.定义节点类；
            3-1.创建发布方；
            3-2.创建定时器；
            3-3.组织消息并发布。
        4.调用spin函数，并传入节点对象；
        5.释放资源。
"""
# 1.导包；
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


# 3.定义节点类；
class Publisher(Node):

    def __init__(self):
        super().__init__('publisher_py')
        # 3-1.创建发布方；
        self.publisher = self.create_publisher(String, 'topic', 10)
        # 3-2.创建定时器；
        timer_period = 0.5 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    # 3-3.组织消息并发布。
    def timer_callback(self):
        msg = String()
        msg.data = 'welcome to RM! %d' % self.i
        self.publisher.publish(msg)
        self.get_logger().info('发布的消息: "%s"' % msg.data)
        self.i += 1


def main():
    # 2.初始化 ROS2 客户端；
    rclpy.init()
    # 4.调用spin函数，并传入节点对象；
    publisher = Publisher()
    rclpy.spin(publisher)
    # 5.释放资源。
    rclpy.shutdown()


if __name__ == '__main__':
    main()