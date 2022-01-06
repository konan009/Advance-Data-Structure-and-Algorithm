VALUES_CONSTANT = "values"
PREVIOUS_NODE_CONSTANT = "previous_vertex"


START_NODE = "A"
END_NODE = "F"


# GRAPH IS 1A
graph = {
  "A": {
    "B" : 5,
    "C" : 2 
  },
  "B": {
    "E" : 4 ,
    "D": 2 ,
  },
  "C" : {
    "B" : 8,
    "D" :  7  
  },
  "E" : {
    "F" :  3 ,
    "D" :  6  
  },
  "D" : {
    "F" :  1  
  },
  "F" : {
  }
}

# GRAPH 1B
# graph = {
#   "A": {
#     "B" : 10
#   },
#   "B": {
#     "C" : 20 ,
#   },
#   "C" : {
#     "D" :  1 ,
#     "E" :  30
#   },
#   "D" : {
#     "B" :  1,
#   },
#   "E" : {
#   }
# }

# GENERATES SCORE TABLE FOR DIJKSTRA ALGORITHM
def generate_score_table():
  SCORE_TABLE = {}
  QUEUE   = [START_NODE]
  SCORE_TABLE[START_NODE] = { VALUES_CONSTANT : 0 }
  VISITED = []
  NEXT_FIRST_NEIGHBOR= list(graph[QUEUE[0]].keys())[0]
  shortest_path_length = 0
  shortest_path_found_bool = False
  # IMPLEMENT BFS
  while len(QUEUE) > 0:
    # TRAVERSE THE EDGES
    for node in graph[QUEUE[0]].keys():
      # IF THE !EXIST IN THE TABLE IT SHOULD INCLUDE IN THE TABLE, OTHERWISE CHECK THE VALUE
      cost = graph[QUEUE[0]][node] + SCORE_TABLE[QUEUE[0]][VALUES_CONSTANT]

      if node not in SCORE_TABLE:
        SCORE_TABLE[node] =  { VALUES_CONSTANT : cost, PREVIOUS_NODE_CONSTANT : QUEUE[0] }
      else:
        if cost < SCORE_TABLE[node][VALUES_CONSTANT]:
          SCORE_TABLE[node] =  { VALUES_CONSTANT: cost, PREVIOUS_NODE_CONSTANT : QUEUE[0]}
    
      if node not in VISITED and node not in QUEUE:
        if(NEXT_FIRST_NEIGHBOR==node and shortest_path_found_bool == False):
          shortest_path_length += 1
          if(node == END_NODE):
            shortest_path_found_bool = True
          else:
            NEXT_FIRST_NEIGHBOR= list(graph[node].keys())[0]

        QUEUE   += [node]

    VISITED += QUEUE[0]
    QUEUE.pop(0)

  return SCORE_TABLE,shortest_path_length
  
    
def get_fastest_path(START_NODE, END_NODE, SCORE_TABLE,shortest_path):
  path = []
  boolean_similar = False
  node = END_NODE
  while  node != START_NODE:
    path.insert(0,node)
    node = SCORE_TABLE[node][PREVIOUS_NODE_CONSTANT]
  path.insert(0,node)


  if(len(path)-1 == shortest_path):
    boolean_similar = True
  else:
    boolean_similar = False

  return path, boolean_similar

SCORE_TABLE,shortest_path_len = generate_score_table()
fastest_path,boolean = get_fastest_path(START_NODE, END_NODE, SCORE_TABLE,shortest_path_len)

print("FASTEST PATH:",fastest_path)
print("BOOLEAN FOR SIMILARITY OF SHORTEST AND FASTEST:",boolean)
