### VNS: Variable neighborhood search

##### Reference: Hansen P, Mladenović N. Variable neighborhood search: Principles and applications[J]. European Journal of Operational Research, 2001, 130(3): 449-467.

##### The variable neighborhood search (VNS) for the traveling salesman problem (TSP).

| Variables  | Meaning                                                      |
| ---------- | ------------------------------------------------------------ |
| coord_x    | The x coordinate of the cities                               |
| coord_y    | The y coordinate of the cities                               |
| k_max      | The maximum number of non-progressive iterations             |
| operator   | The local search operator (default two-point reversion)      |
| num_cities | The number of cities                                         |
| dis_matrix | The distance matrix, dis_matrix[i, j] denotes the distance between cities i and j |
| path       | The current global-best path                                 |
| dis        | The current global-best distance                             |

##### Operation: two-point reversion

path: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

reversion(path, 2, 5): [0, 1, 5, 4, 3, 2, 6, 7, 8, 9]

##### Local search: 

Perfrom all possible two-point reversion operations on a path until no progression.

##### Shaking: 

Randomly perform k times two-point reversion. The shaking process introduces variability into the algorithm. It effectively generates a fresh initial point by modifying the current solution. The aim is to break away from local optima and investigate different areas of the solution space.

-------

#### Test problem

A randomly-generated TSP with 50 cities.

#### Example

```python
if __name__ == '__main__':
    min_coord = 0
    max_coord = 10
    city_num = 50
    x = np.random.uniform(min_coord, max_coord, city_num)
    y = np.random.uniform(min_coord, max_coord, city_num)
    print(main(x, y, 100))
```

##### Output:

![](https://github.com/Xavier-MaYiMing/Variable-Neighborhood-Search/blob/main/VNS%20for%20TSP.png)



