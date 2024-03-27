# min_edge_cut_multiple_st

Python function to find the minimum edge cut for multiple source and target nodes.
Functions using a multigraph approach.

Recommendations

Create graphs with an **edge_id** attribute and when calling the function use 
```python
 min_edge_cut_multiple_st(G,source,targets,edge_id='edge_id')
```
This will return the exact edges as present in the original graph, rather than the edges in the multigraph
