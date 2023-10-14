# Cheat sheet

## general info
- only 0, "", [], {}, set(), () convert to false through bool()
- string[start:stop:step]
- 

## Virtual Environment
---
```console
saghal@saghal-PC:~$ virtualenv <env name>
saghal@saghal-PC:~$ source <env name>/bin/activate
saghal@saghal-PC:~$ deactivate
```


## String striding
---
```python
>>> s = 'King Arthur'
>>> s[::2]
'Kn rhr'
>>> s[1::2]
'igAtu'
```

## tuples
---
immutable
To change a tuple, you should create a new tuple.

## lists
---
mutable

### append
```python
>>> L = [ "Michael Jackson", 10.2]
>>> L.append(['pop', 10])
['Michael Jackson', 10.2, ['pop', 10]]
```
### extend
```python
>>> L = [ "Michael Jackson", 10.2]
>>> L.extend(['pop', 10])
['Michael Jackson', 10.2, 'pop', 10]
```
### split
```python
>>> 'hard rock'.split()
['hard', 'rock']
>>> 'A,B,C,D'.split(',')
['A', 'B', 'C', 'D']
```

### Copy and Clone List

#### copy
```python
>>> A = ["hard rock", 10, 1.2]
>>> B = A
```
![Copy](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/ListsRef.png)

#### clone
```python
>>> B = A[:]
```
![Clone](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%202/images/ListsVal.gif)

## dictionary
{key:value}
key should be unique

## set
A set is a unique collection of objects in Python. You can denote a set with a pair of curly brackets {}. Python will automatically remove duplicate items:





