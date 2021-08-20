# large-numbers
Large numbers info and calculations with programming languages.

# What are large numbers?

Q: Can you calculate 3²⁷ (or 3↑↑3) by hand?  
The answer is… 7625597484987, very large, right?  
But it is only a 13-digit number.  
What about 3⁷⁶²⁵⁵⁹⁷⁴⁸⁴⁹⁸⁷ (or 3↑↑4)?  
Do not try it with Python 3, or you will get a MemoryError.  
Well, it equals to 9³⁸¹²⁷⁹⁸⁷⁴²⁴⁹³·⁵ , and it is about 10³⁵⁵⁰⁰⁰⁰⁰⁰⁰⁰⁰⁰ .  
It is about 3550000000000-digit number!  
Next, there is 2 ways of common representations. They are Knuth's up-arrow notation and Conway's chain.  
All the arrows and chains are calculated from right to left.  
For example:  
x ↑ y = xʸ  
x ↑↑ y = x ↑² y = ʸx = x ↑ x ↑ …(“x” will be repeated for y times)… ↑ x ↑ x  
x ↑ᶻ y = x ↑↑↑…(“↑” will be repeated for z times)…↑↑↑ y  
x ↑ᶻ y = x ↑ᶻ⁻¹ x ↑ᶻ⁻¹ …(“x” will be repeated for y times)… ↑ᶻ⁻¹ x ↑ᶻ⁻¹ x  
1 ↑ⁿ m = 1  
2 ↑ⁿ 2 = 4  
m ↑ⁿ 1 = m  
x → y → z = x → (x → (y - 1) → z) → (z - 1)  
x → y → 1 = x → y  
x → y = xʸ (if the chain length is 2)  
x → y → z = x ↑ᶻ y (if the chain length is 3)  
x → 1 → n = x

Let us start.
### No.1 4 ↑↑ 4
S: 4 ↑↑ 4  
= 4 ↑ 4 ↑ 4 ↑ 4  
= 4 ↑ 4 ↑ 4⁴  
= 4 ↑ 4 ↑ 256  
= 4 ↑ 4²⁵⁶  
= 4 ↑ 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084096  
= 4¹³⁴⁰⁷⁸⁰⁷⁹²⁹⁹⁴²⁵⁹⁷⁰⁹⁹⁵⁷⁴⁰²⁴⁹⁹⁸²⁰⁵⁸⁴⁶¹²⁷⁴⁷⁹³⁶⁵⁸²⁰⁵⁹²³⁹³³⁷⁷⁷²³⁵⁶¹⁴⁴³⁷²¹⁷⁶⁴⁰³⁰⁰⁷³⁵⁴⁶⁹⁷⁶⁸⁰¹⁸⁷⁴²⁹⁸¹⁶⁶⁹⁰³⁴²⁷⁶⁹⁰⁰³¹⁸⁵⁸¹⁸⁶⁴⁸⁶⁰⁵⁰⁸⁵³⁷⁵³⁸⁸²⁸¹¹⁹⁴⁶⁵⁶⁹⁹⁴⁶⁴³³⁶⁴⁹⁰⁰⁶⁰⁸⁴⁰⁹⁶  
≈ 10⁸⁰⁴⁴⁶⁸⁴⁷⁵⁷⁹⁶⁵⁵⁵⁸²⁵⁹⁷⁴⁴⁴¹⁴⁹⁹⁸⁹²³⁵⁰⁷⁶⁷⁶⁴⁸⁷⁶¹⁹⁴⁹²³⁵⁵⁴³⁶⁰²⁶⁶³⁴¹³⁶⁸⁶⁶²³³⁰⁵⁸⁴¹⁸⁰⁴⁴¹²⁸¹⁸⁶⁰⁸¹¹²⁴⁵⁷⁸⁹⁰⁰¹⁴²⁰⁵⁶⁶¹⁴⁰¹⁹¹¹⁴⁹¹¹⁸⁹¹⁶³⁰⁵¹²²⁵²³²⁹⁶⁸⁷¹⁶⁷⁹⁴¹⁹⁶⁷⁸⁶⁰¹⁸⁹⁴⁰³⁶⁵⁰⁴⁶⁰

### No.2 2 ↑³ 6
S: 2 ↑³ 6  
= 2 ↑↑ 2 ↑↑ 2 ↑↑ 2 ↑↑ 2 ↑↑ 2  
= 2 ↑↑ 2 ↑↑ 2 ↑↑ 2 ↑↑ 4  
= 2 ↑↑ 2 ↑↑ 2 ↑↑ 2 ↑ 2 ↑ 2 ↑ 2  
= 2 ↑↑ 2 ↑↑ 2 ↑↑ 2 ↑ 2 ↑ 4  
= 2 ↑↑ 2 ↑↑ 2 ↑↑ 2 ↑ 2⁴  
= 2 ↑↑ 2 ↑↑ 2 ↑↑ 2 ↑ 16  
= 2 ↑↑ 2 ↑↑ 2 ↑↑ 2¹⁶  
= 2 ↑↑ 2 ↑↑ 2 ↑↑ 65536

### No.3 3→3→3
S: 3→3→3  
= 3 → (3 → (3 - 1) → 3) → (3 - 1)  
= 3 → (3 → 2 → 3) → 2  
= 3 → (3 → (3 → (2 - 1) → 3) → (3 - 1)) → 2  
= 3 → (3 → (3 → 1 → 3) → 2) → 2  
= 3 → (3 → 3 → 2) → 2  
= 3 → (3 → (3 → (3 - 1) → 2) → (2 - 1)) → 2  
= 3 → (3 → (3 → 2 → 2) → 1) → 2  
= 3 → (3 → (3 → (3 → (2 - 1) → 2) → (2 - 1))) → 2  
= 3 → (3 → (3 → (3 → 1 → 2) → 1)) → 2  
= 3 → (3 → (3 → 3)) → 2  
= 3 → (3 → 3³) → 2  
= 3 → (3 → 27) → 2  
= 3 → (3²⁷) → 2  
= 3 → 7625597484987 → 2  
= 3 ↑↑ 7625597484987
