from classes import Graph
from . import create_print_render_dot
from . import print_output_info

print("\nStart: Exercise 07 Task 26\n")
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

inputs = ["0:1,2;1:0,3;2:0,3,4;3:1,2,5;4:2,5;5:3,4;;",
          "0:1,8,15;1:0,2,3,15;2:1,4,6;3:1,5,7;4:2,5,6;5:3,4,7;6:2,4,8;7:3,5,8;8:0,6,7,9,10;9:8,11,13;10:8,12,14;" +
          "11:9,12,13;12:10,11,14;13:9,11,15;14:12,10,15;15:0,1,13,14;;",
          "a:b,c,d;b:a,e,i;c:a,g,h;d:a,f,j;e:b,f,g;f:d,e,h;g:e,c,j;h:c,f,i;i:b,h,j;j:g,d,i;;",
          "0:12,16,17,22,23,26,28,29,31,33,34,35,37,40,42,43,44,45,46,47,48,49;" +
          "1:2,3,4,5,6,7,10,12,15,17,20,23,34,35,36,37,39,40,41,45,46,48;" +
          "2:1,3,4,5,6,8,9,13,16,17,18,19,20,24,25,27,28,30,34,37,38,40,41,42,48;" +
          "3:1,2,4,5,6,7,8,12,13,14,15,16,17,21,22,26,27,29,30,31,32,34,37,42,44,45,46,48;" +
          "4:1,2,3,5,7,10,13,14,15,17,18,21,22,29,30,32,34,36,38,43,44,46,47,48;" +
          "5:1,2,3,4,7,10,14,18,22,24,25,27,28,29,33,36,38,40,42,46;" +
          "6:1,2,3,7,9,11,12,13,14,18,21,24,26,27,29,31,32,35,38,39,46,49;" +
          "7:1,3,4,5,6,8,11,13,15,17,20,21,22,23,24,25,26,33,43,48;" +
          "8:2,3,7,9,11,12,14,15,16,19,20,21,24,27,28,30,31,32,33,34,35,37,38,42,45,46,47,49;" +
          "9:2,6,8,12,14,16,17,18,20,21,22,27,28,32,34,37,38,39,43,47,48;" +
          "10:1,4,5,11,12,13,14,15,16,18,19,20,21,25,31,34,36,37,39,40,42,43,45,46,47,49;" +
          "11:6,7,8,10,12,13,14,15,16,17,21,22,26,28,29,32,34,36,42,44,45,47,48,49;" +
          "12:0,1,3,6,8,9,10,11,13,14,15,21,23,24,25,26,27,29,30,31,32,34,35,38,42,44,47,48;" +
          "13:2,3,4,6,7,10,11,12,15,17,18,20,21,22,26,27,28,32,34,37,38,39,40,43,45,46,47,48;" +
          "14:3,4,5,6,8,9,10,11,12,16,18,19,20,21,22,23,25,26,28,29,30,32,34,37,39,41,42,44,46,47;" +
          "15:1,3,4,7,8,10,11,12,13,16,19,20,22,23,24,26,27,28,30,32,33,34,36,38,40,41,42,46,48;" +
          "16:0,2,3,8,9,10,11,14,15,17,19,20,23,24,25,26,29,32,34,35,38,40,47,49;" +
          "17:0,1,2,3,4,7,9,11,13,16,19,20,21,23,28,30,35,37,39,41,42,43,44,45,46,47,48,49;" +
          "18:2,4,5,6,9,10,13,14,20,23,28,29,30,31,32,35,40,41,44,45,46,48;" +
          "19:2,8,10,14,15,16,17,25,26,27,31,33,39,41,42,43,44,45,48;" +
          "20:1,2,7,8,9,10,13,14,15,16,17,18,22,24,25,26,27,28,29,30,32,33,37,38,41,42,43,47,48;" +
          "21:3,4,6,7,8,9,10,11,12,13,14,17,23,25,27,28,29,33,34,35,37,40,41,43,44,45,47,48,49;" +
          "22:0,3,4,5,7,9,11,13,14,15,20,24,25,27,31,32,33,35,42,43,44,46,47,48,49;" +
          "23:0,1,7,12,14,15,16,17,18,21,24,30,34,36,38,39,40,41,44,45,46,49;" +
          "24:2,5,6,7,8,12,15,16,20,22,23,25,26,27,30,31,33,34,38,39,41,42,45,48,49;" +
          "25:2,5,7,10,12,14,16,19,20,21,22,24,26,30,31,32,38,39,40,42,43,44,45,47,48,49;" +
          "26:0,3,6,7,11,12,13,14,15,16,19,20,24,25,27,29,30,32,33,37,40,45,47,48;" +
          "27:2,3,5,6,8,9,12,13,15,19,20,21,22,24,26,28,31,33,34,36,38,40,41,45,47;" +
          "28:0,2,5,8,9,11,13,14,15,17,18,20,21,27,29,30,32,36,38,39,41;" +
          "29:0,3,4,5,6,11,12,14,16,18,20,21,26,28,30,33,34,36,40,42,43,49;" +
          "30:2,3,4,8,12,14,15,17,18,20,23,24,25,26,28,29,32,33,38,40,42,45,46,48,49;" +
          "31:0,3,6,8,10,12,18,19,22,24,25,27,32,33,34,36,37,40,41,43,44,47,49;" +
          "32:3,4,6,8,9,11,12,13,14,15,16,18,20,22,25,26,28,30,31,33,34,35,37,38,39,40,41,44,46,48,49;" +
          "33:0,5,7,8,15,19,20,21,22,24,26,27,29,30,31,32,34,37,38,39,41,42,43,45,47;" +
          "34:0,1,2,3,4,8,9,10,11,12,13,14,15,16,21,23,24,27,29,31,32,33,35,37,39,40,42,43,49;" +
          "35:0,1,6,8,12,16,17,18,21,22,32,34,36,38,39,43,44,47,48;" +
          "36:1,4,5,10,11,15,23,27,28,29,31,35,38,39,40,43,46,47;" +
          "37:0,1,2,3,8,9,10,13,14,17,20,21,26,31,32,33,34,39,41,42,46,47,48;" +
          "38:2,4,5,6,8,9,12,13,15,16,20,23,24,25,27,28,30,32,33,35,36,40,41,43,44,46,47,49;" +
          "39:1,6,9,10,13,14,17,19,23,24,25,28,32,33,34,35,36,37,40,44,45,47,48,49;" +
          "40:0,1,2,5,10,13,15,16,18,21,23,25,26,27,29,30,31,32,34,36,38,39,41,43,44,47,49;" +
          "41:1,2,14,15,17,18,19,20,21,23,24,27,28,31,32,33,37,38,40,44,47,48,49;" +
          "42:0,2,3,5,8,10,11,12,14,15,17,19,20,22,24,25,29,30,33,34,37,44,48,49;" +
          "43:0,4,7,9,10,13,17,19,20,21,22,25,29,31,33,34,35,36,38,40,44,45,47,49;" +
          "44:0,3,4,11,12,14,17,18,19,21,22,23,25,31,32,35,38,39,40,41,42,43,45,47,48;" +
          "45:0,1,3,8,10,11,13,17,18,19,21,23,24,25,26,27,30,33,39,43,44,47,48,49;" +
          "46:0,1,3,4,5,6,8,10,13,14,15,17,18,22,23,30,32,36,37,38,47,49;" +
          "47:0,4,8,9,10,11,12,13,14,16,17,20,21,22,25,26,27,31,33,35,36,37,38,39,40,41,43,44,45,46;" +
          "48:0,1,2,3,4,7,9,11,12,13,15,17,18,19,20,21,22,24,25,26,30,32,35,37,39,41,42,44,45;" +
          "49:0,6,8,10,11,16,17,21,22,23,24,25,29,30,31,32,34,38,39,40,41,42,43,45,46;;"]

results = []
for i, adjazenzlist in enumerate(inputs, start=1):
    graph = Graph(title="Exercise 07 Task 26 Graph 0{}".format(i),
                  filename="e07_t26_g0{}".format(i),
                  value=adjazenzlist)
    print("Colorize graph 0{} >>> Start <<<".format(i))
    r = graph.colorize()
    print("Colorize graph 0{} >>> End <<<".format(i))
    results.append(r)
    create_print_render_dot(graph)

for i, r in enumerate(results, start=1):
    print("\n__Graph_0{}___________: {}".format(i, "<not implemented yet>"))
    print(" - chromatische Zahl : {}".format("<not implemented yet>"))
    print(" - {}-Färbung\t: {}".format("<-1>", "<not implemented yet>"))

print_output_info(e="07", t="26")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print("End: Exercise 7 Task 26\n")
