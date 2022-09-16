from turtle import*


#we want to paint a house

#step 1: draw a square
speed(20)
width(7)
color("purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square

#drawing a door 

forward(70) 
color("yellow")
begin_fill()
left(90)   
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill() #end of door
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)    
left(120)
forward(200)
end_fill()
#drawing a windows
left(30)
penup()
goto(10,135)
pendown()
color("brown")
begin_fill()
left(90)
width(4)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
left(90)
penup()
goto(140,135)
pendown()
begin_fill()
forward(50)
left(90)
forward(50) 
left(90)
forward(50)
left(90)
forward(50)
end_fill()

exitonclick()