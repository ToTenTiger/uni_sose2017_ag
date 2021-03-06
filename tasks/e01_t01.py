from tasks import *


print("Start: Exercise 01 Task 01")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

graph = DiGraph(title="Exercise 01 Task 01 Graph 01",
                filename="e01_t01_g01",)
graph.read_input(value="1:2,3,5,10;" +
                       "2:3,4,7,8;" +
                       "3:5;" +
                       "4:7,10;" +
                       "5:6,8,10;" +
                       "6:7,8,9;" +
                       "7:9,11;" +
                       "8:10;" +
                       "9:10,11;" +
                       "10:11;" +
                       "11:;;")

dot = create_print_render_dot(graph)

print("bnb(2,4) ? %s" % graph.bnb("2", "4"))
print("bnb(4,2) ? %s" % graph.bnb("4", "2"))

print("ausGrad(2) ? %s" % graph.aus_grad("2"))
print("ausGrad(8) ? %s" % graph.aus_grad("8"))
print("einGrad(7) ? %s" % graph.ein_grad("7"))
print("einGrad(2) ? %s" % graph.ein_grad("2"))
print("grad(10) ? %s" % graph.grad("10"))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("End: Exercise 01 Task 01")
