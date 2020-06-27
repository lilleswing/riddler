```python
from itertools import product
from collections import defaultdict
```


```python
dirs = ['left', 'right']
cur_dir = 'north'

transitions = {
    ('north', 'left'): 'east',
    ('north', 'right'): 'west',
    ('east', 'left'): 'north',
    ('east', 'right'): 'south',
    ('south', 'left'): 'east',
    ('south', 'right'): 'west',
    ('west', 'left'): 'south',
    ('west', 'right'): 'north'
}
counts = defaultdict(int)
for steps in product(dirs, repeat=10):
    cur_dir = 'north'
    for step in steps:
        cur_dir = transitions[(cur_dir, step)]
    counts[cur_dir] += 1
```


```python
counts['north'] / sum(counts.values())
```




    0.5




```python
dirs = ['left', 'right', 'straight']

transitions = {
    ('north', 'left'): 'east',
    ('north', 'right'): 'west',
    ('east', 'left'): 'north',
    ('east', 'right'): 'south',
    ('south', 'left'): 'east',
    ('south', 'right'): 'west',
    ('west', 'left'): 'south',
    ('west', 'right'): 'north'
}
counts = defaultdict(int)
for steps in product(dirs, repeat=10):
    cur_dir = 'north'
    for step in steps:
        if step == 'straight':
            continue
        cur_dir = transitions[(cur_dir, step)]
    counts[cur_dir] += 1
counts
```




    defaultdict(int,
                {'north': 14763, 'south': 14762, 'east': 14762, 'west': 14762})




```python
counts['north'] / sum(counts.values())
```




    0.25001270131585634




```python

```
