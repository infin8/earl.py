# earl.py
simple url parameter manipulation

# Usage
```
In [1]: from earl import Url

In [2]: u = Url('https://www.youtube.com/watch?v=Cb7XdHyfgsA&list=RDCb7XdHyfgsA')

In [3]: u.set(t='2m14s') #set the value of parameter: t
Out[3]: https://www.youtube.com/watch?v=Cb7XdHyfgsA&list=RDCb7XdHyfgsA&t=2m14s

In [4]: u.set(('t','1s')) #pass a list of tuples to retain order
Out[4]: https://www.youtube.com/watch?v=Cb7XdHyfgsA&list=RDCb7XdHyfgsA&t=1s

In [5]: u.query.pop('list') #remove a parameter
Out[5]: 'RDCb7XdHyfgsA'

In [6]: u #the Url object is represented as the updated url
Out[6]: https://www.youtube.com/watch?v=Cb7XdHyfgsA&t=1s

In [7]: u.query #query is represented as json if you need it
Out[7]: {"v": "Cb7XdHyfgsA", "t": "1s"}
```
