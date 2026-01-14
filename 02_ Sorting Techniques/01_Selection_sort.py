arr = [13,46,24,52,20,9]


for i in range(0,len(arr)-1):
  small = i
  for j in range(i+1,len(arr)):
    
    if(arr[small]>arr[j]):
      small = j
    
  a = arr[small]
  arr[small] = arr[i]
  arr[i] = a

print(arr) 


# Time Complexity:O(N^2),Selection sort runs in O(N²) time in the best, average, and worst cases due to its nested loop structure. It makes approximately N(N-1)/2 comparisons, regardless of the array's initial state. Even if no swaps are needed (best case), the number of comparisons remains the same./p>

# Space Complexity: O(1). No extra space used


















# Below is a **clear, exam- and interview-oriented explanation** covering **built-in sorting**, **time complexity**, **7 common sorting algorithms**, and **when to use which**.

# ---

# ## 1. Python Built-in Sort (`sort()` / `sorted()`)

# ### What algorithm does Python use?

# Python uses **Timsort** (a hybrid of Merge Sort and Insertion Sort).

# ### Time Complexity

# | Case         | Time Complexity                     |
# | ------------ | ----------------------------------- |
# | Best case    | **O(n)** (already or nearly sorted) |
# | Average case | **O(n log n)**                      |
# | Worst case   | **O(n log n)**                      |

# ### Space Complexity

# * **O(n)** (needs extra memory)

# ### Advantages

# * Very fast in practice
# * Stable (keeps relative order of equal elements)
# * Handles real-world data efficiently

# ### Example

# ```python
# arr.sort()
# # or
# sorted(arr)
# ```

# ---

# ## 2. Can we always use the built-in sort?

# ### Short answer: **YES, in real-world coding**

# ### But NOT always in:

# * Coding interviews
# * Competitive programming (sometimes)
# * When memory usage is strictly limited
# * When the problem explicitly asks for a specific algorithm

# ---

# ## 3. Seven Common Sorting Algorithms (Comparison)

# | Algorithm      | Best       | Average    | Worst      | Space    | Stable |
# | -------------- | ---------- | ---------- | ---------- | -------- | ------ |
# | Bubble Sort    | O(n)       | O(n²)      | O(n²)      | O(1)     | Yes    |
# | Selection Sort | O(n²)      | O(n²)      | O(n²)      | O(1)     | No     |
# | Insertion Sort | O(n)       | O(n²)      | O(n²)      | O(1)     | Yes    |
# | Merge Sort     | O(n log n) | O(n log n) | O(n log n) | O(n)     | Yes    |
# | Quick Sort     | O(n log n) | O(n log n) | O(n²)      | O(log n) | No     |
# | Heap Sort      | O(n log n) | O(n log n) | O(n log n) | O(1)     | No     |
# | Counting Sort  | O(n + k)   | O(n + k)   | O(n + k)   | O(k)     | Yes    |

# ---

# ## 4. Which Sorting Algorithm is Best?

# ### There is **NO single best sorting algorithm**

# It depends on the **problem constraints**.

# ---

# ## 5. When to Use Which Sorting Method

# ### Use Built-in Sort (Timsort) when:

# * Writing production / real-world code
# * Input size is large
# * Data may already be partially sorted
# * Stability matters

# **Recommended choice 90% of the time**

# ---

# ### Use Merge Sort when:

# * Stable sorting is required
# * Working with linked lists
# * Predictable performance needed

# ---

# ### Use Quick Sort when:

# * Memory is limited
# * Average-case speed is important
# * Interview questions

# ---

# ### Use Heap Sort when:

# * Worst-case time must be guaranteed
# * Constant extra space required

# ---

# ### Use Insertion Sort when:

# * Array is very small
# * Data is almost sorted

# ---

# ### Use Counting Sort when:

# * Numbers are in a small fixed range
# * Sorting integers only
# * Performance is critical

# ---

# ## 6. Real-World Rule (Very Important)

# > **Always use the built-in sort unless you have a specific reason not to.**

# Python’s built-in sort is:

# * Faster than most custom implementations
# * Well-tested
# * Optimized at C-level

# ---

# ## 7. Interview Tip

# If asked:

# > “Which sorting algorithm would you use?”

# Answer:

# > “In practice, I use Python’s built-in Timsort. If required to implement manually, I choose Merge Sort for stability or Quick Sort for performance.”

# ---

# ## 8. Summary (Easy to Remember)

# * Built-in sort = **Best for real-world**
# * No single best sorting algorithm
# * Different problems → different sorting methods
# * Interviews ≠ real-world coding

# If you want, I can also give:

# * A **1-line answer for exams**
# * A **decision chart**
# * A **real-life analogy**

# Just tell me.
