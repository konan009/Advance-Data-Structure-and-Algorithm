VALUES_CONSTANT = "values"
PREVIOUS_NODE_CONSTANT = "previous_vertex"

def get_fastest_path(START_NODE, END_NODE, SCORE_TABLE):
  path = []
  node = END_NODE
  while  node != START_NODE:
    path.insert(0,node)
    node = SCORE_TABLE[node][PREVIOUS_NODE_CONSTANT]

  path.insert(0,node)
  return path

# GENERATES SCORE TABLE FOR DIJKSTRA ALGORITHM
def generate_score_table():
  SCORE_TABLE = {}
  QUEUE   = [START_NODE]
  SCORE_TABLE[START_NODE] = { VALUES_CONSTANT :0}
  VISITED = []
  # IMPLEMENT BFS
  while len(QUEUE) > 0:
    for node in graph[QUEUE[0]].keys():
      # IF THE !EXIST IN THE TABLE IT SHOULD INCLUDE IN THE TABLE, OTHERWISE CHECK THE VALUE

      cost =graph[QUEUE[0]][node] + SCORE_TABLE[QUEUE[0]][VALUES_CONSTANT]

      if node not in SCORE_TABLE:
        SCORE_TABLE[node] =  { VALUES_CONSTANT : cost, PREVIOUS_NODE_CONSTANT : QUEUE[0] }
      else:
        if cost < SCORE_TABLE[node][VALUES_CONSTANT]:
          SCORE_TABLE[node] =  { VALUES_CONSTANT: cost, PREVIOUS_NODE_CONSTANT : QUEUE[0]}
      
      if node not in VISITED and node not in QUEUE:
        QUEUE   += [node]

    VISITED += QUEUE[0]
    QUEUE.pop(0)

  return SCORE_TABLE


START_NODE = "A"
END_NODE = "F"
PROBLEM = "1A"

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
    "B" :  8 ,
    "D" :  7  
  },
  "D" : {
    "F" :  1  
  },
  "F" : {
      
  }
}

SCORE_TABLE = generate_score_table()
FASTEST_PATH = get_fastest_path(START_NODE, END_NODE, SCORE_TABLE)
print( "PROBLEM:" , PROBLEM)
print( "STARTING NODE:" ,START_NODE," ENDING NODE:" ,END_NODE )
print("FASTEST PATH:" ,FASTEST_PATH)
print("FASTEST PATH SCORE:" ,SCORE_TABLE[END_NODE][VALUES_CONSTANT])

START_NODE = "A"
END_NODE = "E"
PROBLEM = "1B"
graph = {
  "A": {
    "B" : 10
  },
  "B": {
    "C" : 20 ,
  },
  "C" : {
    "D" :  1 ,
    "E" :  30
  },
  "D" : {
    "B" :  1,
  },
  "E" : {
  }
}
print("")
SCORE_TABLE = generate_score_table()
FASTEST_PATH = get_fastest_path(START_NODE, END_NODE, SCORE_TABLE)
print( "PROBLEM:" , PROBLEM)
print( "STARTING NODE:" ,START_NODE," ENDING NODE:" ,END_NODE )
print("FASTEST PATH:" ,FASTEST_PATH)
print("FASTEST PATH SCORE:" ,SCORE_TABLE[END_NODE][VALUES_CONSTANT])
