# Hashtable 8000
This vjass library adds several new types. Each type is a wrapper for convenient access to a native hash table. Now they can be created, deleted, saved and passed as a parameter.
## Library scope
- Persistent storage
- Temporary storage
- Passing a lot of parameters to a function
## Specifications
- The maximum number of elements within a table is up to 18747
- The maximum number of tables is up to 8190
- Since these tables are based on a native hashtable, they have the same data storage features. Namely: if you delete an object of a reference type (for example, call RemoveUnit() or the unit will simply decompose), then its value in the table will automatically become null, although the cell will not be freed. If you refer to a non-existent element, then in response you will get the same as if you accessed the standard jass hashtable (null, 0 or false)
- All type names look like **h8k_type**, where type is the name of the native **type** for which the table is being created. The key is always an integer type. Example of a table for the real type:
```scala
local h8k_real var = h8k_real.create()
set var[-81] = 15 // save
set var[R2I(var[-81])] = 7 // equivalent to var[15] = 7
// var[15] -> 7.
set var.remove(15) // deallocate
// var[15] -> 0.
set var.destroy() // delete a table
```
<details>
	<summary>List of supported data types</summary>

- (string)
- (destructable)
- (effect)
- (integer)
- (item)
- (lightning)
- (multiboard)
- (multiboarditem)
- (player)
- (real)
- (rect)
- (region)
- (timer)
- (trigger)
- (unit)
</details>

## Example 1
In this example, the tables are used as Databases so that you can find out its "element" by the unit.

https://user-images.githubusercontent.com/103655830/165356868-a9712c33-0ef0-45cb-9a22-3de9cf5b9c0b.mp4
## Example 2
In this example, the table is used to store the positions of 3 effects, although it is passed as 1 object.

![2](https://user-images.githubusercontent.com/103655830/165356895-e34a05df-f194-4eba-b627-5bbf64424be7.gif)
