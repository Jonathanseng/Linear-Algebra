import graphviz as gv

def make_concept_map(nodes, edges):
  """
  Creates a math concept map from a list of nodes and edges.

  Args:
    nodes: A list of strings representing the nodes in the concept map.
    edges: A list of tuples representing the edges in the concept map, where each
      tuple is of the form (source, target).

  Returns:
    A graphviz graph object representing the concept map.
  """

  graph = gv.Digraph()
  for node in nodes:
    graph.node(node)
  for source, target in edges:
    graph.edge(source, target)
  return graph

def main():
  """
  Example usage of the `make_concept_map` function.
  """

  nodes = ["Linear independence", "Linear dependence", "Basis", "Span"]
  edges = [(nodes[0], nodes[1]), (nodes[0], nodes[2]), (nodes[2], nodes[3])]
  graph = make_concept_map(nodes, edges)
  graph.render("linear_independence.png")

if __name__ == "__main__":
  main()
