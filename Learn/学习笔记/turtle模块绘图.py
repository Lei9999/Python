"""
turtle
简单的绘图工具
提供一个小海龟，可以把它理解为一个机器人，只能听得懂有限的命令

绘图窗口的原点(0,0)在正中间，默认海龟的方向是右侧

运动命令：
forward(d)      向前移动d长度
backward(d)     向后移动d长度
right(d)        向右转动多少度
left(d)         向左转动多少度
goto(x, y)      移动到x,y的位置
speed(speed)    笔画绘制的速度[0, 10]

笔画控制命令：
up()            笔画抬起，在移动的时候不会绘图
down()          笔画落下，移动会绘图
setheading(d)   改变海龟的朝向(度)
pensize()       笔画的宽度
pencolor(colorstr)  笔画的颜色
reset()         恢复所有设置，清空窗口，重置turtle状态
clear()         清空窗口，不重置turtle状态
circle(r, e)    绘制一个圆形，r为半径，e为次数（省略是圆形）
# circle(50, steps=5)  # 五边形

# 填充
begin_fill()
fillcolor(colorstr)
end_fill()

undo()          撤销上一次动作
hideturtle()    隐藏海龟
showturtle()    显示海龟
# screensize(x, y)    屏幕大小？

其他命令：
done()  程序继续进行

"""

# 导入turtle库
import turtle
turtle.speed(1)
turtle.forward(100)
turtle.right(45)
turtle.forward(100)
turtle.goto(-100, -200)
turtle.done()
