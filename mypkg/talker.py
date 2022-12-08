#!/usr/bin/python3
# SPDX-FileCopyrightText: 2022 Daiki Kurokawa　　　　
# SPDX-License-Identifier: BSD-3-Clause
import rclpy                     #ROS2のクライアントのためのライブラリ
from rclpy.node import Node      #ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16   #通信の型（16ビットの符号付き整数）

class Talker():
    def __init__(self):
        self.pub = node.create_publisher(Int16,"countup",10)
        self.n = 0

rclpy.init()
node = Node("talker")
talker = Talker()      #オブジェクトを作成（__init__が実行される。）
 
def cb():              #関数内のnやpubをtalkerのものに変更
    msg = Int16()
    msg.data = talker.n
    talker.pub.publish(msg)
    talker.n += 1
 
node.create_timer(0.5, cb)
rclpy.spin(node)
