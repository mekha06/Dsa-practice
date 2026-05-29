#Find Duplicate Element
#You are given an array and need to find elements that appear more than once.
#Example: [1, 3, 2, 3, 4, 1]
#Duplicates: 1, 3

arr=list(map(int,input("enter the array elements : ").split()))
freq_dict={}
for num in arr:
    if num in freq_dict:
        freq_dict[num]+=1
    else:
        freq_dict[num]=1
duplicates=[]
for key, value in freq_dict.items():
   if freq_dict[key]>1: #note we can use value directly here like value>1
       duplicates.append(key)
print("the duplicates are : " , duplicates)

"""
-------------------------------------Output-------------------------------------------
nter the array elements : 1 3 2 3 4 1
the duplicates are :  [1, 3]

-----------------------------------No confusion on dictionary funcs anymore----------------------------
| Function               | Purpose                   | Example                 | Output / Effect             |
| ---------------------- | ------------------------- | ----------------------- | --------------------------- |
| `get(key)`             | Safely get value          | `d.get("name")`         | Returns value or `None`     |
| `get(key, default)`    | Get with fallback         | `d.get("age", 0)`       | Returns 0 if key not found  |
| `keys()`               | All keys                  | `d.keys()`              | `dict_keys([...])`          |
| `values()`             | All values                | `d.values()`            | `dict_values([...])`        |
| `items()`              | Key-value pairs           | `d.items()`             | `dict_items([...])`         |
| `update()`             | Add/update multiple items | `d.update({"a":1})`     | Modifies dictionary         |
| `pop(key)`             | Remove key                | `d.pop("age")`          | Removes key & returns value |
| `popitem()`            | Remove last inserted item | `d.popitem()`           | Removes last pair           |
| `setdefault(key, val)` | Add key if not exists     | `d.setdefault("x", 10)` | Adds only if missing        |
| `clear()`              | Remove all items          | `d.clear()`             | Empty dictionary            |


"""