"""
用Python的turtle模块绘制国旗
"""
import turtle


def draw_rectangle(x, y, width, height):
    # Python自定义函数
    """绘制矩形"""
    turtle.goto(x, y)
    # 从当前位置直接按直线画到指定位置
    turtle.pencolor('red')
    turtle.fillcolor('red')
    # 设定填充的颜色
    turtle.begin_fill()
    # 开始填充
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    # 圈填充的范围，可以不下笔
    turtle.end_fill()
    # 将上面的范围全部填充为填充颜色
    # 填充满闭合的范围，若部分不闭合则从绘制的起点开始到绘制的终点引线，填充满闭合所有范围


def draw_star(x, y, radius):
    """绘制五角星"""
    turtle.setpos(x, y)
    pos1 = turtle.pos()
    # 返回海龟当前位置
    turtle.circle(-radius, 72)
    # 以当前位置为端点，radius为半径，72为角度画部分圆
    pos2 = turtle.pos()
    turtle.circle(-radius, 72)
    pos3 = turtle.pos()
    turtle.circle(-radius, 72)
    pos4 = turtle.pos()
    turtle.circle(-radius, 72)
    pos5 = turtle.pos()
    turtle.color('yellow', 'yellow')
    turtle.begin_fill()
    turtle.goto(pos3)
    turtle.goto(pos1)
    turtle.goto(pos4)
    turtle.goto(pos2)
    turtle.goto(pos5)
    turtle.end_fill()
    # 通过circle确定五角星的五点，再顺次连接圈出五角星并填充


def main():
    """主程序"""
    turtle.speed(12)
    # 海龟速度
    turtle.penup()
    # 抬起笔，默认按下
    x, y = -270, -180
    # 画国旗主体
    width, height = 540, 360
    draw_rectangle(x, y, width, height)
    # 画大星星
    pice = 22
    center_x, center_y = x + 5 * pice, y + height - pice * 5
    turtle.goto(center_x, center_y)
    turtle.left(90)
    turtle.forward(pice * 3)
    turtle.right(90)
    draw_star(turtle.xcor(), turtle.ycor(), pice * 3)
    # 海龟的x，y坐标
    x_poses, y_poses = [10, 12, 12, 10], [2, 4, 7, 9]
    # 画小星星
    for x_pos, y_pos in zip(x_poses, y_poses):
        # 将x_poses和y_poses打包为元组的列表，长度以最短为准，[(10,2),(12,4).....]
        turtle.goto(x + x_pos * pice, y + height - y_pos * pice)
        turtle.left(turtle.towards(center_x, center_y) - turtle.heading())
        # 海龟初始朝向和海龟该点至目标点所成矢量的夹角
        # heading为海龟的朝向
        turtle.forward(pice)
        turtle.right(90)
        draw_star(turtle.xcor(), turtle.ycor(), pice)
    # 隐藏海龟
    turtle.ht()
    # 显示绘图窗口
    turtle.mainloop()


if __name__ == '__main__':
    main()
    # 只允许作为脚本直接执行，被调用时不执行
