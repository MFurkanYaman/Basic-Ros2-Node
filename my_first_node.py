#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self):
       super().__init__ ("python_test")

       self.counter = 0
       self.get_logger().info("Merhaba Ros2")
       self.create_timer(0.5,self.timer_callback)

    def timer_callback(self):
        self.counter+=1
        self.get_logger().info(f"Hello {self.counter}")


def main(args=None):
    rclpy.init(args=args) #ros2'nin haberleşmesini başlatır.

    node=MyNode()
    
    """
    node=Node("python_test")
    node.get_logger().info("Merhaba Ros2")
    """

    rclpy.spin(node) #nodeun sürekli çalışmasını sağlar.

    rclpy.shutdown() #haberleşmeyi sonlandırır ve yazdığın kodu bellekten siler 


if __name__== "__main__":
    main()

