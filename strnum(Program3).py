number = input("Enter a number: ")
number = int(number)
print("Your number multitplied by 2 is: " + str(number * 2))


---

### Code:

```python
number = input("Enter a number: ")   # Step 1
number = int(number)                 # Step 2
print("Your number multiplied by 2 is: " + str(number * 2))   # Step 3
```

---

### 🔎 Step 1: `input()`

* In Python, `input()` **always returns a string**, no matter what you type.
  Example:

```python
x = input("Enter: ")   # suppose you type 10
print(type(x))         # <class 'str'>
```

So here, `number` is initially a string, e.g., `"10"`.

---

### 🔎 Step 2: Convert to integer

```python
number = int(number)
```

* `"10"` → `10` (integer)
* Now `number` is an `int`, so you can do math.

---

### 🔎 Step 3: Printing

```python
print("Your number multiplied by 2 is: " + str(number * 2))
```

* `number * 2` is an **integer** (e.g., `20`).
* You can’t **concatenate string + int** directly in Python → it gives an error.
* That’s why we convert it with `str()`.
* `"Your number multiplied by 2 is: " + "20"` → one single string.

---

?
