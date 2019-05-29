# PyCalc

## Dependencies
- [print](https://github.com/thetianshuhuang/print)

## Usage

On linux, you can install pycalc with
```shell
make install
```

or, if python 2 is desired,
```shell
make install-py2
```

Otherwise, run
```shell
python -i pycalc.py
```

for the full shell experience, or
```shell
python pycalc.py 'your expression here'
```

to evaluate a single command:
```shell
$ alias c='python pycalc.py'
$ c 1 + 1
[pycalc] 1 + 1 = 2
```

## AC Circuits Module


First, set the frequency ```ac.w```:
```python
>>> ac.w = 1000
```

Create circuit elements with the ```ac``` module:
- ```ac.R```: resistor
- ```ac.C```: capacitor
- ```ac.L```: inductor
- ```ac.Ph```: generic phasor

These components can be combined in series or parallel:

```python
>>> ac.w = 1000
>>> C1 = ac.C(10**-4)
>>> C2 = ac.C(10**-3)
>>> L1 = ac.L(10**-2)
>>> C1, C2, L1
(Phasor 10.0 <-90.0, Phasor 1.0 <-90.0, Phasor 10.0 <90.0)
>>> Z = C1 + (C2 | L1)
>>> Z
Phasor 11.111 <-90.0
>>> Z.rect()
(6.803593328596406e-16-11.11111111111111j)
```

## Configuration

Edit ```config.py``` to add more modules to import on startup.

```
{
    "name": name of module,
    "namespace": name to import as; if None, the module is imported as *
        (directly to global namespace)
    "config": configuration options to pass to the _init method of the module
        (optional)
}
```


## Changes

### v0.1
Initial version. Features dynamic module loading, and a configurable math bindings module.

### v0.2
Added Phasor library and installer.

### v0.3
Added AC Circuits library

### v1.0
Added invidual command execution

### v1.1
Made error messages red to ease readability
