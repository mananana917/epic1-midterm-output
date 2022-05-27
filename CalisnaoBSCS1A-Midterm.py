import turtle


wn = turtle.Screen()
wn.bgcolor('#F6F6F6')
wn.title("Cherry Mirra Calisnao BSCS 1A- Midterm Output")

turtle.speed(0)
space = 1
flag = 1000
m = turtle.Pen()
m.width(3)
m.speed(1000)


# Making a patten
while flag:

    m.forward(space)
    m.pencolor("#ee4035")
    m.left(130)
    m.left(2)
    space += 1
    flag -= 1
    

    m.forward(space)
    m.pencolor("#0392cf")
    m.left(130)
    m.left(1)
    space += 1
    flag -= 1

   
    m.forward(space)
    m.pencolor("#f37736")
    m.left(130)
    m.left(2)
    space += 1.5
    flag -= 1

  
    m.forward(space)
    m.pencolor("#fdf498")
    m.left(130)
    m.left(1)
    space += 1.5
    flag -= 1

   
    m.forward(space)
    m.pencolor("#7bc043")
    m.left(130)
    m.left(2)
    space += 1.5
    flag -= 1


wn.exitonclick()
m.done()