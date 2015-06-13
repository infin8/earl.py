# earl.py
simple url parameter manipulation

# Usage
```
In [1]: from earl import Url

In [2]: u = Url('https://www.youtube.com/watch?v=Cb7XdHyfgsA&list=RDCb7XdHyfgsA')

In [3]: u.set('t', '2m14s')
Out[3]: https://www.youtube.com/watch?v=Cb7XdHyfgsA&list=RDCb7XdHyfgsA&t=2m14s

In [4]: u.query.pop('list')
Out[4]: 'RDCb7XdHyfgsA'

In [5]: u
Out[5]: https://www.youtube.com/watch?v=Cb7XdHyfgsA&t=2m14s

In [6]: u.query
Out[6]: {"v": "Cb7XdHyfgsA", "t": "2m14s"}
```
